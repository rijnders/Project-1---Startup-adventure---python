# My first first little code try ever
# By Michel Rijnders - lastname at gmail
# Learning Python the hard way by Zed Shaw
# Questions I probably can't answer very good yet
# Comments and feedback are always welcome
# Do I need to say this is work in progress? :-)


from sys import exit

def start(app_phase, your_money, investors_money):
    print "You are building an app."
    print "You really believe this could be successful."
    print "You have $", your_money,"."
    print "What are you going to do?"
    print "-----------------------------------------------------------------------"
    print "1. Travel and party!"
    print "2. Sell"
    print "3. Build"
    print "-----------------------------------------------------------------------"

    start_choice = raw_input("> ")
    if "1" in start_choice or "travel" in start_choice or "party" in start_choice:
        retire(app_phase, your_money, "You travel the world and party")
    elif "2" in start_choice or "sell" in start_choice:
        sell(app_phase, your_money, investors_money)
    elif "3" in start_choice or "build" in start_choice:
        build(app_phase, your_money, investors_money)
    else:
        retire(app_phase, your_money, "Nobody gets what you are talking about. Nobody gives money anymore. You exit and live lonesome")

def build(app_phase, your_money, investors_money):
    if app_phase == 0 and your_money >= 5000:
        print "You glue together a MVP of your product."
        print "You spend $5000"
        app_phase += 1
        your_money -= 5000
        raw_input("Enter to continue")
        start(app_phase, your_money, investors_money)
    elif app_phase == 1 and your_money >= 30000:
        print "You build a decent version 1.0"
        print "You spend $30000"
        app_phase += 1
        your_money -= 30000
        raw_input("Enter to continue")
        start(app_phase, your_money, investors_money)
    elif app_phase == 2 and your_money >= 50000:
        print "You build your product that is ready for scale-up"
        print "You spend $50000"
        app_phase += 1
        your_money -=50000
        raw_input("Enter to continue")
        start(app_phase, your_money, investors_money)
    elif app_phase == 3:
        print "You reached your goal and dream! You sell the company for $", investors_money
        your_money += investors_money
        retire(app_phase, your_money, "Whoohoo!")
    else:
        retire(app_phase, your_money, "You started investing in building the product, but ran out of money.")


def sell(app_phase, your_money, investors_money):
    if app_phase == 0 and investors_money > 0:
        print "You spend $2000 on marketing and sales"
        print "Your sales income is $7000"
        your_money -= 2000
        your_money += 7000
        investors_money -= 7000
        start(app_phase, your_money, investors_money)
    elif app_phase == 1 and investors_money > 0:
        print "You spend $5000 on marketing and sales"
        print "You sold for $5000"
        your_money -= 5000
        your_money += 5000
        investors_money -= 5000
        start(app_phase, your_money, investors_money)
    elif app_phase == 2 and investors_money > 0:
        print "You spend $30.000 on marketing and sales"
        print "You sold for $100.000"
        your_money -= 30000
        your_money += 100000
        investors_money -= 100000
        start(app_phase, your_money, investors_money)
    elif app_phase == 0 or app_phase == 1:
        your_money = 0
        retire(app_phase, your_money, "Customers don't see the promised product they paid for. They get their money back.")
    else:
        retire(app_phase, your_money, "People don't want to invest in your product anymore. The market ran out of money.")


def retire(app_phase, your_money, why):
    print why, "You live nicely for", your_money / 5000, "months. Than you run out of money and die peacefully."
    exit(0)

start(0, 50000, 500000)
