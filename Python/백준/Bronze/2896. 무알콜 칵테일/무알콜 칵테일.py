A, B, C = map(float, input().split())
I, J, K = map(float, input().split())

x = min(A / I, B / J, C / K)

left_A = A - I * x
left_B = B - J * x
left_C = C - K * x

print(f"{left_A:.10f} {left_B:.10f} {left_C:.10f}")