"""
time_conversion.py

This module contains functions that convert a number of seconds
into various non-conventional time units.

Each function accepts an integer number of seconds
and returns the converted value.
"""

def decaseconds_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to decaseconds.
        1 decasecond = 10 seconds.

    Output:
        Return the equivalent number of decaseconds.
    """
    print("Decaseconds: ")
    return seconds / 10
    



def jiffies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to jiffies.
        1 jiffy = 10 milliseconds.

    Output:
        Return the equivalent number of jiffies.
    """
    # 10 milliseconds = 0.01 seconds, so there are 100 jiffies per second
    print("Jiffies: ")
    return seconds * 100


def new_york_minutes_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to New York Minutes.
        1 New York Minute = 1/20 of a second

    Output:
        Return the equivalent number of New York Minutes.
    """
    # 1 NY minute = 1/20 second, so there are 20 NY minutes per second
    print("Time in NY minutes is: ")
    return seconds * 20


def nanocenturies_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Nanocenturies.
         1 Nanocentury = 3.156 seconds

    Output:
        Return the equivalent number of Nanocenturies.
    """
    print("Nanocenturies: ")
    return seconds / 3.156


def snapchat_streak_days_conversion(seconds:float)->float:
    """
    Input:
        seconds (int): A number of seconds.

    Process:
        Convert the number of seconds to Snapchat Streak Days.
        1 Snapchat Streak Day = 24 hours

    Output:
        Return the equivalent number of Snapchat Streak Days.
    """
    # 24 hours * 60 minutes * 60 seconds = 86,400 seconds
    print("Snapchat streak: ")
    return seconds / 86400


def custom_time_conversion(seconds:float)->float:
    """

    Input:
    seconds (int): A number of seconds.

    Process:
    Convert the number of seconds to episodes.
    1 episode = 2700 seconds.

    Output:
    Return the equivalent number of episodes.

    """
    #the idea was to use netflix episodes as a reference, taking that a show has an avg episode length of 45 mins hence, the value is 2700
    print("Time in custom units: ")
    return seconds / 2700
