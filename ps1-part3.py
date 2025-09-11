
#Defining heart rate function

def heart_rate(age,goal):
    max_HR = 220 - int(age)
    print("Your maximum heart rate is:", max_HR)
    if goal == "S":
        print("Your target heart rate is between", .8*int(max_HR), "and", max_HR)
    if goal == "E":
        print("Your target heart rate is between", .6*int(max_HR), "and", .8*(max_HR))

#Ask user for age and goal

user_age = input("What is your age? ")
user_goal = input("Is your goal speed (S) or endurance (E)? ")

#Call heart rate function

heart_rate(user_age,user_goal)

