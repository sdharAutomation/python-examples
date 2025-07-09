#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
def RemoveDuplicates(nums1):
    
    i=0
    for j in range(1,len(nums1)):
        if nums1[j] != nums1[i]:
            i=i+1
            nums1[i] = nums1[j]
    return i+1

nums1=[8,8,6,5,5,3,3,2,2]
k = RemoveDuplicates(nums1)
print(k)
print (nums1[:k])
