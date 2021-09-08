# Random numbers:
# Writing the files:

import numpy as np

# File to be read from
file1 = open("trainingdata.txt", "r")

# Files to be written
file2 = open("crosstrainingdata1.txt", "a")
file3 = open("crosstrainingdata2.txt", "a")
file4 = open("crosstrainingdata3.txt", "a")
file5 = open("crosstrainingdata4.txt", "a")
file6 = open("crosstrainingdata5.txt", "a")
file7 = open("crosstrainingdata6.txt", "a")
file8 = open("crosstrainingdata7.txt", "a")
file9 = open("crosstrainingdata8.txt", "a")

# Creation of random numbers in the file so we can write different lines
# Missing two files every time it runs
limitsarray = [file2, file3, file4, file5, file6, file7, file8, file9]
limit = np.random.randint(18506, size=18506)
iterator = 0
index = 0
lastindex = 0
readlines = file1.readlines()
for limits in limit:
    if (iterator % 2313 == 0 and iterator != 0):
        index += 1
    limitsarray[index].write(readlines[limits])
    iterator += 1


# print(np.random.randint(18506, size=18506))

# Closing the files
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
file8.close()
file9.close()
