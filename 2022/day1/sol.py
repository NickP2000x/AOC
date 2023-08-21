
l = []
sum_ = 0
with open("/Users/n/Desktop/advent/day1/input.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line.strip()
        if len(line) != 1:
            sum_ += int(line)
        else:
            l.append(sum_)
            sum_ = 0
import numpy as np
first = max(l)
l.remove(max(l))
second = max(l)
l.remove(max(l))
third = max(l)
sum_ = first + second + third
print(sum_)