# Take 20 integer inputs from user and print the following:
# number of positive numbers
# number of negative numbers
# number of odd numbers
# number of even numbers
# number of 0s.

i=0
list=[]
while i<5:
   num=int(input("enter the element"))
   list.append(num)
   i+=1
x=0
]po      
negative=0
positive=0
zero=0
even=0
odd=0
while x<len(list):
   if list[x]==0:
      zero+=1
   elif list[x]>0:
      positive+=1
      if list[x]%2==0:
         even+=1
      else:
         odd+=1
   else:
      negative+=1
      if list[x]%2==0:
         even+=1
      else:
         odd+=1
   x+=1
print("zero:",zero,"positive:",positive,"negative:",negative,"even:",even,"odd:",odd)

##Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order

# i=0
# list1=[]
# while i<10:
#    num=int(input("enter  the element"))
#    list1.append(num)
#    i+=1
# print(list1)
# list2=list1.copy()
# list2.reverse()
# print(list2)


# i=0
# list=[]
# num=int(input("enter the number of element:"))
# while i<num:
#    ele=int(input("enter the element"))
#    if ele%2==0:
#       list.append(ele)
#    i+=1
# print(list)
