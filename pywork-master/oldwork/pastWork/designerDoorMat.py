# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
nums = list(map(int, input().split()))
g = ".|."
for i in range(nums[0]//2):
    print((".|." * ((i * 2) + 1)).center(nums[1], "-"))
print("WELCOME".center(nums[1], "-"))
for i in reversed(range(nums[0]//2)):
    print((".|." * ((i * 2) + 1)).center(nums[1], "-"))
