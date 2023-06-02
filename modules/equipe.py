# -*- coding: utf-8 -*-
import modules.db as db


def afficherEquipe():
    affichage_equipe = []
    mycursor = db.mydb.cursor()
    mycursor.execute(db.requestSelectAll("equipe_dresseurs"))
    myresult = mycursor.fetchall()

    for x in myresult:
        x = list(x)
        affichage_equipe.append(x)

    mycursor.close()
    return affichage_equipe


def ajouterEquipe(pokimac):
    print(pokimac["nom"])
    mycursor = db.mydb.cursor()
    mycursor.execute(
        """INSERT INTO equipe_dresseurs (nom) VALUES (%s)""", (pokimac["nom"],))
    db.mydb.commit()
    mycursor.close()
    print("Redirecting to /PokimacEquipe")


def supprimerEquipe(id):
    mycursor = db.mydb.cursor()
    mycursor.execute("""DELETE FROM equipe_dresseurs WHERE id=%s""", [id])
    db.mydb.commit()
    mycursor.close()


def modifierEquipe(id):
    print("cc on modifie")
