# def f_loop(start, end):
#     if start != end:
#         print(start)
#         f_loop(start+1, end)

# def fakt(n):
    
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return(n*fakt(n-1))

# def fib(n):
    
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))

# for i in range(5):
#     print(fib(i), end= ' ')

def pangkat(bil,pang):
    if pang == 0:
        return 1
    else:
        return (bil*pangkat(bil,pang-1))

print(pangkat(2,3))