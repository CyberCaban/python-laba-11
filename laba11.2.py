print("введите строку для инвертирования")
s = list(input())


def invert(string):
    for i in range(len(string)):
        heap.append(s.pop())


heap = list()
invert(s)
print("инвертированная строка")
print(''.join(heap))
