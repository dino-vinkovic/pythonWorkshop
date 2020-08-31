import os


class Tester:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Projekt:
    def __init__(self, name, tester):
        self.name = name
        self.tester = tester


def inputTesterDetails():
    testerName = input("Type in the tester's name: ")
    testerSurname = input("Type in the tester's surname: ")

    while not testerName.isalpha() or testerName.isspace()\
            or not testerSurname.isalpha() or testerSurname.isspace():
        testerName = input("Type in the tester's name: ")
        testerSurname = input("Type in the tester's surname: ")

    return [testerName, testerSurname]


def inputProjectDetails():
    projectName = input("Type in the project's name: ")

    while not projectName.isalpha() or projectName.isspace():
        projectName = input("Type in the project's name: ")

    return projectName


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
fileName = 'projekti.txt'
writeIntoFile(fileName, projectOne, testerOne)
writeIntoFile(fileName, projectTwo, testerTwo)


# Write from file
writeFromFile(fileName)