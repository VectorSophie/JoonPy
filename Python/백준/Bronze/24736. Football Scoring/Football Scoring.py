import sys
def score(T,F,S,P,C):
    return T*6 + F*3 + S*2 + P*1 + C*2
t1,f1,s1,p1,c1 = map(int,sys.stdin.readline().split())
t2,f2,s2,p2,c2 = map(int,sys.stdin.readline().split())
print(score(t1,f1,s1,p1,c1), score(t2,f2,s2,p2,c2))