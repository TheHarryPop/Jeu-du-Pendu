import random

from database import Database
from view import View
from model import Player

NB_COUPS = 8

MOTS = [
    'bonsai',
    'chat',
    'ordure',
    'maison',
    'mobile',
    'navet',
    'torture',
    'ordonner',
    'football',
    'voiture',
    'finale',
    'europe',
    'oiseau',
    'dinosaure',
    ]


class Controller:

    def __init__(self):
        self.scores = Database()
        self.view = View()
        self.player = None
        self.words = MOTS

    def home(self):
        possible_choices = [1, 2, 3]
        choice = self.view.home()
        integer = False
        while not integer:
            try:
                int(choice)
                integer = True
            except ValueError:
                self.view.value_needed()
                choice = self.view.home()
        while int(choice) not in possible_choices:
            self.view.incorrect_selection()
            self.home()
        if int(choice) == 1:
            self.create_player()
        elif int(choice) == 2:
            self.get_player()
        elif int(choice) == 3:
            exit()

    def create_player(self):
        players = [player for player in self.scores.scores]
        not_created = True
        player = self.view.create_player()
        while not_created:
            if player in players:
                self.view.already_exist()
                player = self.view.create_player()
            else:
                self.player = Player(name=player, score=0)
                not_created = False
        return self.menu()

    def get_player(self):
        players = [player for player in self.scores.scores]
        if not players:
            self.view.no_players()
            self.home()
        scores = [score for player, score in self.scores.scores.items()]
        not_selected = True
        choice = self.view.select_player(players)
        integer = False
        while not integer:
            try:
                int(choice)
                integer = True
            except ValueError:
                self.view.value_needed()
                choice = self.view.select_player(players)
        while not_selected:
            if int(choice) in range(len(players)):
                not_selected = False
            else:
                self.view.incorrect_selection()
                self.get_player()
        self.player = Player(players[int(choice)], scores[int(choice)])
        self.menu()

    def menu(self):
        possible_choices = [1, 2]
        choice = self.view.select_menu(self.player)
        integer = False
        while not integer:
            try:
                int(choice)
                integer = True
            except ValueError:
                self.view.value_needed()
                choice = self.view.select_menu(self.player)

        while int(choice) not in possible_choices:
            self.view.incorrect_selection()
            self.menu()
        if int(choice) == 1:
            self.new_game()
        elif int(choice) == 2:
            exit()

    def new_game(self):
        trials = NB_COUPS
        word = random.choice(self.words)
        player_word_list = ["*" for _ in word]
        player_word = ''.join(player_word_list)
        letters = []
        while trials > 0 and '*' in player_word_list:
            not_selected = True
            letter = self.view.letter_choice(player_word, trials, error=None)
            while not_selected:
                if len(letter) != 1:

                    letter = self.view.letter_choice(player_word, trials, error=1)
                elif letter.isdigit():

                    letter = self.view.letter_choice(player_word, trials, error=2)
                elif letter in letters:

                    letter = self.view.letter_choice(player_word, trials, error=3)
                else:
                    not_selected = False

            if letter in word:
                indexs = []
                ind = 0
                for let in word:
                    if letter == let:
                        indexs.append(ind)
                    ind += 1

                for index in indexs:
                    player_word_list[index] = letter
                    player_word = ''.join(player_word_list)
            else:
                self.view.wrong_letter()
                trials -= 1
            letters.append(letter)

        if "*" not in player_word:
            self.player.score += trials
            self.view.victory(self.player, word)

        else:
            new_score = self.player.score - 8
            if new_score < 0:
                self.player.score = 0
            self.view.defeat(word, self.player.score)

        self.scores.save_scores(self.player.__dict__)

        self.menu()



