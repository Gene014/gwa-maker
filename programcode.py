# Calma, Eugene Marie S.
# BSCPE_1-4
# OOP Laboratory Exercise Number 3 Problem 2 (GWA-MAKER)

#Write a Python program that read a file containing the name of 20 students together with their GWA. 
#The program will outputs the name of the student who got the highest GWA (including the GWA).


#set variables for max gwa and for the uname
max_gwa=0
max_name=""
    #open gwa.txt (read)
with open("gwa.txt","r") as input_file:
        #read gwa.txt line by line
        for line in input_file:
            profile=line.strip().rsplit(' ',1)
            if len(profile) ==2:
                name, gwa = profile
            #convert gwa to float
                gwa=float(gwa)
                if max_gwa == 0:
                    max_gwa= gwa
                    max_name= name
                    #check if current gwa is greater than maximum gwa
                if gwa < max_gwa: 
                    #update the maximum gwa and student name
                    max_gwa= gwa
                    max_name= name
                    #print the output
        print(f"The student with the highest GWA is {max_name} with a GWA of {max_gwa:.2f}. Have a good day!")
