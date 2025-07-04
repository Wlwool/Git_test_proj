"""Fitch Cheney's Five Card Trick
In this classic 5-card trick, a Magician and his Assistant work together.

Setup
Five cards are randomly selected from a standard deck of Cards and
given to the Assistant.

The Assistant

chooses to hide one card
presents remaining four cards in a specific order to the Magician.
Using only those four cards and the agreed method the Magician must
determine the hidden card.

Task
Implement two functions:

assistant: Takes a list of 5 cards and returns 4 cards in a specific order.
magician: Takes the 4 cards shown by the Assistant and returns the hidden card.
Notes
Each card is represented as a 2-character string: a rank ("23456789TJQKA")
followed by a suit
("cdhs" for clubs, diamonds, hearts, spades). For example, "Jh"
is the Jack of hearts.
The magician should return a result for any 4-card input — even ones
that would never realistically be passed by the assistant. These cases
won't be judged for correctness, but your solution must not crash
or raise an exception.
"""

suit_priority = {"c": 0, "d": 1, "h": 2, "s": 3}
rank_order = "A23456789TJQK"


def assistant(five_cards):
    # Группировка карт по масти
    suits = {}
    for card in five_cards:
        suit = card[1]
        if suit not in suits:
            suits[suit] = []
        suits[suit].append(card)

    # Выбор масти с >= 2 картами и наивысшим приоритетом
    candidate_suit = None
    for suit, cards in suits.items():
        if len(cards) >= 2:
            if (
                candidate_suit is None
                or suit_priority[suit] > suit_priority[candidate_suit]
            ):
                candidate_suit = suit
    if candidate_suit is None:  # Если не нашли (редкий случай)
        for suit, cards in suits.items():
            if len(cards) >= 2:
                candidate_suit = suit
                break
    if candidate_suit is None:  # Если всё ещё нет, вернуть последние 4 карты
        return five_cards[1:]

    cards_in_suit = suits[candidate_suit]

    # Функция сортировки карт масти по рангам
    def get_rank_index(card):
        return rank_order.index(card[0])

    cards_in_suit.sort(key=lambda card: get_rank_index(card))

    # Выбор двух карт: a это младшая, b это старшая
    a, b = cards_in_suit[0], cards_in_suit[1]
    rank_a = get_rank_index(a)
    rank_b = get_rank_index(b)
    d = rank_b - rank_a

    if d <= 6:
        indicator = a
        hidden = b
        s_val = d
    else:
        indicator = b
        hidden = a
        s_val = 13 - d

    # Подготовка оставшихся трёх карт
    remaining = [card for card in five_cards if card != indicator and card != hidden]

    # Функция для сортировки карт - масть -> ранг
    def card_key(card):
        s_pri = suit_priority[card[1]]
        r_idx = get_rank_index(card)
        return (s_pri, r_idx)

    remaining_sorted = sorted(remaining, key=card_key)

    # Перестановки для кодирования s_val (0-5)
    permutations = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    perm_index = s_val - 1
    if perm_index < 0 or perm_index >= 6:
        perm_index = 0
    perm = permutations[perm_index]
    ordered_remaining = [remaining_sorted[i] for i in perm]

    return [indicator] + ordered_remaining


def magician(four_cards_list):
    if len(four_cards_list) < 4:
        return "As"  # Заглушка при ошибочном вводе

    indicator = four_cards_list[0]
    three_cards = four_cards_list[1:]

    # Функция для сортировки карт (как у ассистента)
    def card_key(card):
        s_pri = suit_priority[card[1]]
        r_idx = rank_order.index(card[0])
        return (s_pri, r_idx)

    # Определение s по порядку трёх карт
    sorted_three_cards = sorted(three_cards, key=card_key)
    index_map = {card: idx for idx, card in enumerate(sorted_three_cards)}
    try:
        indices = [index_map[card] for card in three_cards]
    except:
        indices = [0, 1, 2]  # при ошибке используем порядок по умолчанию

    permutations = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    try:
        s_val = permutations.index(indices) + 1
    except:
        s_val = 1  # по умолчанию

    # Вычисление скрытой карты
    rank_idx_indicator = rank_order.index(indicator[0])
    rank_hidden = (rank_idx_indicator + s_val) % 13
    hidden_rank = rank_order[rank_hidden]
    hidden_card = hidden_rank + indicator[1]  # Масть как у индикатора

    return hidden_card


def test_magician_guess_correctly():
    test_cases = [
        ["6c", "3h", "Jh", "Ac", "3c"],
        ["6c", "Qs", "5d", "Kd", "Qd"],
        ["7h", "Ah", "5h", "3c", "Jh"],
        ["7s", "9s", "5s", "Kh", "3s"],
        ["As", "Jd", "2s", "Qc", "2h"],
    ]

    for cards in test_cases:
        # Ассистент обрабатывает 5 карт
        revealed = assistant(cards)

        # Маг угадывает скрытую карту
        guess = magician(revealed)

        # Определяем реально скрытую карту
        hidden_card = list(set(cards) - set(revealed))[0]

        # Проверка на совпадение
        if guess == hidden_card:
            print(f"[+] Верно: {cards} -> Угадана {guess} (Скрыта: {hidden_card})")
        else:
            print(f"[X] Ошибка: {cards} -> Угадана {guess}, но должна быть {hidden_card}")


test_magician_guess_correctly()
