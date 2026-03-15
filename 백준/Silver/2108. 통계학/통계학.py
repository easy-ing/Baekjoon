import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

# 1. 산술평균
avg = round(sum(nums) / n)
if avg == -0:
    avg = 0

# 2. 중앙값
median = nums[n // 2]

# 3. 최빈값
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1

max_freq = max(count.values())
modes = []

for num, freq in count.items():
    if freq == max_freq:
        modes.append(num)

modes.sort()

if len(modes) > 1:
    mode = modes[1]   # 두 번째로 작은 값
else:
    mode = modes[0]

# 4. 범위
range_value = nums[-1] - nums[0]

print(avg)
print(median)
print(mode)
print(range_value)