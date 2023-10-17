def bubble_sort(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
    print('Sorted list using bubble sort is:\n', lst)
lst=[5,67,82,2,45,105,101,7]
print('Unsorted list:\n',lst)
bubble_sort(lst)