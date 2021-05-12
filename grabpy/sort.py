def bubble_sort(nums,n):
    for i in range(n):
        flag = False
        for j in range(0,n-i-1):
            if(nums[j]>nums[j+1]):
                flag = True
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
        if not flag:
            break
    return nums


def merge_sort(nums):
    l = len(nums)
    if(l==1):
        return nums
    elif(l==2):
        if(nums[0]<nums[1]):
            return nums
        else:
            return nums[::-1]
    mid = l//2
    left = nums[:mid]
    right = nums[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    i=j=k=0
    llen = len(left)
    rlen = len(right)
    while(True):
        if(i<llen and j<rlen):
            if(left[i]<right[j]):
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        elif(i<llen):
            while(i<llen):
                nums[k]=left[i]
                i+=1
                k+=1
        elif(j<rlen):
            while(j<rlen):
                nums[k]=right[j]
                j+=1
                k+=1
        else:
            break
    return nums

def insertion_sort(nums,n):
    for i in range(1,n):
        j = i
        while(j>0 and nums[j]<nums[j-1]):
            temp = nums[j]
            nums[j]=nums[j-1]
            nums[j-1]=temp
            j-=1

    return nums



def timsort(nums):
    l = len(nums)
    if(l==1):
        return nums
    elif(l==2):
        if(nums[0]<nums[1]):
            return nums
        else:
            return nums[::-1]
    mid = l//2
    left = nums[:mid]
    right = nums[mid:]
    if(l>64):
        left = timsort(left)
        right = timsort(right)
    else:
        left = insertion_sort(left,len(left))
        right = insertion_sort(right,len(right))
    i=j=k=0
    llen = len(left)
    rlen = len(right)
    while(True):
        if(i<llen and j<rlen):
            if(left[i]<right[j]):
                nums[k]=left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        elif(i<llen):
            while(i<llen):
                nums[k]=left[i]
                i+=1
                k+=1
        elif(j<rlen):
            while(j<rlen):
                nums[k]=right[j]
                j+=1
                k+=1
        else:
            break
    return nums

nums = list(map(int,input().split()))
nums = timsort(nums)
print(nums)
