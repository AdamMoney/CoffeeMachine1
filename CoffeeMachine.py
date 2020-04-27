class coffee_machine:
    def __init__(self, state, water, milk, beans, cups, money):
        self.state = state
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __repr__(self):
      if self.state == "action":
        return "Write action (buy, fill, take, remaining, exit):"
      elif self.state == "remaining":
        print ("The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n${} of money".format(self.water,self.milk,self.beans,self.cups,self.money))
        print ("")
        return "Write action (buy, fill, take, remaining, exit):"
        print ("Machine State is {}".format(test1.state))
      elif self.state == "fill":
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())
        print ("")
        return "Write action (buy, fill, take, remaining, exit):"
      elif self.state == "buy":
        return "What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"
      elif self.state == "1":
        if self.water < 250:
          print ("Sorry, not enough water!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.beans < 16:
          print ("Sorry, not enough coffee beans!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.cups < 1:
          print ("Sorry, not enough disposable cups!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        else:
          self.water -= int(250)
          self.beans -= int(16)
          self.money += int(4)
          self.cups -= int(1)
          print("I have enough resources, making you a coffee!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
      elif self.state == "2":
        if self.water < 350:
          print ("Sorry, not enough water!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.milk < 75:
          print ("Sorry, not enough milk!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.beans  < 20:
          print ("Sorry, not enough coffee beans!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.cups < 1:
          print ("Sorry, not enough disposable cups!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        else:
          self.water -= int(350)
          self.milk -= int(75)
          self.beans -= int(20)
          self.money += int(7)
          self.cups -= int(1)
          print("I have enough resources, making you a coffee!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
      elif self.state == "3":
        if self.water < 200:
          print ("Sorry, not enough water!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.milk < 100:
          print ("Sorry, not enough milk!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.beans  < 12:
          print ("Sorry, not enough coffee beans!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        elif self.cups < 1:
          print ("Sorry, not enough disposable cups!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
        else:
          self.water -= int(200)
          self.milk -= int(100)
          self.beans -= int(12)
          self.money += int(6)
          self.cups -= int(1)
          print("I have enough resources, making you a coffee!")
          print ("")
          return "Write action (buy, fill, take, remaining, exit):"
      elif self.state == "take":
        if self.money >= 0:
            print ("I gave you ${}".format(self.money))
            self.money = int(0)
            print ("")
            return "Write action (buy, fill, take, remaining, exit):"





test1 = coffee_machine("action",400,540,120,9,550)

# now you need to work out a way of changing the state of test 1 via the users input



print(test1) #testing parts although i think this is actually appearing at the
#start! MEH for now sod it!





# starting point of the program

start = "anything"
while test1.state != "exit":
    test1.state = input()

    if test1.state == "fill":
        print(test1)


    elif test1.state == "buy":
        print(test1)
        test1.state = input()
        if test1.state == "1":
            print(test1)
        if test1.state == "2":
            print(test1)
        if test1.state == "3":
            print(test1)

    elif test1.state == "take":
        print(test1)





    elif test1.state == "remaining":
        print(test1)
