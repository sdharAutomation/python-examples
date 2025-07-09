#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def MajorityElement(nums1):
    count = 0
    candidate = None
    for num in nums1:
        if count == 0:
            candidate = num
        if num == candidate:
            count = count+1
        else:
            count = count-1
    return candidate  

nums1 = [1, 1, 2, 3, 3, 4, 3, 4]
print(MajorityElement(nums1))
