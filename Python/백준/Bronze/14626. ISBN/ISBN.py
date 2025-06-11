def totalcode(arrcode):
    total = 0
    for i in range(12):
        digit = int(arrcode[i])
        if i % 2 == 1:
            total += 3 * digit
        else:
            total += digit
    return (10 - (total % 10)) % 10

def isbn_scan(isbn):
    isbn_arr = list(isbn)
    target = isbn_arr.index('*')
    answer = int(isbn_arr[12])

    for guess in range(10):
        isbn_arr[target] = str(guess)
        if totalcode(isbn_arr) == answer:
            return guess

isbn = input()
print(isbn_scan(isbn))
