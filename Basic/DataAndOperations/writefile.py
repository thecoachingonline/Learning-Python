#!/usr/bin/env python3

# create and open file
f = open("test.txt","w")

# write data to file 
f.write("Hello World, \n")
f.write("This data will be written to the file.")

# close file
f.close()

# create and open file
f = open("test.txt","a")

# write data to file 
f.write("Don't delete existing data \n")
f.write("Add this to the existing file.")

# close file
f.close()