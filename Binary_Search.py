def binarysearch(mylist,search_element,start,end):
    if end>=start:
        mid=(start+end)//2
        if mylist[mid]==search_element:
            return mid
        elif mylist[mid]>search_element:
            return binarysearch(mylist,search_element,start,mid-1)
        elif mylist[mid]<search_element:
            return binarysearch(mylist,search_element,mid+1,end)
    else:
        return -1
mylist=[6,3,4,10,9,16,7]
mylist.sort()
print(mylist)
search_element=int(input("Enter the element toi search:\n"))
result=binarysearch(mylist,search_element,0,len(mylist)-1)
if result!=-1:
    print("Element found at", str(result+1))
else:
    print("Element not found")