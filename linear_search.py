mylist=[3,7,4,9,6]
search_element=int(input("Enter the element to search:\n"))
a=0
for i in range(len(mylist)):
    if mylist[i]==search_element:
        a=1
        print(f"Element at {i+1} position")
        break
if a==0:
    print("Element not found")