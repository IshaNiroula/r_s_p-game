'''  rock scissor paper game  '''

# taking user name and age #
global score
score=0

list = []
name = input("Enter your name: ")

while name.isalpha() == False:
    print("Unvalid username.")
    name = input("Enter valid name: ")

list.append(name)

age = (input("Enter your age: "))
while age.isnumeric() == False or int(age) == 0:
    print("Unvalid age.")
    age = input("Enter valid age: ")

# taking password #

pw = input("Enter the password to enter in the game: ")
a = '1'

while pw != a:
    print("Unvalid password.")
    pw = input("Enter valid password: ")

# after accessing the game #

from random import randint


def menu():

        global score
        print("\t\t\t\t\t\tMENU:")
        ch = int(input("Enter your choice of operations: \n1.Play \n2.Score \n3.Quit"))
        if ch==1:
            game()
        elif ch==2:
            print("Your score is ",score)
            menu()
        elif ch==3:
            print("QUITTING")
            print("Your score is: ",score)
            print("Thank you for playing the game :-)")
            quit(0)
        else:
            print("Invalid input.")
            menu()

def ask():
    y = int(input(" Do you want to\n 1.Play \n 2.Go to menu "))
    if y == 1:

        score = game()


    elif y == 2:

        menu()

    else:
        print("That is not a valid input.")
        ask()

def game():
                global score
                t = ['r', 'p', 's']
                x = t[randint(0, 2)]



                print("...You are going to play rock,paper,scissor game...")
                g = input("Enter r for rock , p for paper , s for scissor .")

                if g == x:
                    print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tTie!")


                elif g == 'r':
                    if x == 'p':
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Loose")

                    else:
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Win!!!")
                        score = score + 1

                elif g == 'p':
                    if x == 's':
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Loose")

                    else:
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Win!!!")
                        score = score + 1

                elif g == 's':
                    if x == 'r':
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Loose")

                    else:
                        print("You entered: ",g,"\nComputer entered: ",x,"\n\t\tYou Win!!!")
                        score = score + 1

                else:
                    print("Invalid input.")

                x = t[randint(0, 2)]


                ask()


menu()



