import os


class Tester:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Projekt:
    def __init__(self, name, tester):
        self.name = name
        self.tester = tester


# Function to repeatedly prompt user for tester name and check the input is a letter
def inputTesterDetails():
    testerName = input("Type in the tester's name: ")
    testerSurname = input("Type in the tester's surname: ")

    while not testerName.isalpha() or testerName.isspace()\
            or not testerSurname.isalpha() or testerSurname.isspace():
        testerName = input("Type in the tester's name: ")
        testerSurname = input("Type in the tester's surname: ")

    return [testerName, testerSurname]


# Function to repeatedly prompt user for project name and check the input is a letter
def inputProjectDetails():
    projectName = input("Type in the project's name: ")

    while not projectName.isalpha() or projectName.isspace():
        projectName = input("Type in the project's name: ")

    return projectName


# Function that writes project and tester details into a file
def writeIntoFile(fileName, projectName, tester):

    # Append if file already exists, create a new one otherwise
    if os.path.exists(fileName):
        appendWrite = 'a'
    else:
        appendWrite = 'w'

    projectsFile = open(fileName, appendWrite)

    projectsFile.write('Project name: ' + projectName.name + '\n')
    projectsFile.write('Main tester: ' + tester.name + ' ' + tester.surname + '\n')

    projectsFile.close()


# Function that writes from a file
def writeFromFile(fileName):

    projectFile = ''

    try:
        projectFile = open(fileName)

        for line in projectFile:
            print(line)
    except IOError:
        print('File not found.')
    finally:
        projectFile.close()


# Ask user to input 2 testers
testerOneInput = inputTesterDetails()
testerTwoInput = inputTesterDetails()


# Create two tester objects
testerOne = Tester(testerOneInput[0], testerOneInput[1])
testerTwo = Tester(testerTwoInput[0], testerTwoInput[1])


# Ask user to input 2 projects
projectOneInput = inputProjectDetails()
projectTwoInput = inputProjectDetails()


# Create two project objects
projectOne = Projekt(projectOneInput, testerOne)
projectTwo = Projekt(projectTwoInput, testerTwo)


# Write into file
txtFile = 'projekti.txt'
writeIntoFile(txtFile, projectOne, testerOne)
writeIntoFile(txtFile, projectTwo, testerTwo)


# Write from file
writeFromFile(txtFile)
