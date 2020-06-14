#Problem ID: MISSP
#Problem Name: Chef and Dolls

for _ in range(int(input())):
    dolls = []
    for __ in range(int(input())):
        dolls.append(int(input()))

    arr = [False] * max(dolls)
    for i in dolls:
        arr[i - 1] += 1

    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            print(i + 1)

