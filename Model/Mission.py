from asyncore import read
import datetime
from multiprocessing.sharedctypes import Value
import sqlite3
import os.path
import Model.Planete as Planete
from DataAccess import MissionDataAccess #a rectifier

def convert(val):

    if val >= 1000000000:
        val = "{} Milliard".format(val/1000000000)
    elif val < 1000000000 : 
        val = "{} Million".format(val/1000000)
    return val
    
class Mission():
    nomPlanete = MissionDataAccess.GetNomPlanete()
    nomPlaneteSat = MissionDataAccess.GetNomPlaneteSat()
    nomSat = MissionDataAccess.GetNomSat()
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
        planete = MissionDataAccess.GetNomPlaneteBySat(sat)
        self.cible = sat
        self.SetPlanete(planete)
        self.objectifPlanete.add(MissionDataAccess.GetSatPrice(sat))
        

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