# test
nums = [16, 17, 4, 23, 8, 15, 42, 1, 2]
target = 19
hash = {}
success = False

for index, num in enumerate(nums):
    print((index, num))
    complement = target - num
    if complement in hash:
        print("Solution found!")
        print(f"[{index}, {num}]")
        print([hash[complement], index])
        success = True
        break
    else:
        # Add the number to the hash
        hash[num] = index

if not success:
    print("No solution found")
