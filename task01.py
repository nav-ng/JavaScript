# str1="7774846y23774789y222"
# palindrome=[]
# l=len(str1)
# for i in range(l-1):
#     for j in range(i+1, l):
#         str2=str1[i:j+1]
#         if str2==str2[::-1]:
#             palindrome.append(str2)
# palindrome=set(palindrome)     
# size=0
# for i in palindrome:
#     if len(i)>size:
#         output=i
#         size=len(output)
# print(output)

sorted_list=[1,2,3,4,5,6,7,8,9,10]
flag=0
size=len(sorted_list)
target=13
left=0
right=size-1
while left<=right:
    mid=(left+right)//2
    if target==sorted_list[mid]:
        flag=1
        break
    elif target<sorted_list[mid]:
        right=mid-1
    else:
        left=mid+1


if flag==1:
    print("Element Found")
else:
    print("Element not Found")
