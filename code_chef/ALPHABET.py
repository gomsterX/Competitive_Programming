#Problem ID: ALPHABET
#Problem Name: Studying Alphabet

s = set(list(input()))
for _ in range(int(input())):
    if(set(list(input())).issubset(s)):
        print("Yes")
    else:
        print("No")
