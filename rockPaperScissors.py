user_option = input("Piedra, papel o tijera =>")
computer_option = "piedra"

if (user_option == computer_option):
    print("Empate")
elif user_option == "piedra":
    if computer_option == "tijera":
        print("Piedra gana a tijera")
        print("Ganó el usuario")
    else:
        print("Papel gana a piedra")
        print("Ganó la computadora")
elif user_option == "papel":
    if computer_option == "piedra":
        print("Papel gana a piedra")
        print("Ganó el usuario")
    else:
        print("Tijera gana a papel")
        print("Ganó la computadora")
elif user_option == "tijera":
    if computer_option == "papel":
        print("Tijera gana a papel")
        print("Ganó el usuario")
    else:
        print("Piedra gana a tijera")
        print("Ganó la computadora")
