#!/usr/bin/env python3

# Created by: Seti Ngabo
# Created on: Sept 2021
# This program tells you if you can date my grandchild


def main():
    # this function checks if you qualify to date my granddaughter

    # input
    user_wealth = input("Are you rich?(yes or no): ")
    user_looking = input("Are you good looking(yes or no): ")
    print("")

    # process and output
    if user_wealth == "yes" and user_looking == "yes":
        print("You are accepted to date my grandchild.")
        print("")
    elif user_wealth == "no" or user_looking == "no":
        print("Not accepted, come back when you get rich.")
        print("")
    else:
        print("Invalid input, try again.")
        print("")

    print("Thanks for checking.")

    print("\nDone.")


if __name__ == "__main__":
    main()
