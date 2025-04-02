T = int(input())  
for _ in range(T): 
    R, S = input().split()  
    R = int(R)  
    ans = [char * R for char in S]  
    print("".join(ans)) 

        