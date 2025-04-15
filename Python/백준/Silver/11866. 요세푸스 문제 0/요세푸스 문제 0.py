from queue import Queue

def yosif(n, k) :
    q = Queue()
    result = []

    for i in range(1, n+1):
        q.put(i)

    while not q.empty():
        for i in range(k):
            num = q.get()

            if i == k - 1:
                result.append(str(num))
            else:
                q.put(num)     
    return result

N,K = map(int,input().split())
yosifos = yosif(N,K)

print("<"+", ".join(yosifos)+">")