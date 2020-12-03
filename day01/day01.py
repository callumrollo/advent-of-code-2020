# find the two entries that sum to 2020 and then multiply those two numbers together.

import pandas as pd

# Read in the data with pandas
exp = pd.read_csv('day01_expenses.csv')
ex = exp['expenses']

sltn1 = False
sltn2 = False

# Loop through values in three triple nested loop
# When solution is found, stop calculating
for x in ex:
    for y in ex:
        if not sltn1:
            if x + y == 2020:
                print("solution 1 is " + str(x*y))
                sltn1=True
        if not sltn2:
            for z in ex:
                sum = x + y + z
                if sum ==2020:
                    print("solution 2 is "+str(x*y*z))
                    sltn2=True
    if sltn1 and sltn2:
        break

