# Jeu du Pendu

Un jeu du pendu bien connu de tous !

### Installation et Lancement :

```bash
$ git clone https://github.com/TheHarryPop/Jeu_du_Pendu.git
$ cd Jeu_du_Pendu
$ python3 -m venv env (Sous Windows => python -m venv env)
$ source env/bin/activate (Sous Windows => env\Scripts\activate)
$ python main.py
```

### Personnalisation :

Dans le fichier *controller.py* :

- il est possible de modifier le nombre de coups possibles :
```python
NB_COUPS = 8
```

- il est possible d'ajouter des mots dans la liste :
```python
MOTS = [
    '...',
    '...',
]   
```

### Sauvegarde :

Votre profil ainsi que votre score sont sauvegardés automatiquement dans le fichier *scores*

### A venir :

Une interface graphique est en préparation 