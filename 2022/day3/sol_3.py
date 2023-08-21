points_d = {}
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = [n for n in range(1, 53)]

sum_ = 0

for tup in zip(letters, nums):
    points_d[tup[0]] = tup[1]
count = 0
with open("day3/input.txt", 'r') as f:

    lines = f.readlines()

    for line in lines:
        line = line.strip()
        if count == 0:
            first = set(line)
            print(count)
            count += 1 
        elif count == 1:
            second = set(line)
            print(count)
            count += 1 
        elif count == 2:
            third = set(line)
            letter = list(first.intersection(second, third))[0]
            sum_ += points_d[letter]
            count = 0
            
"""
    for line in lines:
        line = line.strip()

        length = len(line)
        half = length // 2

        first = set(line[:half])
        second = set(line[half:])
        print(first, second)
        letter = list(first.intersection(second))[0]
            
        sum_ += points_d[letter]
"""
print(sum_)
        