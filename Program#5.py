def get_user_file(user_file, readwrite):
    """get the name of the file to be edited from the user. Error check and print a prompt if an error is thrown."""
    while True:
        file_given = input(user_file,)#getting the input the user has entered
        try:
            correct_File = open(file_given, readwrite)
        except FileNotFoundError:
            print("File name incorrect, please try again.")#Error handling for FileNotFoundError
        except IOError:
            print("IOError, please try again.")#Error handling for IOError
        else:
            return correct_File#If there is no issues with the file that the user has entered, the file is returned and ready to use

def get_filter(question, acceptable_answers):
    """Get input from user, decide what filter they would like to use"""
    while True:
        choice = input(question)
        if choice in acceptable_answers:#acceptable answers is a list of the strings 1,2 or 3
            return choice

def check_format(user_file):
    """checks format of file to see if it is a ppm file. firs line should contain P3 and third line should contain 255"""
    lst = user_file.readlines()
    if "P3" not in lst[0] or "255" not in lst[2]:#error handling for if P3 or 255 are not in the proper spots
        print("The file you have submitted is not the correct file type. Please try another file.")
        return False
    return True





while True:
    user_file = get_user_file("What is that name of the picture file you would like to edit?","r")#user input for the file name of the image they would like to convert
    if check_format(user_file)==True:#error handling for file format, causing the above prompt if the format is incorrect
        break



file_created = get_user_file("Please name a file you would like to write your image too.","w")#user input for the file name that the user would like to write to
user_filter = get_filter("choose one of the following; 1.)Grayscale 2.)Vintage 3.)Quit (please choose 1, 2 or 3)",["1","2","3"])#user input for what they would like to do with their file and assigning that choice to acceptable_answers

while True:
    if user_filter=="1":#if user chooses conversion to grayscale
        list_file = []
        for line in user_file:#iterate over lines in user file
            list_file.append(line.strip("\n"))#strips spaces
        for line in list_file[0:3]:#getting the formatting info from the top three lines of the file
            file_created.write(line+"\n")#creating new file with the formating info included and adding spaces back in
        new_list = list_file[3:]#focusing on the lines not containing formating info
        for i in range(int(len(new_list)/3)):#dividing the list into segments of three indices
            pixel = new_list[i*3:(i*3)+3]#each pixel contains three indices then moves to the next three indices by incrementing by three times the index plus three
            red_color = int(pixel[0])*0.299#red color converted to grayscale is 29.9% of the origional value
            green_color = int(pixel[1])*0.587#green color converted to grayscale is 58.7% of the origional value
            blue_color = int(pixel[2])*0.114#blue color converted to grayscale is 11.4% of the origional value
            total_pixel  = red_color+green_color+blue_color#summing the value of all the pixels
            file_created.write((str(total_pixel)+"\n")*3)#making the total pixel the value for the three pixels in that group


    elif user_filter == "2":#if user chooses conversion to vintage
        list_file = []
        for line in user_file:
            list_file.append(line.strip("\n"))
        for line in list_file[0:3]:#keeping all of the format information and adding it back to file file that we are creating later
            file_created.write(line+"\n")
            new_list = list_file[3:]
        for i in range(int(len(new_list)/3)):#dividing list into groups of three
            pixel = new_list[i*3:(i*3)+3]#isolating slices of three, same as last time
            red_color = int(pixel[0])
            green_color = int(pixel[1])
            blue_color = int(pixel[2])*0.5#in vintage, blue is the only color that is converted. Converted to half of its origional value

            file_created.write(str(red_color)+"\n")
            file_created.write(str(green_color)+"\n")
            file_created.write(str(blue_color)+"\n")#writing all of the pixels to a file

    elif user_filter == "3":#if user chooses to quit the program
        break
    else:
        print("incorrect input, please choose from 1, 2, or 3.")#error handling for if the user does not enter 1,2 or 3 for an answer to the prompt
