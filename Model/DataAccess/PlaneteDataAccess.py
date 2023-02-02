import sqlite3
import os.path

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