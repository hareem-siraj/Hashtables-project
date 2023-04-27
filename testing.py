from hashskip import Chainedhashtable
import pandas as pd

my_table = Chainedhashtable()

# read the csv file
df = pd.read_csv('sampledata.csv')
#df = pd.read_csv('age_dataset.csv')

    # iterate over each row in the CSV file
for index, row in df.iterrows():
        # add the data to the hashtable
        key = row[3]  # assuming the first column contains the key
        #key = row[6]  # for dataset2
        value = row[1]  # assuming the second column contains the value
        my_table[key] = value#iterate over the data to add it into the hashtable

#print
print(my_table.items())

#search
print(my_table._find_(8))

#discard
my_table.discard(8)
print(my_table.items())

#insert
my_table.__setitem__(0,783)
print(my_table.items())

#my_table.discard(56)       for dataset2
# print(my_table.items())



# H = Chainedhashtable()
# for i in range(10):
#     H.__setitem__(1+i,i*4)
# # H.__setitem__(33,783)
# # print(H.items())
# # H.discard(33)
# print(H.items())
# H.discard(8)
# print(H._find_(3))
# print(H.items())
# H.clear()
# print(H.items())