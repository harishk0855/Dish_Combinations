from itertools import combinations
import re
import csv
import sys
import os
import math


# Variables
flag = 0
target_amt = 0
data_dict={}
temp_lt =[]

def dish_names(lt, data_dict):
    """
    This function will print items with names and cost
    lt : list of combination of dish
    data_dict : dictionary which is formed from csv file
    """
    for element in lt:
        for key, val in data_dict.items():
            if val == element:
                print(key +" : "+str(val))

    print("-" * 25)


# Validate csv file passed
try:
    if os.path.isfile(sys.argv[1]) and str(sys.argv[1]).endswith('csv'):
        print(sys.argv[1])
        flag = True
    else:
        print("\n%s is not a valid file Path\n" % sys.argv[1])
        flag = False
except:
    print("""\nPlease pass the input file name path as Argument
              \nUsage\t--help\n%s  <input file path>
          """ % sys.argv[0])
    flag = False

if flag:
    # open and read csv file
    with open(sys.argv[1], 'r') as datafile:
        csv_reader = csv.reader(datafile)
        for row in csv_reader:
            row_st = ''.join(row[0:2])
            #read target price
            if re.match('Target', row_st):
                target_amt = row[1]
                target_amt = round(float(target_amt.replace('$','').strip()),2)
                print("\nTarget Price : $%f" % target_amt)

            # read all the values
            elif row[0] and row[1]:
                data_dict[row[0].strip()] = round(float(row[1].replace('$','').strip()),2)
                temp_lt.append(data_dict[row[0].strip()])

    #iterate all the combinations and find which one is having the sum value equal to target price.
    ft = [val for i in range(1,len(temp_lt)) for val in combinations(temp_lt,i) if round(sum(val),2) == target_amt]
    if ft:
        for lt in ft:
            print("\nPossible cominations is/are : "+ str(len(ft))+"\n"+'-'*25)
            dish_names(lt, data_dict) #print all the combinations
    else:
        print("There is no combination of dishes that is equal to the target price")

else:
    print("calling exit()")
    exit()
