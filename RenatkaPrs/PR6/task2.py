nums = list(map(int, input().split()))
result = nums[-2:] + nums[:-2]
print(*result)
