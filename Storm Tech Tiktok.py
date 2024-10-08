import webbrowser
import colorama
from colorama import Fore, Style

def print_ascii_art():
    colorama.init(autoreset=True)  # Initialisation de colorama pour les couleurs
    art = """
  ____________________________ __________    _____   
 ____  _                       
/ ___|| |_ ___  _ __ _ __ ___  
\___ \| __/ _ \| '__| '_ ` _ \ 
 ___) | || (_) | |  | | | | | |
|____/ \__\___/|_|  |_| |_| |_|
    """
    print(Fore.BLUE + art)  # Affiche l'ASCII art en bleu

def open_website():
    url = "https://zefoy.com"
    webbrowser.open(url)

if __name__ == "__main__":
    print_ascii_art()
    choice = input("Cliquer sur 1 pour accéder à la tech : ")
    
    if choice == "1":
        open_website()
        input("Appuyez sur Entrée pour fermer le programme.")  # Garde la fenêtre ouverte après avoir ouvert la page
    else:
        print("Option invalide. Fin du programme.")
        input("Appuyez sur Entrée pour fermer le programme.")
