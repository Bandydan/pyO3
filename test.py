alskjdvalskjdbv
dlkfjnvlskdjnvalskdjnv
lkjvbasjdvaskbv
import sys

numbers = []

with open(sys.argv[1], "r") as f:
    items = f.read().split("\n")
    for i in items[:-1]:
        numbers.append([int(n) for n in i.split(",")])
for nums in numbers:
    print("\n")
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            print("FB", end = " ")
        elif num % nums[0] == 0:
            print("F", end = " ")
        elif num % nums[1] == 0:
            print("B", end = " ")
        else:
            print(num, end = " ")
with open(sys.argv[2], "w") as file:
 for elem in nums:
    file.write(' '.join(map(str, nums)))
