
def get_user_file(user_file, readwrite):
    """get the name of the file to be edited from the user. Error check and print a prompt if an error is thrown."""
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
    """Get input from user, decide what filter they would like to use"""
    while True:
        choice = input(question)
        if choice in acceptable_answers:
            return choice

def check_format(user_file):
    """checks format of file to see if it is a ppm file. firs line should contain P3 and third line should contain 255"""
    lst = user_file.readlines()
    if "P3" not in lst[0] or "255" not in lst[2]:
        print("The file you have submitted is not the correct file type. Please try another file.")
        return False
    return True



#while True:
user_file = get_user_file("What is that name of the picture file you would like to edit?","r")
    #if check_format(user_file)==True:
        #break

file_created = get_user_file("Please name a file you would like to write your image too.","w")
user_filter = get_filter("choose one of the following; 1.)Grayscale 2.)Vintage 3.)Quit (please choose 1, 2 or 3)",["1","2","3"])

while True:
    if user_filter=="1":
        list_file = []
        for line in user_file:
            list_file.append(line.strip("\n"))
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
        break


    elif user_filter == "2":
        list_file = []
        for line in user_file:
            list_file.append(line.strip("\n"))
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
        break

    elif user_filter == "3":
        break
    else:
        print("incorrect input, please choose from 1, 2, or 3.")
