import turtle
while True:
    def CarbonFootprint():
        for i in range(1):
            print("-------------------------------------------------------")
        elec = int(input("Enter your yearly electricity use "))
        mainElec = elec * 0.1
        ask = input("Do you have a private vehicle? ")
        if ask == "No" or ask ==  "nO" or ask == "NO" or ask == "no":
            Factor = 0
            KM = 0
        else:
            KM = int(input("Enter the distance that your vehicle travels per year "))
            Factor = input("Your vehicle? ")
            if Factor == "Car" or Factor == "car" or Factor == "CaR" or Factor == "CAR" or Factor == "car" or Factor == "cAr":
               isCarElectric = input("Is your car electric? ")
               if isCarElectric == "yes" or isCarElectric == "Yes" or isCarElectric == "yEs" or isCarElectric == "YES" or isCarElectric ==  "YeS":
                   Factor = 0
               elif isCarElectric == "No" or isCarElectric ==  "nO" or isCarElectric == "NO" or isCarElectric == "no":
                   Factor = 0.18
               else:
                   return print("Invalid Argument!")
            elif Factor == "cycle" or Factor == "Cycle" or Factor == "CYCLE":
                 Factor = 0
            elif Factor == "Bike" or Factor == "BIKE" or Factor == "bike" or Factor == "Scooter" or Factor == "scooter" or Factor == "SCOOTER":
                Factor = 0.2
            elif Factor == "JEEP" or Factor == "jeep" or Factor == "Jeep":
               isCarElectric = input("Is your jeep electric? ")
               if isCarElectric == "yes" or isCarElectric == "Yes" or isCarElectric == "yEs" or isCarElectric == "YES" or isCarElectric ==  "YeS":
                   Factor = 0
               else:
                   Factor = 0.20
            else:
                return print("Invalid Argument!")
        emission = Factor * KM
        asker = input("do you eat meat? ")
        if asker == "No" or asker ==  "nO" or asker == "NO" or asker == "no":
            asket = input("Are you vegan? ")
            if asket == "No" or asket ==  "nO" or asket == "NO":
                foodies = 3
            else:
                foodies = 2.5
        else:
            foodies = 7
        TotalFood = foodies * 365
        Final = TotalFood+emission+mainElec
        if Final<3000:
            print("little emmision,good")
            t = turtle.Turtle()
            t.speed(1)
            t.setheading(90)
            t.color("green")
            t.circle(50, 30)
            t.dot()
            t.circle(100, 60)
            t.color("orange")
            t.circle(100, 60)
            t.color("red")
            t.circle(100, 60)
            t.hideturtle()
            turtle.done()
        elif Final<10000:
            print("Avrage emmision")
            t = turtle.Turtle()
            t.speed(1)
            t.setheading(90)
            t.color("green")
            t.circle(100, 60)
            t.color("orange")
            t.circle(50, 30)
            t.dot()
            t.circle(100, 60)
            t.color("red")
            t.circle(100, 60)
            t.hideturtle()
            turtle.done()
        else:
            print("High emmision")
            t = turtle.Turtle()
            t.speed(1)
            t.setheading(90)
            t.color("green")
            t.circle(100, 60)
            t.color("orange")
            t.circle(100, 60)
            t.color("red")
            t.circle(50, 30)
            t.dot()
            t.circle(100, 60)
            t.hideturtle()
            turtle.done()

    CarbonFootprint()
