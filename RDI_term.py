# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel("RDI-6.xlsx")
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=["Standardised"])
# take the data in a an array
data = data.values
#remove the nan values
data = data[~pd.isnull(data)]
# remove zero values
data = data[data != 0]
print("The array is:\n", data)
near_28 = data[:28*12-2]
middle_28 = data[28*12-2:56*12-2]
far_29 = data[56*12-2:]
print("The first 28 years are:\n", len(near_28))
# print("The second 28 years are:\n", middle_28)
# print("The last 28 years are:\n", far_29)
# find at least three consecutive negative values
short_near=0
middle_near=0
long_near=0

short_middle=0
middle_middle=0
long_middle=0

short_far=0
middle_far=0
long_far=0
neg_list = []
for i in range(len(near_28)):
    if near_28[i] > 0:
        if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_near += 1
        elif len(neg_list) <= 6 and len(neg_list) >= 4:
            middle_near += 1
        elif len(neg_list) >= 7:
            long_near += 1
        neg_list = []
    else:
        neg_list.append(near_28[i])

if len(neg_list) >= 2:
    # find the lowest negative value in the list
    if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_near += 1
    elif len(neg_list) <= 6 and len(neg_list) >= 4:
        middle_near += 1
    elif len(neg_list) >= 7:
        long_near += 1

print("The number of short of near_28 is: ", short_near)
print("The number of middle of near_28 is: ", middle_near)
print("The number of long of near_28 is: ", long_near)

neg_list = []
for i in range(len(middle_28)):
    if middle_28[i] > 0:
        if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_middle += 1
        elif len(neg_list) <= 6 and len(neg_list) >= 4:
            middle_middle += 1
        elif len(neg_list) >= 7:
            long_middle += 1
        neg_list = []
    else:
        neg_list.append(middle_28[i])

if len(neg_list) >= 2:
    # find the lowest negative value in the list
    if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_middle += 1
    elif len(neg_list) <= 6 and len(neg_list) >= 4:
        middle_middle += 1
    elif len(neg_list) >= 7:
        long_middle += 1

print("The number of short of middle_28 is: ", short_middle)
print("The number of middle of middle_28 is: ", middle_middle)
print("The number of long of middle_28 is: ", long_middle)


neg_list = []
for i in range(len(far_29)):
    if far_29[i] > 0:
        if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_far += 1
        elif len(neg_list) <= 6 and len(neg_list) >= 4:
            middle_far += 1
        elif len(neg_list) >= 7:
            long_far += 1
        neg_list = []
    else:
        neg_list.append(far_29[i])

if len(neg_list) >= 2:
    # find the lowest negative value in the list
    if len(neg_list) <= 3 and len(neg_list) >= 2:
            short_far += 1
    elif len(neg_list) <= 6 and len(neg_list) >= 4:
        middle_far += 1
    elif len(neg_list) >= 7:
        long_far += 1

print("The number of short of far_29 is: ", short_far)
print("The number of middle of far_29 is: ", middle_far)
print("The number of long of far_29 is: ", long_far)



