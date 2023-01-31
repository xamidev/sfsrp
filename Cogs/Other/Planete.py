import sqlite3
import os.path
#region def

try:
    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "sqlite.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()


except sqlite3.Error as error:
    print("Failed to read data from sqlite table", error)


def GetNomPlanete(): 
    cur.execute("""
    select nom_planete 
    from planete 
    """)
    arr = []
    for rows in cur:
        for row in rows:
            arr.append(row)
    
    return arr

def GetPrixPlanete(planete): # recuperation des datas des planetes

    if planete == "Terre":
        cur.execute("""
        select prix, suborbital_prix,orbite_basse_prix,orbite_haute_prix,retour_terre_prix,docking_prix,mission_habite_prix,place_sup_prix 
        from planete 
        where nom_planete = \'Terre\';
        """)
        
        

    elif planete == "Autre":
        cur.execute("""
        select prix, orbite_prix,sonde_prix,rover_prix,retour_terre_prix,survol_prix 
        from planete
        where nom_planete = \'{}\';
        """.format(planete))
   
        
    
    else :
        cur.execute("""
        select prix, orbite_prix,sonde_prix,rover_prix,retour_terre_prix,mission_habite_prix,place_sup_prix,survol_prix
        from planete 
        where nom_planete = \'{}\';
        """.format(planete))
    
    return cur

def GetNomPlaneteSat():
    cur.execute("""
    select nom_planete 
    from satelite, planete
    where satelite.planete_id = planete.id 
    """)
    arr = []
    for rows in cur:
        for row in rows:
            arr.append(row)
    return arr

#endregion



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
        
        if self.prix < 1000000000: # si prix total inferieur a 1 Milliard
            return self.prix + (self.prix / 2)# benefice de 50%
            
        elif self.prix >= 1000000000 and self.prix < 100000000000:# si prix total superieur a 1 Milliard et inferieur a 100 Milliard
            return self.prix + (self.prix / 4)#benefice de 25%

        elif self.prix >= 100000000000 and self.prix < 1000000000000: # si entre 100Milliard et 1 Billiard
            return self.prix # benefice de 0
        else :
            return self.prix -(self.prix/4) # plus de 1 Billiard => -25% de benef
        




class PlaneteLointaine(Planete):
    survol = 0
    orbite = 0
    sonde = 0
    rover = 0

    def __init__(self):
        self.planete = "Autre"
        data = GetPrixPlanete(self.planete)

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

        data = GetPrixPlanete(self.planete)

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

        data = GetPrixPlanete(self.planete)

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
