def task1(nums1, nums2):
    nums = set()
    nums.update(nums1, nums2)
    return nums

print(task1({1, 2, 3, 7}, {4, 5, 6}))

