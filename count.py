import re

sum = 0
actual_data = open('actual_data.txt')
for line in actual_data:
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            sum += int(number)

print(sum)
