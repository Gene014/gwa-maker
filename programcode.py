# Calma, Eugene Marie S.
# BSCPE_1-4
# OOP Laboratory Exercise Number 3 Problem 2 (GWA-MAKER)

#Write a Python program that read a file containing the name of 20 students together with their GWA. 
#The program will outputs the name of the student who got the highest GWA (including the GWA).

def process():
    #open gwa.txt (read)
    with open("gwa.txt","r") as input_file:
        #read gwa.txt line by line
        for line in input_file:
            input_gwa = str(line)
            gwa=(input_gwa)
            print(gwa.split())
            edited=(gwa.split())
            print(edited.strip())
process ()