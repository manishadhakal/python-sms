# numbers=list(range(1,11))
numbers=[1,2,3,4,5,6,7,8,9,10]
# print(numbers.pop())
# print(numbers.index(1,6))
# print(numbers)
def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))

