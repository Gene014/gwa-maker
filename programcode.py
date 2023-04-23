# Calma, Eugene Marie S.
# BSCPE_1-4
# OOP Laboratory Exercise Number 3 Problem 2 (GWA-MAKER)

#Write a Python program that read a file containing the name of 20 students together with their GWA. 
#The program will outputs the name of the student who got the highest GWA (including the GWA).

def process():
    #set variables for max gwa and for the uname
    max_gwa=1
    max_name=""
    #open gwa.txt (read)
    with open("gwa.txt","r") as input_file:
        #read gwa.txt line by line
        for line in input_file:
            variables=line.strip().rsplit('',1)
            if len(variables) ==2:
                name, gwa = variables
                
            
process ()