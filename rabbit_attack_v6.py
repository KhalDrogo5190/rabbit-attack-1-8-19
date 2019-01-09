# Rabbit Attack!

def start():
    print("Welcome to RABBIT ATTACK!")
    print("     / \ ")
    print("    / _ \ ")
    print("   | / \ | ")
    print("   ||   || _______ ")
    print("   ||   || |\     \ ")
    print("   ||   || ||\     \ ")
    print("   ||   || || \    | ")
    print("   ||   || ||  \__/ ")
    print("   ||   || ||   || ")
    print("    \\_/ \_/ \_// ")
    print("   /   _     _   \ ")
    print("  /               \ ")
    print("  |    O     O    | ")
    print("  |   \  ___  /   | ")                           
    print(" /     \ \_/ /     \ ")
    print("/  -----  |  --\    \ ")
    print("|     \__/|\__/ \   | ")
    print("\       |_|_|       / ")
    print(" \_____       _____/ ")
    print("       \     /")
    print("       |     |")

def end():
    print("Goodbye. Thanks for playing!")
    print("")  
    print("        o8%8888, ")    
    print("      o88%8888888. ")  
    print("     8'-    -:8888b ")   
    print("    8'         8888 ")  
    print("   d8.-=. ,==-.:888b ")  
    print("   >8 `~` :`~' d8888 ")   
    print("   88         ,88888 ")   
    print("   88b. `-~  ':88888 ")  
    print("   888b ~==~ .:88888 ") 
    print("   88888o--:':::8888 ")      
    print("   `88888| :::' 8888b ")  
    print("   8888^^'       8888b ")  
    print("  d888           ,%888b. ")   
    print(" d88%            %%%8--'-. ")  
    print("/88:.__ ,       _%-' ---  -  ") 
    print("    '''::===..-'   =  --. ")
    
def confirm(question):
    while True:
        answer = input(question + " (y/n)")
        answer = answer.lower()
        
        if answer in ["y" , "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False

def play():
    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")
            
        if use_grenade:
            print("1... 2... 5... No, 3!")
            print("")
            print("'.  \ | /  ,' ")
            print("  `. `.' ,' ")
            print(" ( .`.|,' .) ")
            print(" - ~ -0- ~ - ")
            print("")
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")


start()

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
