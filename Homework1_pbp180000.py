# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 12:24:33 2022

@author: Prachi
"""
import sys
import pathlib 
import re
import pickle

class Person:
    
    def __init__(self, last, first, mi, id, phone):
        #initiate employee information
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone
        
    
    def display(self):
        #displaying employee information
        print("Employee id : " + self.id)
        print("\t" + self.first + " " + self.mi + " " + self.last)
        print("\t" + self.phone)
        




def getfile(filepath):
    #get the file data from csv file
    with open(pathlib.Path.cwd().joinpath(filepath), 'r') as f:
        text = f.read()
    return text

def process(file):
    
    #split the file into multiple rows and remove very first row as it is just the header
    file = file.split("\n")
    file = file[1:]
    
    #split each row by the commas 
    for x in range(0,5):
        file[x] = file[x].split(",")
       
    #create empty dictionary
    dictionPerson = {}
    
    #iterate over each row and Capitalize the Last and First names
    for x in range(0,5):
        file[x][0] = file[x][0].capitalize()
        file[x][1] = file[x][1].capitalize()
        
        #if the middle initial is empty change it to X otherwise capitalize the middle initial
        if file[x][2] == "":
            file[x][2] = "X"
        else:
            file[x][2] = file[x][2].capitalize()
            
        #match the id to the format required with two letters followed by four digits.
        # if id is not in required format ask user to input it again
        while re.search(r"[A-za-z]{2}[0-9]{4}$", file[x][3]) == None:
            inp = input("ID invalid: " + file[x][3] + "\n" +
                        "ID is two letters followed by 4 digits" + "\n" +
                        "Please enter a valid id:")
            file[x][3] = inp
            
        # match phone number to required format and if not in format then ask user to input
        #phone number in correct format
        while re.search(r"^[1-9]\d{2}-\d{3}-\d{4}", file[x][4]) == None:
            inp = input("Phone " + file[x][4] + " is invalid \n" +
                        "Enter phone number in form 123-456-7890" + "\n" +
                        "Enter phone number:")
            file[x][4] = inp
        
        #create Person variable with employee information
        pers = Person(file[x][0], file[x][1], file[x][2], file[x][3], file[x][4])
        
        #ensure that employee id key is not already in dictionary and as long as its not a duplicate
        #add the employee into the Person dictionary
        if file[x][3] in dictionPerson:
            print("ID already in dictionary")
        else:
            dictionPerson[file[x][3]] = pers
    return dictionPerson
                
                
if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('Please input a filename as a system arg')
    else:
        fp = sys.argv[1]
        file = getfile(fp)
        people = process(file)
        
        # save dictionary to pickle file
        pickle.dump(people, open('people.p', 'wb'))
        
        #open pickle file and convert back to dictionary
        peopleLoad = pickle.load(open('people.p', 'rb'))
        
        #print employee list
        print("Employee List:")
        
        for people in peopleLoad.values():
            people.display()