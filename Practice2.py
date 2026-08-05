nums = [2,4,6,8]
result = []
for n in nums:
    if n % 4 == 0:
        result.append(n // 2)
    else:
        result.append(n + 2)

        print(result)