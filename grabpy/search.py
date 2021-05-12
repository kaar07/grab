def linear_search(arr,target,n):
    linearIndex = -1
    i=0
    while(i<n):
        if(arr[i] == target):
            linearIndex == i
            break
        i+=1
    return linearIndex

def binary_search(arr,target,start,end):
    binIndex = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid] == target):
            binIndex = mid
            break
        elif(arr[mid]<target):
            start = mid + 1
        else:
            end = mid -1

    return binIndex

def strictly_greatest_than(arr,target,start,end):
    sgbinIndex = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]<=target):
            start = mid + 1
        else:
            sgbinIndex = mid
            end = mid - 1
    return sgbinIndex

def strictly_less_than(arr,target,start,end):
    slbinIndex = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid]>=target):
            end = mid -1
        else:
            slbinIndex = mid
            start = mid + 1
    return slbinIndex

def less_than_equal(arr,target,start,end):
    ltebinIndex = -1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid] == target):
            ltebinIndex = mid
            break
        elif(arr[mid]>target):
            end = mid -1
        else:
            ltebinIndex = mid
            start = mid + 1
    return ltebinIndex

def greater_than_equal(arr,target,start,end):
    gtebinIndex = -1
    while(start<=end):
        mid = (start + end)//2
        if(arr[mid] == target):
            gtebinIndex = mid
            break
        elif(arr[mid]<target):
            start = mid +1
        else:
            gtebinIndex = mid
            end = mid -1
    return gtebinIndex


#  arr = [2,4,6,8,10,11,12]
#  print(arr)
#  for i in range(10):
    #  t = int(input("Search for: "))
    #  print("greater than equal: ",greater_than_equal(arr,t,0,6))
    #  print("less than or equal: ",less_than_equal(arr,t,0,6))
