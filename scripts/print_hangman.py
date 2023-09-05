def menu():
    print("""               Daren's hangman
    -------------------------------------------------------------
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                  /|\       |
                                  / \       |
                                   _________|__________
    
    """)




def gamephase0():
    print("""
    
                                    ________
                                   |        |
                                   |        |
                                            |
                                            |
                                            |
                                   _________|__________
    
    """)


def gamephase1():
    print("""

                                    ________
                                   |        |
                                   |        |
                                   o        |
                                            |
                                            |
                                   _________|__________

    """)


def gamephase2():
    print("""
    
    
    
    
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                   |        |
                                            |
                                   _________|__________
    
    """)


def gamephase3():
    print("""
    
    
    
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                  /|        |
                                            |
                                   _________|__________
    
    """)


def gamephase4():
    print("""
    
    
    
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                  /|\       |
                                            |
                                   _________|__________
    """)



def gamephase5():
    print("""
    
    
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                  /|\       |
                                  /         |
                                   _________|__________
    """)


def gamephase6():
    print("""
    
                                    You Lose
                                    ________
                                   |        |
                                   |        |
                                   o        |
                                  /|\       |
                                  / \       |
                                   _________|__________
    """)


def print_gamestate(lives):
    if (lives == 6):
        gamephase0()
    elif (lives == 5):
        gamephase1()
    elif (lives == 4):
        gamephase2()
    elif (lives == 3):
        gamephase3()
    elif (lives == 2):
        gamephase4()
    elif (lives == 1):
        gamephase5()
    elif (lives == 0):
        gamephase6()
