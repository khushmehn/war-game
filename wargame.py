def main():
    while True:
        print('Welcome to The War Game. Choose the scenario:')
        print('1) First Battle of Panipat: Babur VS Ibrahim Lodi')
        print('2) Cold War : Russia VS USA')
        print('3) North Korea VS South Korea')
        print('4) END/EXIT')
        Scenario = input('Enter 1,2,3 or 4 here: ')
        if int(Scenario) == 1:
            print('This is The First Battle of Panipat: Babur VS Ibrahim Lodi')
            Check = Scenario1()
            if Check == -1:
                break
        elif int(Scenario) == 2:
            print('This is then Cold War: Russia VS USA')
            Check1 = Scenario2()
            if Check1 == -1:
                break
        elif int(Scenario) == 3:
            print('This is North Korea VS South Korea')
            Check2 = Scenario3()
            if Check2 == -1:
                break
        elif int(Scenario) == 4:
            break
        else:
            print('Please Enter a Valid Choice')


def Scenario1():
    B = 100
    I = 100
    while B > 0 and I > 0:
        print("Babur's Turn")
        print('You can choose your move from the following options:')
        print('1) Artillary')
        print('2) Flank Attack')
        print('3) Cannon')
        print('4) Surrender')
        Move1 = input('Enter 1, 2, 3 or 4 here: ')
        if int(Move1) == 1:
            I -= 30
        elif int(Move1) == 2:
            I -= 40
        elif int(Move1) == 3:
            I -= 20
        elif int(Move1) == 4:
            print('Babur has surrendered , Lodi Wins')
            break
        else:
            print('Please Enter a Valid Choice')
        print("Ibrahim Lodi's Turn")
        print('You can choose your move from the following options:')
        print('1) Artillary')
        print('2) Onward March')
        print('3) Cannon')
        print('4) Surrender')
        Move2 = input("Please Select: ")
        if int(Move2) == 1:
            B -= 40
        elif int(Move2) == 2:
            B -= 20
        elif int(Move2) == 3:
            B -= 30
        elif int(Move2) == 4:
            print("Lodi has surrendered , Babur Wins")
            break
        else:
            print('Please Enter a Valid Choice')
        print('Babur your score is', B)
        print('Lodi your score is', I)
    if B > I:
        print('Babur Wins')
    elif I > B:
        print('Lodi Wins')
    else:
        print("That's a tie!")
    action1 = 'n'
    while action1 == 'y' or action1 == 'n':
        action1 = input("press 'y' to end game or 'n' to change scenario :")
        if action1 == 'y':
            action1 = 0
            return -1
        elif action1 == 'n':
            action1 = 0
        else:
            print('Enter a Valid Choice')


def Scenario2():
    A = 100
    R = 100
    while A > 0 and R > 0:
        print("America's Turn")
        print('You can choose your move from the following options:')
        print('1) Embargo')
        print('2) Nuclear Bomb')
        print('3) Proxy')
        print('4) Surrender')
        Move1 = input('Enter 1, 2, 3 or 4 here: ')
        if int(Move1) == 1:
            R -= 25
        elif int(Move1) == 2:
            R -= 50
        elif int(Move1) == 3:
            R -= 20
        elif int(Move1) == 4:
            print('America has surrendered , Russia Wins')
            break
        else:
            print('Please Enter a Valid Choice')
        print("Russia's Turn")
        print('You can choose your move from the following options:')
        print('1) Proxy')
        print('2) Nuclear Bomb')
        print('3) Blockade')
        print('4) Surrender')
        Move2 = input('Enter 1, 2, 3 or 4 here: ')
        if int(Move2) == 1:
            A -= 25
        elif int(Move2) == 2:
            A -= 50
        elif int(Move2) == 3:
            A -= 20
        elif int(Move2) == 4:
            print('Russia has surrendered , America Wins')
            break
        else:
            print('Please Enter a Valid Choice')
        print('America your score is', A)
        print('Russia your score is', R)
    if A > R:
        print('America Wins')
    elif R > A:
        print('Russia Wins')
    else:
        print("That's a tie!")
    action2 = 'n'
    while action2 == 'y' or action2 == 'n':
        action2 = input("press 'y' to end game or 'n' to change scenario :")
        if action2 == 'y':
            action2 = 0
            return -1
        elif action2 == 'n':
            action2 = 0
        else:
            print('Enter a Valid Choice')


def Scenario3():
    N = 100
    S = 100
    while N > 0 and S > 0:
        print("North Korea's Turn")
        print('You can choose your move from the following options:')
        print('1) Conventional attack')
        print('2) Nuclear Bomb')
        print('3) Propaganda')
        print('4) Surrender')
        Move1 = input('Enter 1, 2, 3 or 4 here: ')
        if int(Move1) == 1:
            S -= 35
        elif int(Move1) == 2:
            S -= 50
        elif int(Move1) == 3:
            S -= 10
        elif int(Move1) == 4:
            print('North Korea has surrendered , South Korea Wins')
            break
        else:
            print('Please Enter a Valid Choice')
        print("South Korea's Turn")
        print('You can choose your move from the following options:')
        print('1) Conventional Attack')
        print('2) Call for US intervention')
        print('3) Blockade')
        print('4) Surrender')
        Move2 = input('Enter 1, 2, 3 or 4 here: ')
        if int(Move2) == 1:
            N -= 45
        elif int(Move2) == 2:
            N -= 60
        elif int(Move2) == 3:
            N -= 10
        elif int(Move2) == 4:
            print('South Korea has surrendered , North Korea Wins')
            break
        else:
            print('Please Enter a Valid Choice')
        print('North Korea your score is', N)
        print('South Korea your score is', S)
    if N > S:
        print('North Korea Wins')
    elif S > N:
        print('South Korea Wins')
    else:
        print("That's a tie!")
    action3 = 'n'
    while action3 == 'y' or action3 == 'n':
        action3 = input("press 'y' to end game or 'n' to change scenario :")
        if action3 == 'y':
            action3 = 0
            return -1
        elif action3 == 'n':
            action3 = 0
        else:
            print('Enter a Valid Choice')


main()
