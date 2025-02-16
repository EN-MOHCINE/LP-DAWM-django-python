class Etudiant:
    def __init__(self, matricule, nom, prenom, genre, note):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.note = note

    def nom_complet(self):
        return self.nom + " " + self.prenom

    def genre_entier(self):
        if self.genre == 'M':
            return 'Masculin'
        else:
            return 'Feminin'

    def mention(self):
        if self.note>=16:
            return 'Tres Bien'
        elif self.note>=14:
            return 'Bien'
        elif self.note>=12:
            return 'Assez Bien'
        elif self.note>=10:
            return 'Passable'
        else:
            return 'Insuffisant'
