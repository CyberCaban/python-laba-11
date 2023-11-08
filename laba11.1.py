def pal_check(string, mod_2):
    for i in range(len(string)):
        del_el = string.pop()
        if not del_el == s[int(len(s) / 2 + i + mod_2)]:
            print("не палиндром")
            exit()


print("введите слово для проверки на палиндром")
s = list(input())
heap = list()

if len(s) < 3:
    print("в слове меньше 3 букв")
    exit()

for i in range(int(len(s) / 2)):
    heap.append(s[i])

even_or_odd = len(s) % 2

pal_check(heap, even_or_odd)

print("палиндром")
