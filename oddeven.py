number = int(input())

val = number%2

string = val*"ODD" + abs(val-1)*"EVEN"

print(f"The number is {string}")
