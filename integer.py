#!/usr/bin/env python3

# Created By: Luke
# Date: March 25, 2025
# Reads an integer input of a user and determines wether it is negative or positive


def main():
    # asks for int input
    user_int = int(input("Enter an integer: "))
    # checks user int then displays corresponding answer otherwise checks if negative else it is 0
    if user_int > 0:
        print(str(user_int), "is a positive number")
    elif user_int < 0:
        print(str(user_int), "is a negative number")
    else:
        print("Your number is just 0")


if __name__ == "__main__":
    main()
