test = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","tre7buchet"]

f = open("input.txt", "r")

start_digit = 0
end_digit = 0
start_flag = 1
cal_value = "xx"
cal_sum = 0

for line in f:
    for element in line:
        if (element.isdigit()):
            end_digit = element
            if (start_flag == 1):
                start_digit = element
                start_flag = 0

    start_flag = 1
    cal_value = start_digit + end_digit
    cal_sum += int(cal_value)
print(cal_sum)

f.close()