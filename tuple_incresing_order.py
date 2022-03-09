# Write a Python program to get a list, sorted in increasing order by the last element in each 
# tuple from a given list of non-empty tuples
#  Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# sample_list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# i=0
# while i<len(sample_list):
#    j=0
#    while j<len(sample_list)-1:
#       if sample_list[j][1]>sample_list[j+1][1]:
#          t=sample_list[j]
#          sample_list[j]=sample_list[j+1]
#          sample_list[j+1]=t
#       j+=1
#    i+=1
# print(sample_list)


# a=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# i=0
# while i<len(a):
#    j=0
#    while j<len(a)-1:
#       if a[j][1]>a[j+1][1]:
#          t=a[j]
#          a[j]=a[j+1]
#          a[j+1]=t
#       j+=1
#    i+=1
# print(a)
      
         