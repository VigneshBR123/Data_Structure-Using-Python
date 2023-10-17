def insertion_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while lst[j]<lst[j-1] and j>0:
            temp = lst[j]
            lst[j]=lst[j-1]
            lst[j-1]=temp
            j-=1
    print('Sorted list:',lst)
lst=[3,4,2,1]
print('Unsorted list:',lst)
insertion_sort(lst)