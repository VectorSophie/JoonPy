import math

s = input().strip()
t = input().strip()

lcm_length = (len(s) * len(t)) // math.gcd(len(s), len(t))

s_repeat = s * (lcm_length // len(s))
t_repeat = t * (lcm_length // len(t))

if s_repeat == t_repeat:
    print(1)
else:
    print(0)
