
# Store the functions for writing to and reading from the file of players in a separate module named FileIO.py. 
# Use the csv module for file I/O operations. 

# Handle the exception that occurs if the program can’t find the data file. 
# The read function should return an empty list and the program should not end.

# Use the BaseballPlayers.csv file that is on the assignment page as the source for the lineup. 
# The name of the file will be managed as a constant in the FileIO module.

import csv
import pickle

# The function that reads the file will return the list of players and have no parameters. 
def readCSV():
    # Open CSV file to read data
    try:
        products = []
        with open('BaseballPlayers.csv', 'r', newline="") as file:
            reader_object = csv.reader(file)
            # loop through each row in file and append list to products list
            for row in reader_object:
                products.append(row)
    
        return products

    except FileNotFoundError as e:
        print(type(e), e)
        print("The", 'BaseballPlayers.csv', " file could not be found")
        return None
    except Exception as e:
        print(type(e), e)
        print("This error occured while reading from the CSV file")
        return None
    
# The function that writes to the file will take a lineup list as the only input parameter and will not return anything. 
def writeCSV(player_list):
    # Open CSV file to write list
    with open('BaseballPlayers.csv', 'w', newline="") as file: 
    # Create CSV object and send list to write rows method
        writer_object = csv.writer(file)
        writer_object.writerows(player_list)


