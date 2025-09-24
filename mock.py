def get_num():
# program to get number
    return int(input("Enter a number: "))
def odd_even(num):
# program to check if number is even or odd
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"
def sign(num):
# program to check if number is positive or negative
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
def square(num):
# program to find square of number
    return num**2
def cube(num):
# program to find cube of number
    return num**3
def main():
    number = get_num()
    print(odd_even(number))
    print(sign(number))
    print(square(number))
    print(cube(number))
main()