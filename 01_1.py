import sys

calibration_values = []
total = 0
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    x1 = next(filter(lambda x: x.isdigit(), line))
    x2 = next(filter(lambda x: x.isdigit(), reversed(line)))
    total += int(x1+x2)
print(total)
