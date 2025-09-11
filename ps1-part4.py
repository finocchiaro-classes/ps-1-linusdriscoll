
#Establish variables for user input

prior = int(input("Prior arrests: "))
ordinance = input("Prior arrests for local ordinance (Y/N): ")
age = int(input("Age at release: "))

#Define function for recidivism risk

def recidivism_risk(prior,ordinance,age):
    value = 0
    if prior >= 2:
        value+=1
    if prior >= 5:
        value+=1
    if ordinance == "Y":
        value+=1
    if age in range(18,24):
        value+=1
    if age >= 40:
        value-=1
    print("The recidivism risk score is", (value))

#Call function

recidivism_risk(prior,ordinance,age)

    
