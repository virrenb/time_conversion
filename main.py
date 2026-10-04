"""
main.py

Driver program for the Time Conversion project.
Prompts the user for a number of seconds and
displays time conversions using the time_conversion module.
"""

# import the module
import project2

# TO DO #1: Declare a variable called num_seconds and assign it a value of 0
num_seconds = 0


def main():

    # statements for output formatting
    print("*******************************")
    print("Start - Time Conversion Program")
    print("*******************************")

    
    # TO DO #2: ask the user to enter the number of seconds to be converted
    # and assign the value to num_seconds as an integer value
    num_seconds = int(input("Enter the number of seconds to convert: "))



    #####################################################
    # you do not need to add anything below this line

    # call function to calculate Decaseconds
    print(project2.decaseconds_conversion(num_seconds))

    # call function to calculate Jiffies
    print(project2.jiffies_conversion(num_seconds))

    # call function to calculate New York Minutes
    print(project2.new_york_minutes_conversion(num_seconds))

    # call function to calculate Nanocenturies
    print(project2.nanocenturies_conversion(num_seconds))

    # call function to calculate Snapchat Streak Days
    print(project2.snapchat_streak_days_conversion(num_seconds))

    # uncomment the function call to calculate custom time
    #print(time_conversion.custom_time_conversion(num_seconds))

    # statements for output formatting
    print("*******************************")
    print("End - Time Conversion Program")
    print("*******************************")


if __name__ == "__main__":
    main()