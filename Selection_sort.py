def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
    print('Sorted Array:\n',lst)
lst=[20,12,10,15,2]
print('Unsorted list:\n',lst)
selection_sort(lst)