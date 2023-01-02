# This program will accept a numeric value from the keyboard between 0 and 1023.    The binary equivalent will then be returned and ptinted on the screen.
# This program handles a 10 digit binary string.  Below is the order that digits are determined starting with the highest digit.   The entered decimal value 
# is compared to 512 for the hiighest digit and half this value for each subsequent value


result = ""

def determine_binary_from_decimal(decimal_num):
    binary_num = {}
    check_num = 512.0
    iteration = 0

    while check_num >= 1:
        print("Is " + str(decimal_num) + " greater than or equal to "+ str(check_num) + "?")
        if (int(decimal_num) >= check_num):
            binary_num[iteration] = "1"
            decimal_num = int(decimal_num) - check_num
        else:
            binary_num[iteration] = "0"
        check_num = check_num / 2
        iteration += 1
    return binary_num

decimal_num = input("Enter a number between 0 and 1023 and I'll return the binary value:   ")
orig_num = decimal_num
binary_num = determine_binary_from_decimal(decimal_num)
for i in binary_num:
    result = result + (binary_num[i])
print()
print("The binary value of " + orig_num + " is: " + result)
