#Remove element val 2 from a list of array nums1 [1,3,2,4,5,2,7]

def RemoveElement(val,nums1):
    #loop through the list check if it matches the val dont add it move to next value, return new length of array and modified array
    i=0
    k=0
    for i in range(len(nums1)-1):
        if nums1[i] != val:
            nums1[k] = nums1[i]
            k = k+1
    return k
val = 2
nums1 = [1,3,2,4,5,2,7]
k = RemoveElement(val,nums1)
print("New length:", k)
print("Modified Array:",nums1[:k])
