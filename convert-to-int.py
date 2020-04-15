#####
##Given a string, convert it to an integer
##without using the builtin str function. You are allowed to use ord to convert a character to ASCII code.
#####

def convert_to_int(s):
    validateArray = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
    int_value = 0
    flag = 1
    obtain_String = ""

    for i in s:
        if ord(i) in validateArray:
            obtain_String += i

    l = len(obtain_String)
    for j in obtain_String:
        my_val = ord(j) - 48
        my_val_raise = my_val * (10**(l - flag))
        int_value += my_val_raise
        flag += 1

    if s[0] == "-":
        return int_value*(-1)

    else:
        return int_value

print(convert_to_int("15454") + 1)
