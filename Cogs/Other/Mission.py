from asyncore import read
import datetime
from multiprocessing.sharedctypes import Value
import sqlite3
import os.path
import Cogs.Other.Planete as Planete
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
    from planete ;
    """)
    arr = []
    for rows in cur:
        for row in rows:
            arr.append(row)
    
    return arr

def GetNomSat(): 
    cur.execute("""
    select satelite_nom 
    from satelite ;
    """)
    arr = []
    for rows in cur:
        for row in rows:
            arr.append(row)
    
    return arr

def GetNomPlaneteSat(): 
    cur.execute("""
    select planete.nom_planete  
    from satelite, planete
    where satelite.planete_id = planete.id;
    """)
    arr = []
    for rows in cur:
        for row in rows:
            arr.append(row)
    
    return arr

def GetNomPlaneteBySat(sat): 
    cur.execute("""
    select planete.nom_planete  
    from satelite, planete
    where satelite.planete_id = planete.id
    and satelite_nom  = \'{}\';
    """.format(sat))
    return str(cur.fetchone()[0])

def GetSatPrice(sat):
    cur.execute("""
    select prix 
    from satelite 
    where satelite_nom =  \'{}\';
    """.format(sat))
    return float(cur.fetchone()[0])

def convert(val):

    if val >= 1000000000:
        val = "{} Milliard".format(val/1000000000)
    elif val < 1000000000 : 
        val = "{} Million".format(val/1000000)
    return val


#endregion


class Mission():
    nomPlanete = GetNomPlanete()
    nomPlaneteSat = GetNomPlaneteSat()
    nomSat = GetNomSat()
    planete = ""
    cible = ""
    objectifPlanete = None
    objectifMultiple = False # Les objectif eligibles au calcul : survol / docking / orbite / Sonde / Rover ( la vrai technique serait de commencer par le plus cher de tous, et de diviser par 2 les couts d'options ds autres)
    altChoisie = False
    Retour = False
    Habitee = False

    def SetPlanete(self, planete):
        self.planete = planete
        if self.cible == "":
            self.cible = planete
        if planete == "Terre":
            self.objectifPlanete = Planete.PlaneteTerre()

        elif planete == "Autre":
            self.objectifPlanete = Planete.PlaneteLointaine()

        else: 
            self.objectifPlanete = Planete.PlaneteClassique(self.planete)
             

    def SetPlaneteBySat(self,sat):
        planete = GetNomPlaneteBySat(sat)
        self.cible = sat
        self.SetPlanete(planete)
        self.objectifPlanete.add(GetSatPrice(sat))
        

    def Suborbital(self):
        
        if self.objectifMultiple :
                
            self.objectifPlanete.add(self.objectifPlanete.GetSuborbital()/2)
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetSuborbital())
        self.altChoisie = True
        
    def OrbiteHaute(self):
       
        if self.objectifMultiple :
                
            self.objectifPlanete.add(self.objectifPlanete.GetOrbiteH()/2)
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetOrbiteH())
        self.altChoisie = True

    def OrbiteBasse(self):
            
        if self.objectifMultiple :
                
            self.objectifPlanete.add(self.objectifPlanete.GetOrbiteB()/2)
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetOrbiteB())
        self.altChoisie = True

    def Orbite(self):
       
        if self.objectifMultiple :
                
            self.objectifPlanete.add(self.objectifPlanete.GetOrbite()/2)
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetOrbite())
    
    def RetourTerre(self):
        self.objectifPlanete.add(self.objectifPlanete.GetRetourTerrePrix())
        self.Retour = True

    def VolHabitee(self):
        if self.Retour :
            
            self.objectifPlanete.add(self.objectifPlanete.GetHabitee())
            self.Habitee = True

    def PlaceSup(self, nb):
        self.objectifPlanete.add(self.objectifPlanete.GetPlaceSup() * int(nb))

    def Docking(self):
        if self.objectifMultiple :
                
            self.objectifPlanete.add(self.objectifPlanete.GetDocking()/2)
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetDocking())
            
    def Sonde(self):
        if self.objectifMultiple:
            self.objectifPlanete.add(self.objectifPlanete.GetSonde() /2 )
        else :
            self.objectifMultiple = True
            self.objectifPlanete.add(self.objectifPlanete.GetSonde())

    def Rover(self):
       
        self.objectifMultiple = True
        self.objectifPlanete.add(self.objectifPlanete.GetRover())

    def Satellite(self): 
        return None
        #if self.objectifPlanete.asSatellite:
        #self.objectifPlanete.add(data.get(id[x-1]))

    def GetPrix(self):
        return self.objectifPlanete.GetPrix()

    def GetRecette(self):
        return self.objectifPlanete.GetRecette()

    def GetRDTime(self):
        return datetime.datetime(2100,10,1) - datetime.datetime.now().day




