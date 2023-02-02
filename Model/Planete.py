from DataAccess import PlaneteDataAccess

class Planete():
    planete = ""
    prix = 0.0
    retourTerre = 0
    satellite = {}
    asSatellite = False

    def GetPrix(self):
        return self.prix

    def GetRetourTerrePrix(self):

        return self.retourTerre

    def GetSatellites(self):
        return self.satellite

    def add(self,val):
        self.prix += float(val)

    def GetRecette(self):

        if self.prix < 10**10: #si prix total inferieur a 10 Milliards
            return self.prix * 1.5 #benefice de 50%

        elif self.prix >= 10**10 and self.prix < 10**11:# si prix total superieur a 10 Milliard et inferieur a 100 Milliard
            return self.prix * 1.25 #benefice de 25%

        elif self.prix >= 10**11 and self.prix < 10**12: # si entre 100Milliards et 1 Billiard
            return self.prix #benefice de 0
        else :
            return self.prix * 0.75 # plus de 1 Billiard => -25% de benef

class PlaneteLointaine(Planete):
    survol = 0
    orbite = 0
    sonde = 0
    rover = 0

    def __init__(self):
        self.planete = "Autre"
        data = PlaneteDataAccess.GetPrixPlanete(self.planete)

        for row in data:

            self.prix=row[0]
            self.orbite = row[1]
            self.sonde = row[2]
            self.rover = row[3]
            self.retourTerre = row[4]
            self.survol = row[5]


    def GetSurvol(self):
        return self.survol

    def GetOrbite(self):
        return self.orbite

    def GetSonde(self):
        return self.sonde

    def GetRover(self):
        return self.rover



class PlaneteTerre(Planete):
    sub = 0
    orbiteBas = 0
    orbiteHaut = 0
    Docking = 0
    volHabitee = 0
    placeSup = 0

    def __init__(self):
        self.planete = "Terre"

        data = PlaneteDataAccess.GetPrixPlanete(self.planete)

        for row in data:
            self.prix=row[0]
            self.sub = row[1]
            self.orbiteBas = row[2]
            self.orbiteHaut = row[3]
            self.docking = row[4]
            self.retourTerre = row[5]
            self.volHabitee = row[6]
            self.placeSup = float(row[7])

    def GetSuborbital(self):
        return self.sub

    def GetOrbiteH(self):
        return self.orbiteHaut

    def GetOrbiteB(self):
        return self.orbiteBas

    def GetDocking(self):
        return self.docking

    def GetHabitee(self):
        return self.volHabitee

    def GetPlaceSup(self):
        return self.placeSup



class PlaneteClassique(Planete):
    survol = 0
    orbite = 0
    sonde = 0
    rover = 0
    volHabitee = 0
    placeSup = 0

    def __init__(self,planete):
        self.planete = planete

        data = PlaneteDataAccess.GetPrixPlanete(self.planete)

        for row in data:

            self.prix=row[0]
            self.orbite = row[1]
            self.sonde = row[2]
            self.rover = row[3]
            self.retourTerre = row[4]
            self.volHabitee = row[5]
            self.placeSup = float(row[6])
            self.survol = row[7]

    def GetSurvol(self):
        return self.survol

    def GetOrbite(self):
        return self.orbite

    def GetSonde(self):
        return self.sonde

    def GetRover(self):
        return self.rover

    def GetHabitee(self):
        return self.volHabitee

    def GetPlaceSup(self):
        return self.placeSup
