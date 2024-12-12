
nums = list(map(int, input("Enter a list of numbers: ").split()))
target = int(input("Enter a target: "))

numMap = {}
n = len(nums)

for i in range(n):
   complement = target - nums[i]
   if complement in numMap:
      print([numMap[complement], i])
   numMap[nums[i]] = i


