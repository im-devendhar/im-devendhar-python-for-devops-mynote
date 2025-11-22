import sys
type = sys.argv[1]

if type == "t2.micro":
    print("It will charge you 2 dollars a day")
elif type == "t2.medium":
    print("It will charge you 4 dollars a day")
elif type == "t2.xlarge":
    print("It will charge you 8 dollars a day")
else:
    print("Please provide a valid instance type")
