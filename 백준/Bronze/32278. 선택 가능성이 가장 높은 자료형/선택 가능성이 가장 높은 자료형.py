N = int(input().strip())
print("short"if -32768<=N<=32767 else("int"if-2147483648<=N<=2147483647 else "long long"))

