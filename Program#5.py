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
        if choice in acceptable_answers:
            return choice

def grayscale(user_file):
    lst = user_file.readlines()
    if "P3\n" in lst:
        print("P3")
    elif "P3\n" not in lst:
        print("The file you have submitted is not the correct file type. Please try another file.")







user_file = get_user_file("What is that name of the picture file you would like to edit?","r")
file_created = get_user_file("Please name a file you would like to write your image too.","w")
user_filter = get_filter("choose one of the following; 1.)Grayscale 2.)Vintage 3.)Quit",["1","2","3"]).lower()

if user_filter=="1":
    grayscale(user_file)
    print("It works!!")
elif user_filter == "2":
    print("woah buddy!")
elif user_filter == "3":
    print("kick ass!")
else:
    print("incorrect input, please choose from 1, 2, or 3.")
