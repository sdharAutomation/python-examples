#Print Max and Min number in an Array
def MaxMinNumberInArray(nums1):
    max=nums1[0]
    min=nums1[0]
    for num in nums1:
        if num > max:
            max = num
        if num < min:
            min = num
    return max,min

nums1=[1,2,4,5,3,6,9,5]
print(MaxMinNumberInArray(nums1))