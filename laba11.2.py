heap = list()
s = list(input())


def invert(string):
    for i in range(len(string)):
        heap.append(s.pop())


invert(s)
print(heap)
