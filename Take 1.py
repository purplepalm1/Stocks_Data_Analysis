import pandas as pd
import statistics
import matplotlib.pyplot as plt

def display_opening(data):
    print("---- Welcome to Stock Pricing and Graphing ----")
    print("Available Companies to Analyze: ")

    #Print company names
    for key, value in data.items():
        print("\t\t\t{}".format(key))

    while done == False:
        # take user input and capitalized all the letters
        user_selection = input("Enter the name of a company: ").upper()

        #check if the user selection is in the directory
        for key, value in data.items():
            if user_selection == key.upper():
                done = True
                break
