def check(arr):
    count=0
    unsorted=False
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            unsorted=True
            break
        count+=1
    return unsorted,count
def BubbleSort(arr):
    
    unsorted,count=check(arr)
    if unsorted:
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]   
                count+=1    
    return arr,count

def SelectionSort(arr):
    count=0
    for i in range(len(arr)):
        index=i
        for j in range(i+1,len(arr)):
            if arr[index]>arr[j]:
                index=j
            count+=1
        arr[i],arr[index]=arr[index],arr[i]
    return arr,count

def InsertionSort(arr):
    count=0
    for i in range(1,len(arr)):
        val=arr[i]
        j=i-1
        while arr[j]>val and j>=0:
            arr[j+1]=arr[j]
            j-=1
            count+=1
        arr[j+1]=val
    return arr,count

while True:
    # if 1=int(input('enter 1 if you want to do any sorting operation else enter 0:')):
        print('Enter the numbers separated by comma, to sort in ascending order: ')
        arr=list(map(int,input().split(",")))
        print('Bubble sort:1')
        print('Selection sort:2')
        print('Insertion Sort:3')
        print('please enter your choice:')
        choice=int(input())
        if choice==1:
            sorted_arr,count=BubbleSort(arr)
            print('Bubble sort')
            print('sorted array:',sorted_arr)
            print('number of steps:',count)
            print()
        elif choice==2:
            sorted_arr,count=SelectionSort(arr)
            print('Selection sort')
            print('sorted array:',sorted_arr)
            print('number of steps:',count)
            print()
        elif choice==3:
            sorted_arr,count=InsertionSort(arr)
            print('Insertion sort')
            print('sorted array:',sorted_arr)
            print('number of steps:',count)
            print()
    # else:
    #     exit('thank you for visiting this')

