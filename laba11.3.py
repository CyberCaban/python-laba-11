import os.path

path = "./data/laba11.3-input.txt"
if not os.path.exists(path):
    print("файла нет")
    exit()

with open(path, encoding="utf-8") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.split(","), lines))
lines = [[lines[i][x].replace("\n", "").replace(" ", "") for x in range(len(lines[i]))] for i in range(len(lines))]

# print("lines: ", lines)

heap = list()

maxlen = max((len(lines[x]) for x in range(len(lines))))
j = 0
while j < maxlen:
    for i in range(len(lines)):
        if lines[i]:
            heap.append(lines[i].pop(0))
    j += 1

print("очередь: ", " ".join(heap))
