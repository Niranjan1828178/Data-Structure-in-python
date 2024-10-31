# def check(arr):
#     count=0
#     unsorted=False
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             unsorted=True
#             break
#         count+=1
#     return unsorted,count
def BubbleSort(arr):
    count=0
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
        count+=1
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
        count+=1
    return arr,count

# def partition(arr,LB,UB,count):
#     pivot=arr[LB]
#     start=LB
#     end=UB
#     while True:
#         while start<=end and arr[start]<=pivot:
#             print('start:',start)
#             start+=1
#             count+=1
#         while start<=end and arr[end]>pivot:
#             print('end:',end)
#             end-=1
#             count+=1
#         if start<end:
#             arr[start],arr[end]=arr[end],arr[start]
#         else:
#             break
#     arr[LB],arr[end]=arr[end],arr[LB]
#     return end,count

# def QuickSort(arr,count=0):
#     if len(arr)>0:
#         pind,count=partition(arr,0,len(arr)-1,count)
#         print('inq',arr)
#         QuickSort(arr[:pind],count)
#         QuickSort(arr[pind+1:],count)
#     return count
    
def CountingSort(arr):
    count=max(arr)
    count_arr=[0 for i in range(max(arr)+1)]
    while arr!=[]:
        count_arr[arr[0]]+=1
        count+=1
        arr=arr[1:]
    for i in range(len(count_arr)):
        while count_arr[i]>0:
            arr.append(i)
            count_arr[i]-=1
    return arr,count
def Merge(arr,L,mid,R):
    Larr=[arr[i] for i in range(L,mid+1)]
    Rarr=[arr[i] for i in range(mid+1,R+1)]
    i,j,k=0,0,L
    count=0
    while i<len(Larr) and j<len(Rarr):
            if Larr[i]<Rarr[j]:
                arr[k]=Larr[i]
                i+=1
                k+=1
            else:
                arr[k]=Rarr[j]
                j+=1
                k+=1
            count+=1
    while i<len(Larr):
        arr[k]=Larr[i]
        i+=1
        k+=1
    while j<len(Rarr):
        arr[k]=Rarr[j]
        j+=1
        k+=1
    return count
    
def MergeSort(arr,L=0,R=None):
    if R==None:
        R=len(arr)-1
    count=0
    if L<R:
        mid=(L+R)//2
        count+=MergeSort(arr,L,mid)
        count+=MergeSort(arr,mid+1,R)
        count+=Merge(arr,L,mid,R)
    return count


while True:
        print('Enter 0 to exit:')
        print('Bubble sort:1')
        print('Selection sort:2')
        print('Insertion Sort:3')
        # print('Quick sort:4')
        print('Counting Sort:5')
        print('Merge Sort:6')
        print('please enter your choice:')
        choice=input()
        if choice=='0':
            exit('Thank You!')
        else:
            print('Enter the numbers separated by comma, to sort in ascending order: ')
            arr=list(map(int,input().split(",")))
            if choice=='1':
                sorted_arr,count=BubbleSort(arr)
                print('Bubble sort')
                print('sorted array:',sorted_arr)
                print('number of steps:',count)
                print()
            elif choice=='2':
                sorted_arr,count=SelectionSort(arr)
                print('Selection sort')
                print('sorted array:',sorted_arr)
                print('number of steps:',count)
                print()
            elif choice=='3':
                sorted_arr,count=InsertionSort(arr)
                print('Insertion sort')
                print('sorted array:',sorted_arr)
                print('number of steps:',count)
                print()
            # elif choice=='4':
            #     count=QuickSort(arr)
            #     print('Quick sort')
            #     print('sorted array:',arr)
            #     print('number of steps:',count)
            #     print()
            elif choice=='5':
                sorted_arr,count=CountingSort(arr)
                print('Counting sort')
                print('sorted array:',sorted_arr)
                print('number of steps:',count)
                print()
            elif choice=='6':
                count=MergeSort(arr)
                print('Merge sort')
                print('sorted array:',arr)
                print('number of steps: ',count)
                print()
            else:
                print('Invalid choice!, please try again\n')
