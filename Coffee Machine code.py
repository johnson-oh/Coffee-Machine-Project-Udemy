#completed

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk':0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machinemoney=0

#asks user which beverage they would like to order, returns a report of how much resources left if 'report' is entered and ends code when 'off' is entered
def ask():
    for key, value in MENU.items():
        print(key)
    while True:
        userinput=input('What would you like?')
        if userinput == 'off':
            exit()
        elif userinput == 'report':
            for key,value in resources.items():
                print(f'{key}: {value}')
            print(f'money: ${machinemoney}')
        elif userinput not in MENU:
            print('try again')

        else:
            print(f'cost is {MENU[userinput]["cost"]}')
            return userinput

#checks if there are sufficent resources to make the coffee
def resourcechecker(beverage):
    lacking=False
    missing=[]
    for key,value in resources.items():
        if resources[key]<MENU[beverage]["ingredients"][key]:
            missing.append(key)
            lacking=True
    if lacking == True:
        print(f'sorry there is not enough resources to make the coffee, missing {missing}')
        return 1
    else:
        return 0

#takes coins from user
def coinprocessor(a):
    if a == 0:
        print('insert coins')
        while True:
            try:
                dollarinput=int(input('$ dollars'))
                break
            except ValueError:
                print('enter an integer')
        while True:
            try:
                quartersinput=int(input('$ quarters'))
                break
            except ValueError:
                print('enter an integer')
        while True:
            try:
                dimesinput = int(input('$ dimes'))
                break
            except ValueError:
                print('enter an integer')
        while True:
            try:
                nickeslinput = int(input('$ nickes'))
                break
            except ValueError:
                print('enter an integer')
        while True:
            try:
                penniesinput = int(input('$ pennies'))
                break
            except ValueError:
                print('enter an integer')
        return quartersinput*0.25+dimesinput*0.10+nickeslinput*0.05+penniesinput*0.01+dollarinput

#checks if coins match price of coffee
def transactionchecker(a,b):
    costofcoffee=MENU[a]['cost']
    global machinemoney
    if b==costofcoffee:
        print(f'success here is your {a} ')
        print(f'enjoy your {a}!')
        for key, value in resources.items():
            resources[key]=resources[key]-MENU[a]["ingredients"][key]
        machinemoney+=costofcoffee
    elif b>costofcoffee:
        print(f'success here is your {a} ')
        print(f'here is the change {round(b-costofcoffee,2)}')
        print(f'enjoy your {a}!')
        for key, value in resources.items():
            resources[key]=resources[key]-MENU[a]["ingredients"][key]
        machinemoney+=costofcoffee
    else:
        print('sorry that is not enough money. money refunded')


def main():
    while True:
        beverage=ask()
        k=resourcechecker(beverage)
        if k==0:
            totalusermoney=coinprocessor(k)
            transactionchecker(beverage,totalusermoney)
main()
