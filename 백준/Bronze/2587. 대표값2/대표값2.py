import sys

nums = [int(sys.stdin.readline()) for _ in range(5)]

avg = sum(nums) // 5
median = sorted(nums)[2]

print(avg)
print(median)