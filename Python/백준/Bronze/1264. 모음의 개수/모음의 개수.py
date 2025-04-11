while True:
    a = input()
    cnt = 0
    if a == "#":
        break

    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'A' or a[i] == 'e' or a[i] == 'E' or a[i] == 'o' or a[i] == 'O' or a[i] == 'u' or a[i] == 'U' or a[i] == 'i' or a[i] == 'I':
            cnt+=1
    print(cnt)