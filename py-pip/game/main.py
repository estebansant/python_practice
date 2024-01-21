import random

def choose_options():
    options = ("piedra", "papel", "tijera")

    user_option = input("Piedra, papel o tijera =>")

    if not user_option in options:
        print("esa opción no es válida")
        #continue
        return None, None
        
    user_option = user_option.lower()
    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)
    return (user_option, computer_option)

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if (user_option == computer_option):
        print("Empate")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("Piedra gana a tijera")
            print("Ganó el usuario")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("Ganó la computadora")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("Papel gana a piedra")
            print("Ganó el usuario")
            user_wins += 1
        else:
            print("Tijera gana a papel")
            print("Ganó la computadora")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("Tijera gana a papel")
            print("Ganó el usuario")
            user_wins += 1
        else:
            print("Piedra gana a tijera")
            print("Ganó la computadora")
            computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    if user_wins == 2:
            print("El usuario es el ganador del partido")
    elif computer_wins == 2:
        print("La computadora es la ganadora del partido")

def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0

    while (user_wins < 2) and (computer_wins < 2):

        print("*" * 10)
        print("ROUND #", rounds)
        print("*" * 10)

        user_option, computer_option = choose_options()

        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        check_winner(user_wins, computer_wins)

        rounds +=1
        
        print("Rondas ganadas por el usuario:", user_wins)
        print("Rondas ganadas por la computadora:", computer_wins)

run_game()
