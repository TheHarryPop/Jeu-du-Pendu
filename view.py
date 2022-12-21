class View:
    @staticmethod
    def home():
        print("Bienvenue,\n"
              "Tapez 1 pour créer un nouveau profil\n"
              "Tapez 2 pour charger un profil existant\n"
              "Tapez 3 pour quitter l'application")
        return input("Votre choix : ")

    @staticmethod
    def no_players():
        return print("Il n'y a aucun profil enregistré")

    @staticmethod
    def value_needed():
        return print('Vous devez renseigner une valeur proposée')

    @staticmethod
    def incorrect_selection():
        return print("Sélection incorrect")

    @staticmethod
    def create_player():
        return input("Entrez votre nom : ")

    @staticmethod
    def already_exist():
        return print('Ce joueur existe déjà')

    @staticmethod
    def select_player(players):
        print("Veuillez sélectionner votre joueur")
        i = 0
        for player in players:
            print(f"Pour sélectionner {player}, tapez : {i}")
            i += 1
        return input("Votre choix : ")

    @staticmethod
    def select_menu(player):
        print(f'Bonjour {player.name}, votre score actuel est : {player.score}\n'
              f'Tapez 1 pour commencer une nouvelle partie\n'
              f'Tapez 2 pour quitter le jeu')
        return input("Votre choix : ")

    @staticmethod
    def letter_choice(word, trials, error):
        if not error:
            print(f'{word}')
            print(f'Il vous reste {trials} essais.')
        elif error == 1:
            print('Vous devez renseigner un seul caractère')
        elif error == 2:
            print('Vous devez choisir une lettre')
        elif error == 3:
            print('Vous avez déjà proposé cette lettre')
        return input("Quelle lettre choississez vous ? : ")

    @staticmethod
    def wrong_letter():
        return print("Cette lettre ne fait pas partie du mot recherché")

    @staticmethod
    def victory(player, word):
        return print(f'Félicitations {player.name}, vous avez trouvé {word} !\n'
                     f'Votre nouveau score : {player.score}')

    @staticmethod
    def defeat(word, score):
        return print('Vous avez perdu...\n'
                     f'Le mot était {word}\n'
                     f'Votre nouveau score est {score}')


