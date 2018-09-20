"""
LottoAnalysis: Generates random lottery draws and provides
basic analysis on the resulting numbers.
"""

import random
from pprint import pprint

__author__ = "David Bristoll"

def randomDraw():
    """
    Returns 7 random numbers from a set of 1 to 52 (inclusive)
    """
    draw = []
    draw = random.sample(range(1,53),7)
    return draw

def isNumber(s):
    """
    Tests if the value passed is a number.
    Returns True or False.
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def runApp():
    """
    Runs the app
    """
    while True:
        draws = []
        numberOfDraws = 0
        displayDraws = False
        display = ""
        while numberOfDraws == 0:
            print("Please enter the number of draws required.")
            enteredNumber = input()
            if isNumber(enteredNumber):
                numberOfDraws = int(enteredNumber)

        while display.lower() != "y" and display.lower() != "n":
            print("\nWould you like to see the draws? (This is slower, especialy where there are thousands of draws)\n")
            print("\nPlease enter y or n\n")
            display = input()
        if display.lower() == "y":
            displayDraws = True
        for i in range(numberOfDraws):
            draws.append(randomDraw())
        if displayDraws:
            pprint(draws)

        print("\nPress enter to run analysis\n")
        input()
        analysisMenu(draws)



def analysisMenu(draws):
    """
    Takes the current list of draws and gives analysis options.
    Passes the list of draws to the relevant function to return the
    appropriate data.
    """
    leaveMenu = False
    analysisOptions = {"1) Range scan": [1, rangeScan]}
    print("\nPlease select one of the following optons:\n")
    print("0) Exit")
    for option in analysisOptions:
        print(option)
    while leaveMenu == False:
        selection = input()
        if isNumber(selection):
            for option in analysisOptions:
                if int(selection) == 0:
                    leaveMenu = True
                    break
                if int(selection) == analysisOptions[option][0]:
                    leaveMenu = True
                    analysisOptions[option][1](draws)

def rangeScan(draws):
    """
    Takes the list of draws and displays a break down of the ranges of 
    numbers that have been selected.
    """
    
    ranges = {"range1to13": 0,
              "range14to26": 0,
              "range27to39": 0,
              "range40to52": 0,
              "range1to26": 0,
              "range27to52": 0,
              "range1to13PC": 0,
              "range14to26PC": 0,
              "range27to39PC": 0,
              "range40to52PC": 0,
              "range1to26PC": 0,
              "range27to52PC": 0,
              }

    
    numberOfNumbers = 0
    
    for draw in draws:
        for number in draw:
            numberOfNumbers += 1
            if number < 14:
                ranges["range1to13"] += 1
            elif number >= 14 and number < 27:
                ranges["range14to26"] += 1
            elif number >= 27 and number < 40:
                ranges["range27to39"]+= 1
            elif number > 39:
                ranges["range40to52"] += 1

            if number < 27:
                ranges["range1to26"] += 1
            else:
                ranges["range27to52"] += 1

    # Quarter ranges
    ranges["range1to13PC"] = round((ranges["range1to13"] / numberOfNumbers) * 100, 2)
    ranges["range14to26PC"] = round((ranges["range14to26"] / numberOfNumbers) * 100, 2)
    ranges["range27to39PC"] = round((ranges["range27to39"] / numberOfNumbers) * 100, 2)
    ranges["range40to52PC"] = round((ranges["range40to52"] / numberOfNumbers) * 100, 2)

    # Half ranges
    ranges["range1to26PC"] = round((ranges["range1to26"] / numberOfNumbers) * 100, 2)
    ranges["range27to52PC"] = round((ranges["range27to52"] / numberOfNumbers) * 100, 2)

    # Display breakdown
    print("\nStatistical breakdown of drawn number ranges\n")
    print("Total number of balls from 1 to 13: ", str(ranges["range1to13"]),
          "as a percentage of numbers drawn: ", str(ranges["range1to13PC"]))
    print("\nTotal number of balls from 14 to 26: ", str(ranges["range14to26"]),
          "as a percentage of numbers drawn: ", str(ranges["range14to26PC"]))
    print("\nTotal number of balls from 27 to 39: ", str(ranges["range27to39"]),
          "as a percentage of numbers drawn: ", str(ranges["range27to39PC"]))
    print("\nTotal number of balls from 40 to 52: ", str(ranges["range40to52"]),
          "as a percentage of numbers drawn: ", str(ranges["range40to52PC"]))

    print("\nTotal number of balls from 1 to 26: ", str(ranges["range1to26"]),
          "as a percentage of numbers drawn: ", str(ranges["range1to26PC"]))
    print("\nTotal number of balls from 27 to 52: ", str(ranges["range27to52"]),
          "as a percentage of numbers drawn: ", str(ranges["range27to52PC"]))

    print("Press enter to continue.")

    input()

    return

# Run the app
runApp()
