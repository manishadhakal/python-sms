
# def fun1(n):
#     for i in range(1,n+1):
#         yield(i)
#
# number=(fun1(10))
# print(number)
# for num in number:
#     print(num)
# for num in number:
#     print(num)
#
# l=[1,2,3,4]
# # num1=[a**2  for a in l]
# num1=list((a**2  for a in l))
#
# print(num1)

def odd_even(n):
    for i in range(1,n+1):
        if i%2==0:
            # yield (i)
            yield(i**2)

odd_even(10)
for i in odd_even(10):
    print(i)