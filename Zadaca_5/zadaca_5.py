class Tester:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Projekt:
    def __init__(self, name, tester):
        self.name = name
        self.tester = tester


# Function to repeatedly prompt user for tester name and check the input is a letter
def input_tester_details():
    tester_name = ''
    tester_surname = ''

    while not tester_name.isalpha() or not tester_surname.isalpha():
        tester_name = input("Type in the tester's name: ")
        tester_surname = input("Type in the tester's surname: ")

    return tester_name, tester_surname


# Function to repeatedly prompt user for project name and check the input is a letter
def input_project_details():
    project_name = ''

    while not project_name.isalpha():
        project_name = input("Type in the project's name: ")

    return project_name


# Function that writes project and tester details into a file
def write_into_file(file_name, project_name, tester):

    # Append if file already exists, create a new one otherwise
    projects_file = open(file_name, 'a')

    projects_file.write('Project name: ' + project_name.name + '\n')
    projects_file.write('Main tester: ' + tester.name + ' ' + tester.surname + '\n')

    projects_file.close()


# Function that writes from a file
def write_from_file(file_name):

    project_file = ''

    try:
        project_file = open(file_name)

        for line in project_file:
            print(line)
    except IOError:
        print('File not found.')
    finally:
        project_file.close()


# Ask user to input 2 testers
tester_one_input = input_tester_details()
tester_two_input = input_tester_details()


# Create two tester objects
tester_one = Tester(tester_one_input[0], tester_one_input[1])
tester_two = Tester(tester_two_input[0], tester_two_input[1])


# Ask user to input 2 projects
project_one_input = input_project_details()
project_two_input = input_project_details()


# Create two project objects
project_one = Projekt(project_one_input, tester_one)
project_two = Projekt(project_two_input, tester_two)


# Write into file
txt_file = 'projekti.txt'
write_into_file(txt_file, project_one, tester_one)
write_into_file(txt_file, project_two, tester_two)


# Write from file
write_from_file(txt_file)
