def toString(List): 
    return ''.join(List) 
  
def permuteStr(a, l, r): 
    if l == r: 
        return(toString(a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permuteStr(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] 
  

def factorial(N):
    res = 1
    for i in range (N):
        res = res * (i + 1)
    return res

def permute(N, R):
    return factorial(N) / factorial(N - R)

'''
while True:
    string = input("string = ")
    n = len(string) 
    a = list(string) 
    print(permuteStr(a, 0, n-1))
'''
while True:
    N = int(input("N = "))
    R = int(input("R = "))
    print(permute(N, R))