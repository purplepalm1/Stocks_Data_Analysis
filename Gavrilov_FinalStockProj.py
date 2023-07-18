"""
 Class: CS230--Section 01

 Name: Benjamin Gavrilov

 Description: This program is meant to calculate descriptive stats and provide graphs about certain stocks.

 I have completed this programming assignment independently.

 I have not copied the code from a student or any source.

 I have not shared my code with any student.
"""

import pandas as pd
import statistics
import matplotlib.pyplot as plt

def display_opening(data):
    print("---- Welcome to Stock Pricing and Graphing ----")
    print("Available Companies to Analyze: ")

    #Print company names
    for key, value in data.items():
        print("\t\t\t{}".format(key))

    done = False

    while done == False:
        # take user input and capitalized all the letters
        user_selection = input("Enter the name of a company: ").upper()

        #check if the user selection is in the directory
        for key, value in data.items():
            if user_selection == key.upper():
                done = True
                break

        if done == False:
            print("You typed a wrong company name. Please try again.")

    #return user selection in capital letters
    return user_selection

def calculation_prompt():
    prompt_text = ("Enter type of data to calculate (O for open, H for high, L"
                   "for low, C for close, V for volume) or Q to quit: ")


    valid_letters= ["O", "H", "L", "C", "V", "Q"]

    done = False
    while done == False:
        user_selection = input(prompt_text).upper()

        if user_selection in valid_letters:
            done = True
            break

        if done == False:
            print("You typed a wrong calculation name. Please try again.")

    # return user selection in capital letters
    return user_selection

def descriptive_statictics (data_file_name, calculation):
    #read selected data according to calculation letter
    if calculation == 'O':
        column_name = "Open"

    elif calculation == 'H':
        column_name = "High"

    elif calculation == 'L':
        column_name = "Low"

    elif calculation == 'C':
        column_name = "Close"

    elif calculation == 'V':
        column_name = "Volume"

    df = pd.read_csv(data_file_name)
    saved_column = df[column_name]

    # do calculations for saved_column
    count = int(len(saved_column))
    mean = statistics.mean(saved_column)
    std = statistics.stdev(saved_column)

    #print the results
    print("Descriptive Statistics for " + column_name)
    print("==================================")
    print("Count\t\t{0:.6f}".format(count))
    print("Mean\t\t{0:.6f}".format(mean))
    print("Min\t\t\t{0:.6f}".format(min(saved_column)))
    print("STD\t\t\t{0:.6f}".format(std))
    print("Max\t\t\t{0:.6f}".format(max(saved_column)))
    print("\n")

def graphing_prompt():
    prompt_1 = """\t\t\tGraphing Type and Data Set
    Graph selection:
    \t\t\t1 - Line
    \t\t\t2 - Bar
    """
    prompt_2 ="""Data Seletion:
    \t\t\tH - High
    \t\t\tL - Low
    \t\t\tO - Open
    \t\t\tC - Close
    \t\t\tV - Volume
    """

    print(prompt_1)
    valid_letters= ["1", "2"]

    done = False
    while done == False:
        user_selection_1 = input("\t\t\tEnter your choice: ").upper()
        if user_selection_1 in valid_letters:
            done = True
            break

        if done == False:
            print("You typed a wrong graph selection. Please try again.")

    print(prompt_2)
    valid_letters = ["O", "H", "L", "C", "V"]

    done = False
    while done == False:
        user_selection_2 = input("\t\t\tEnter your choice: ").upper()
        if user_selection_2 in valid_letters:
            done = True
            break

        if done == False:
            print("You typed a wrong graph selection. Please try again.")

    return user_selection_1, user_selection_2

def draw_graph(graph_type, data_file_name, data_set, company_name):
    #Graph Type 1-line, 2-bar

    #read proper data, date and selected column
    if data_set == 'O':
        column_name = "Open"

    elif data_set == 'H':
        column_name = "High"

    elif data_set == 'L':
        column_name = "Low"

    elif data_set == 'C':
        column_name = "Close"

    elif data_set == 'V':
        column_name = "Volume"

    df = pd.read_csv(data_file_name)
    dates = df["Date"]
    opens = df["Open"]
    closes = df["Close"]
    volume = df["Volume"]
    saved_column = df[column_name]

    if graph_type == "1":
        #draw line graph
        plt.plot(dates, saved_column, 'm')
        plt.xlabel('Years: 2000 to Current Day')
        # naming the y axis
        plt.ylabel('Price')

        # giving a title to my graph
        plt.title(column_name + ' Stock Prices of ' + company_name)

        # function to show the plot
        plt.show()

    elif graph_type == "2":
        #draw bar graph
        # draw line graph
        plt.bar(dates, saved_column, )

        plt.xlabel('Years: 2000 to Current Day')
        # naming the y axis
        plt.ylabel('Price')

        # giving a title to my graph
        plt.title(column_name + ' Stock Prices of ' + company_name)

        # function to show the plot
        plt.show()

    #draw open versus Close stock prices
    # draw line graph
    plt.plot(dates, opens, 'co')
    plt.plot(dates, closes, 'yo')

    plt.xlabel('Years: 2000 to Current Day')
    # naming the y axis
    plt.ylabel('Price')

    # giving a title to my graph
    plt.title('Open versus Close Stock Prices of ' + company_name)

    # function to show the plot
    plt.show()

    #draw histogram
    plt.hist(volume)
    # naming the y axis
    plt.style.use('ggplot')
    plt.ylabel('Volume')
    plt.title('Stock Volume of ' + company_name)
    plt.show()

#create a dictionary for companies
companies = {}

# read companies.txt in read only mode
file_read = open("companies.txt", "r")

for line in file_read:
    # read company name and data file name splitting by comma
    company_name = line.split(", ")[0]
    company_data_file = line.split(", ")[1]

    #remove \n from the end of the company_data_file name
    company_data_file = company_data_file.rstrip("\n")

    #write the company infos to dictionary
    companies[company_name] = company_data_file

#close the file
file_read.close()

opening_selection = display_opening(companies)

# read the csv file of the company
for key, value in companies.items():
    if opening_selection == key.upper():
        data_file_name = companies[key]

calculation_selection = calculation_prompt()

while calculation_selection != "Q":
    descriptive_statictics(data_file_name, calculation_selection)
    calculation_selection = calculation_prompt()

graph_type, data_set = graphing_prompt()

draw_graph(graph_type, data_file_name, data_set, opening_selection)

