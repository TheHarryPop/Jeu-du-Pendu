import pickle


class Database:

    def __init__(self):
        self.scores = self.load_scores()

    @staticmethod
    def load_scores():
        try:
            with open("scores", 'rb') as fichier:
                mon_unpickler = pickle.Unpickler(fichier)
                return mon_unpickler.load()
        except:
            return {}

    def save_scores(self, scores_dict):
        player = {scores_dict['name']: scores_dict['score']}
        self.scores.update(player)
        with open("scores", 'wb') as fichier:
            mon_pickler = pickle.Pickler(fichier)
            mon_pickler.dump(self.scores)


if __name__ == '__main__':
    pass
