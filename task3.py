# numbers=list(range(1,5))
# def square_list(k):
#     square=[]
#     for i in k:
#         square.append(i**2)
#     return square
# print(square_list(numbers))


# numbers=[1,2,3,4]
# def reverse_list(numbers):
#     reverse=numbers[::-1]
#      for i in numbers:
# print(reverse_list(numbers))

#  def reverse_list(l):
#       #l.reverse()
#      return l[::-1]
#  numbers=[1,2,3,4]
#  print(reverse_list(numbers))

# def reverse_list(k):
#      number=[]
#      for i in range(1,len(k)+1):
#          poped_item=k.pop()
#          number.append(poped_item)
#      return number
# print(reverse_list(numbers))

#TASK4
word=['abc','def','ghi']
# def reverse_list(k):
#     elements=[]
#     for i in k:
#         elements.append(i[::-1])
#     return elements
# print(reverse_list(word))


# TASK5
# list=[1,2,3,4,5,6,7,8]
# def odd_even(number):
#     even_nums=[]
#     odd_nums=[]
#     for i in number:
#         if i%2==0:
#          even_nums.append(i)
#         else:
#              odd_nums.append(i)
#     output=[odd_nums,even_nums]
#     return output
# print(odd_even(list))



#task6
def common_list(l,k):
    common=[]
    for i in l:
        if i in k:

            common.append(i)
    return common
print(common_list([1,2,3,4],[1,2,3]))
