def longestMountain(arr):
    mx=0
    j=1
    n=len(arr)
    while j<n-1:
        if arr[j-1]< arr[j]>arr[j+1]:
            left=j-1
            right=j+1
            while left>0 and arr[left-1]<arr[left]:
                left-=1
            while right<n-1 and arr[right+1]<arr[right]:
                right+=1
            mx=max(mx,right-left+1)
            j=right
        else:
            j+=1
    return mx

arr=[2,1,4,7,3,2,5]
print(longestMountain(arr))