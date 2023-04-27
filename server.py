# -*- coding: utf-8 -*-
from flask import Flask, redirect, request, render_template, jsonify, abort
from flask_cors import CORS
import random
import mysql.connector
app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
    host="localhost",
    user="IMAC",
    password="IMAC@2025@3490",
    database="PokIMAC"
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ajoutDresseur")  # exemple de route
def index():
    mycursor = mydb.cursor()
    """
    blabla code dans le DB
    """
    mycursor.close()
    return render_template("pageAjoutDresseur.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
