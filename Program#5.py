########################################################################
##
## CS 101
## Program # 5
## Name Brooke McFarland
## Email blmz99@mail.umkc.edu
##
## PROBLEM : Take an image file provided by the user and convert it to grayscale or a vintage filter
##
## ALGORITHM :
##      1.)	Prompt user to input what type of filter they would like on their picture.
##a.	Function
##i.	Grayscale
##ii.	Vintage
##iii.	Quit
##1.	Break
##2.)	Prompt user for what file they would like to use
##a.	Function
##i.	User file to be opened
##1.	Try / except error handling
##a.	FileNotFoundError
##i.	Print(“Invalid file name, please try again.”)
##b.	IOError
##i.	Print(“IOError, please input file name again.”)
##ii.	Prompt for a file they would like to write out to
##1.	Error handling for invalid file name format
##iii.	Close file
##3.)	Check if file is formatted correctly
##a.	Function
##b.	Iterate over user file
##i.	Run a check to verify the P3 is in the first line of the file
##1.	If p3 not in first line of file
##a.	Print(“Error, incorrect file”)
##ii.	Check that color depth is 255
##1.	If color depth is not 255
##a.	Print(“Error, incorrect file”)
##4.)	If user selects grayscale
##a.	For red in pixel: grayscale = 0.299*red
##b.	For green in pixel: grayscale = 0.587*green
##c.	For blue in pixel: grayscale = 0.114*blue
##d.	The sum of all of these pixels = total grayscale
##5.)	If user selects vintage
##a.	Iterate over user file
##b.	Find the blue value in pixel
##c.	Decrease the value of the blue pixel by ½ so that if it had been 100, it would be converted to 50.
##
##
## ERROR HANDLING:
##      IOError used to catch incorrect special charactors in user file names
##      FileNotFounError catch if a file is not stored in the same location as the program
##      prompting user if:
##          incorrect response to choice of 1, 2, 3
##          incorrect file format
##
##
## OTHER COMMENTS:
##  "Now stand aside, worthy advisary!"
##  "Tis but a scratch!"
##  "A scratch? Your arm's off!"
##  "No, it isn't."
##          - Monty Python and the Holy Grail
##
########################################################################
def get_user_file(user_file, readwrite):
    """get the name of the file to be edited from the user. Error check and print a prompt if an error is thrown.
    while true, will loop until no error is thrown
    IOError mostly using to catch if user puts a asterisk in their file name"""
    while True:
        file_given = input(user_file)
        try:
            correct_File = open(file_given, readwrite)
        except FileNotFoundError:
            print("File name incorrect, please try again.")
        except IOError:
            print("IOError, please try again.")
        else:
            return correct_File

def get_filter(question, acceptable_answers):
    """Get input from user, decide what filter they would like to use acceptable answers indicates which of the three choices the user has chosen"""
    while True:
        choice = input(question)
        if choice in acceptable_answers:
            return choice
#while loop created to always be true
#user file gets passed through the get_user_file and is assigned to the file the user would like to read
#file_created gets passed through the get_user_file and is assigned to the file the user would like to write to
#user_filter gets passed through the get_filter function and is assigend to choice 1, 2, 3
while True:
    user_file = get_user_file("What is that name of the picture file you would like to edit?","r")
    file_created = get_user_file("Please name a file you would like to write your image too.","w")
    user_filter = get_filter("choose one of the following:\n 1.)Grayscale\n 2.)Vintage\n 3.)Quit\n (please choose 1, 2 or 3)",["1","2","3"])
    #if the user chooses 3, the program will quit
    if user_filter == "3":
        break
    #set list_file to empty string
    #for each item in list_file the carriage return is removed
    #a check for "P3" and "255"
    #if those strings at first and third line, the file is correct format and program continues. If not correct format, loop starts over and asks for new file to read
    list_file = []
    for line in user_file:
        list_file.append(line.strip("\n"))
    if "P3" not in list_file or "255" not in list_file:
        print("The file you have submitted is not the correct file type. Please try another file.")
        continue
    #if user chooses choice 1 the user has chosen to convert the image to grayscale
    #the first three lines are ignored untile we put the file back together when writing to the file the user has given
    #list divided into segments of three in new_list
    #each value in each segment has its value changed to a percentage of the origional value to convert to grayscale
    #total_pixel sums all of the segments and concatenates them, then assignes that value as the value for all three color types in the segement
    #writes converted data to file with origional format
    if user_filter=="1":
        for line in list_file[0:3]:
            file_created.write(line+"\n")
        new_list = list_file[3:]
        for i in range(int(len(new_list)/3)):
            pixel = new_list[i*3:(i*3)+3]
            red_color = int(pixel[0])*0.299
            green_color = int(pixel[1])*0.587
            blue_color = int(pixel[2])*0.114
            total_pixel = red_color+green_color+blue_color
            file_created.write((str(total_pixel)+"\n")*3)
        print("\nYour grayscale photo is ready.")
        break

    #if user choice is 2, the file is converted to the vintage filter
    #the the carrage return and the first three lines are ignored
    #new_list divided into segments of three
    #only pixel color that is altered is blue
    #combines all pixels into a file that has been written to with origional format
    elif user_filter == "2":
        for line in list_file[0:3]:
            file_created.write(line+"\n")
        new_list = list_file[3:]
        for i in range(int(len(new_list)/3)):
            pixel = new_list[i*3:(i*3)+3]
            red_color = int(pixel[0])
            green_color = int(pixel[1])
            blue_color = int(pixel[2])*0.5

            file_created.write(str(red_color)+"\n")
            file_created.write(str(green_color)+"\n")
            file_created.write(str(blue_color)+"\n")
        print("\nYour vintage photo is ready.")
        break

    #Error handling for if user does not put in correct input for what filter they would like to use
    else:
        print("incorrect input, please choose from 1, 2, or 3.")
#closing the file that is being read and the file being written to
user_file.close()
file_created.close()