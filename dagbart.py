class person():
    soort = 'mens'
    def __init__(self, voornaam, naam):
        self.voornaam = voornaam
        self.naam = naam

    def geef_naam(self):
        return self.naam

    def __str__(self):
        return self.voornaam + " " + self.naam

    def isBart(self):
        return self.voornaam.lower()== 'bart'

bart = person('bart','vanparys')
print(bart.isBart())
print(bart)
