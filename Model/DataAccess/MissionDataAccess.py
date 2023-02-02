from asyncore import read
from multiprocessing.sharedctypes import Value
import sqlite3
import os.path
import Model.Planete as Planete

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