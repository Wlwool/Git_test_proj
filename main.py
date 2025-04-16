# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/Wlwool/Git_test_proj.git
# git push -u origin main


print("Из обеих веток конфликт разрешен")

class ListWrapper(list):
    def __init__(self, iterable):
        self._list = list(iterable)

    def __getitem__(self, index):
        return self._list[index]

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return f"ListWrapper (length: {len(self)}, elements: {self._list})"

wrapper = ListWrapper([1, 2, 3])
print(wrapper)          # Вывод: ListWrapper (length: 3, elements: [1, 2, 3])
print(wrapper[0])


print("Привет из branch-a")
