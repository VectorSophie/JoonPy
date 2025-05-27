scores = [int(input()) for _ in range(5)]
adjust = [score if score >= 40 else 40 for score in scores]
print(sum(adjust) // 5)