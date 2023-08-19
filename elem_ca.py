# 10-08-2023 Working as of today. 
# Author: Preethi Ann Jacob
# Python implementation of elementary Cellular Automata. All the cells in a generation use the same ruleset. Output for all 0-255 rules is stored in separate text files.

# Function to delete all files in a directory
# Note: Folders within are safe. If you want to save old outputs, keep them in a folder within "output/"
def delete_files_in_directory(directory_path):
   import os
   try:
     with os.scandir(directory_path) as entries:
       for entry in entries:
         if entry.is_file():
            os.unlink(entry.path)
     # print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")

# Function to convert decimal integer to binary number in list
# e.g. binary(30)=[0,0,0,1,1,1,1,0]
def binary(dec):
    bin=[0]*8
    binindex=7
    while(dec>0):
        bin[binindex]=dec%2
        dec=dec//2
        binindex-=1
    return bin

# Print a single generation of Cellular Automata to corresponding output file
# e.g. Save output for printCA(ca,30) in "output/Rule30.txt" file
def printCA(ca,dec):
    filename='output/Rule'+str(dec)+'.txt'
    with open(filename, 'a') as f:                      # a= append file mode. Create file if not present
        for element in ca:
            if element==1:  f.write("*")
            else:           f.write("_")
        f.write("\n")
 
# Delete all old outputs
directory_path = 'output'
delete_files_in_directory(directory_path)

for dec in range(256):                                  # Since for neighbourhood 2^8=256 combinations are possible
    ruleset=binary(dec)
    # print("RuleSet",dec,"=",ruleset)

    noOfCells=200                                       # No of cells in one generation
    noOfGenerations=100                                 # No of generations

    # Initializing CA such that almost all except the middle element is zero
    ca=[0 for i in range(noOfCells)]
    ca[noOfCells//2]=1
    printCA(ca,dec)

    # Making new generation of CA wrt neighbourhood of each cell
    gen=1;
    while(gen<=noOfGenerations):
        nextGen=[0 for i in range(noOfCells)]
        for i in range (1,noOfCells-1):                 # Excluding the first and last cell to avoid border doubts
            neighbourhood = (ca[i-1],ca[i],ca[i+1])
            if   (neighbourhood==(0,0,0)):  nextGen[i]=ruleset[7]
            elif (neighbourhood==(0,0,1)):  nextGen[i]=ruleset[6]
            elif (neighbourhood==(0,1,0)):  nextGen[i]=ruleset[5]
            elif (neighbourhood==(0,1,1)):  nextGen[i]=ruleset[4]
            elif (neighbourhood==(1,0,0)):  nextGen[i]=ruleset[3]
            elif (neighbourhood==(1,0,1)):  nextGen[i]=ruleset[2]
            elif (neighbourhood==(1,1,0)):  nextGen[i]=ruleset[1]
            elif (neighbourhood==(1,1,1)):  nextGen[i]=ruleset[0]
        ca=nextGen[:]
        printCA(ca,dec)
        gen+=1
    print("CA for rule ",dec,"is ready in the output folder")
print("Thank you for waiting. CA for all the 256 rules are available in the output folder")
