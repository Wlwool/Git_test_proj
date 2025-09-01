"""
Скрипт для решения задачи "Угадать слова на 5 букв"

Вводить подсказки в чат-режиме:
forbid а / pos 2 и / notpos 3 а / have е 2 / suggest

для загрузки слов:
https://raw.githubusercontent.com/Harrix/Russian-Nouns/refs/heads/main/dist/russian_nouns.txt | grep -x '.\{5\}' > words.txt

"""

from collections import Counter, defaultdict


WORDS_FILE = "words.txt"
AVOID_REPEAT_LETTER_EARLY = True
MAX_SUGGESTIONS = 8


def load_words(path):
    """Загрузка слова из файла."""
    with open(path, encoding="utf-8") as f:
        words = [w.strip().lower() for w in f if len(w.strip()) == 5]
    return words


class Constraints:
    def __init__(self):
        self.must_have = defaultdict(set)  # # буква -> минимальное количество в слове (вдоль можно расширить)
        self.must_positions = dict()  # pos(0..4) -> буква (фиксированная)
        self.cannot_positions = defaultdict(set)  # буква -> set(позиции где не может быть)
        self.forbidden = set()  # буквы которых точно нет в слове

    def matches(self, word):
        # запрещенные буквы
        if any(c in self.forbidden for c in word):
            return False
        # фиксированные позиции
        for position, c in self.must_positions.items():
            if word[position] != c:
                return False
        # позиции в которых не может быть буквы
        for c, bad_position in self.cannot_positions.items():
            for pos in bad_position:
                if word[pos] == c:
                    return False
        # минимальное количество букв
        word_counter = Counter(word)
        for c, count in self.must_have.items():
            if word_counter[c] < count:
                return False
        return True

# Оценка информационной ценности слова
def score_word(word, pool, constraints):
    """
    # 1) Частота букв в пуле (исключая уже запрещённые и уже фиксированные позиции)
    # 2) Награда за уникальные буквы в слове (мы хотим покрыть как можно больше разных букв)
    """
    pool_letters = "".join(pool)
    frequency = Counter(pool_letters)

    unique_letters = set(word)
    # низкая ценность если содержит буквы, уже в must_positions (повторы)
    already_known = set(constraints.must_positions.values())
    new_letters = unique_letters - already_known

    # score: сумма частот новых букв (чем чаще буква в пуле — тем важнее проверить её)
    score = sum(frequency[c] for c in new_letters if c not in constraints.forbidden)

    # небольшой штраф за повтор букв внутри слова (если AVOID_REPEAT_LETTER_EARLY)
    if AVOID_REPEAT_LETTER_EARLY:
        repeats = len(word) - len(set(word))
        score = score - repeats * (0.5 * max(1, score))

    # позиционный бонус: слово ставит букву в позицию, которая ещё не проверена
    # (если буква стоит в позиции, где constraints не заданы, даём бонус)

    position_bonus = 0
    for i, c in enumerate(word):
        if i not in constraints.must_positions :
            position_bonus += (1 if c in new_letters else 0)
    score += 0.1 * position_bonus

    return score

# Основная логика выбора
def suggest_new_words(all_words, constraints, top_n=5):
    pool = [w for w in all_words if constraints.matches(w)]
    if not pool:
        return [], pool

    # пересчет частоты букв в пуле
    freq = Counter("".join(pool))
    scored = []
    for w in pool:
        s = score_word(w, pool, constraints)
        scored.append((s, w))

    scored.sort(reverse=True)
    suggestions = [w for _, w in scored[:top_n]]
    return suggestions, pool

def interactive_mode():
    all_words = load_words(WORDS_FILE)
    cons = Constraints()

    print("Загружено слов:", len(all_words))
    print("Интерактивный режим. Вводи команды:")
    print("  forbid X (добавить букву в forbidden)")
    print("  pos i X (фиксировать букву X в позиции i, i от 1 до 5)")
    print("  notpos i X (буква X не может быть в позиции i)")
    print("  have X n  (буква X есть минимум n раз)")
    print("  suggest (получить подсказки)")
    print("  pool (сколько кандидатов осталось)")
    print("  exit")

    while True:
        try:
            cmd = input("> ").strip().lower()
            if not cmd:
                continue
            parts = cmd.split()

            if parts[0] == "forbid" and len(parts) == 2:
                cons.forbidden.add(parts[1])
                print("Добавлено в forbidden:", parts[1])
            elif parts[0] == "pos" and len(parts) == 3:
                i = int(parts[1]) - 1
                cons.must_positions[i] = parts[2]
                print("Фиксировано:", parts[2], "в позиции", i + 1)
            elif parts[0] == "notpos" and len(parts) == 3:
                i = int(parts[1]) - 1
                cons.cannot_positions[parts[2]].add(i)
                print("Буква", parts[2], "не в позиции", i + 1)
            elif parts[0] == "have" and len(parts) == 3:
                cons.must_have[parts[1]] = int(parts[2])
                print("Минимум", parts[2], "букв", parts[1])
            elif parts[0] == "suggest":
                suggestions, pool = suggest_new_words(all_words, cons, top_n=MAX_SUGGESTIONS)
                print("Оставшихся кандидатов:", len(pool))
                print("Топ подсказок:", suggestions)
            elif parts[0] == "pool":
                pool = [w for w in all_words if cons.matches(w)]
                print("Кандидатов:", len(pool))
                if len(pool) <= 50:
                    print(pool)
            elif parts[0] == "exit":
                break
            else:
                print("Неизвестная команда")
        except KeyboardInterrupt:
            if input("\nВы уверены, что хотите выйти? (y/n) ").lower() == "y":
                print("До свидания!")
                break
            else:
                print("Продолжаем...")


if __name__ == "__main__":
    interactive_mode()
