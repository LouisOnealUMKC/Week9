import math

TestScores = []
Assignments = []

TestWeight = 0.6
AssignmentWeight = 0.4


def GradeMenu():
    selection = input("1 -Add Test\n2 -Remove Test\n3 -Clear Tests\n4 -Add Assignment\n5 -Remove Assignment\n6 -Clear Assignments\nD -Display Scores\nQ -Quit\n==> ").upper()
    print (selection)
    if(selection == "1"):
        AddTest()
    elif(selection == "2"):
        RemoveTest()
    elif(selection == "3"):
        ClearTest()
    elif(selection == "4"):
        AddAssignment()
    elif(selection == "5"):
        RemoveAssignment()
    elif(selection == "6"):
        ClearAssignments()
    elif(selection == "D"):
        DisplayScores()
    elif(selection == "Q"):
        QuitProgram()
    else:
        GradeMenu()

def AddTest():
    TestScore = float(input("Enter the new Test score 0-100 ==> "))
    if not isinstance(TestScore,float):
        GradeMenu()
    if TestScore < 0:
        GradeMenu()
    else:
        TestScores.append(TestScore)
    GradeMenu()

def RemoveTest():
    TestScore = input("Enter the Test to remove 0-100 ==> ")
    if TestScore in TestScores:
        TestScores.remove(TestScore)
    elif TestScore not in TestScores:
        print("Could not find that score to remove")
    GradeMenu()

def ClearTest():
    TestScores.clear()
    GradeMenu()

def AddAssignment():
    Assignment = float(input("Enter the new Assignment score 0-100 ==> "))
    Assignments.append(Assignment)
    GradeMenu()

def RemoveAssignment():
    Assignment = input("Enter the Assignment to remove 0-100 ==> ")
    if Assignment in Assignments:
        Assignments.remove(Assignment)
    elif Assignment not in Assignments:
        print("Could not find that score to remove")
    GradeMenu()

def ClearAssignments():
    Assignments.clear()
    GradeMenu()

def DisplayScores():
    if(TestScores):
        print("Tests # {} min: {} max: {} avg: {} std: {}".format(len(TestScores),min(TestScores),max(TestScores), Mean(TestScores), StandardDeviation(TestScores)))
    elif not (TestScores):
        print("Test # n/a min: n/a max: n/a avg: n/a std: n/a")        
    if(Assignments):
        print("Programs # {} min: {} max: {} avg: {} std: {}".format(len(Assignments),min(Assignments),max(Assignments), Mean(Assignments), StandardDeviation(Assignments)))
    elif not (Assignments):
        print("Programs # n/a min: n/a max: n/a avg: n/a std: n/a")

    TestWeighted = 100 * TestWeight
    AssignmentsWeighted = 100 * AssignmentWeight
    if TestScores : TestWeighted = Mean(TestScores) * TestWeight
    if Assignments: AssignmentsWeighted = Mean(Assignments) * AssignmentWeight
    if TestScores or Assignments : 
        WeightedScore = TestWeighted + AssignmentsWeighted
        print("The weighted scores is ", WeightedScore)
    GradeMenu()

def QuitProgram():
    quit()

def Mean(list):
    if(list):
        Sum = 0
        for value in list:
            Sum += int(value)
        Mean = Sum / len(list)
        return Mean

def StandardDeviation(list):
    if(list):
        meanval = 0
        meanval = Mean(list)
        tempSD = 0
        for value in list:
            workingValue = (int(value) - meanval)**2
            tempSD += workingValue
        return math.sqrt(tempSD / len(list))

GradeMenu()

