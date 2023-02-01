nums = input("enter a few number: ").split(" ")
maxNum = nums[0]
for num in nums:
    if maxNum < num:
        maxNum = num
print(maxNum)