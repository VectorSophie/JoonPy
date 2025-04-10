import sys
from collections import Counter

def stats(numbers):
    N = len(numbers)
    numbers.sort()
    
    mean = round(sum(numbers) / N)

    median = numbers[N // 2]

    count = Counter(numbers)
    most_common = count.most_common()
    max_freq = most_common[0][1]

    modes = [num for num, freq in most_common if freq == max_freq]
    modes.sort()
    mode_val = modes[0] if len(modes) == 1 else modes[1]

    rangenumbers = numbers[-1] - numbers[0]

    return mean, median, mode_val, rangenumbers

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

mean, median, mode_val, rangenumbers = stats(numbers)
print(mean)
print(median)
print(mode_val)
print(rangenumbers)
