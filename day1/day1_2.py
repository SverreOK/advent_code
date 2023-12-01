import re

f = open("input.txt", "r")

cal_num = 0

string_2_digit_map = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

for line in f:
    digit_list = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
    cal_num += string_2_digit_map[digit_list[0]]*10 + string_2_digit_map[digit_list[-1]]

print(cal_num)
print(digit_list)