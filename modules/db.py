# -*- coding: utf-8 -*-
import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="IMAC",
    password="IMAC@2025@3490"
)


def requestInsert(table, head):
    return (
        f"INSERT IGNORE INTO {table} " +
        f"({', '.join([f'{_}' for _ in head])})"+" VALUES "
        + f"""({', '.join([f'%s' for _ in head])});"""
    )


def requestSelectAll(table):
    return f"SELECT * FROM {table}; "


def initDB(filename, db):
    file = open(filename, mode='r', encoding='utf-8-sig')
    csv_data = csv.reader(file)
    header = {}
    mycursor = mydb.cursor()
    skipHeader = True
    for row in csv_data:
        if skipHeader:
            header = row[0].split(";")
            skipHeader = False
            continue
        args = row[0].split(';')
        requete = requestInsert(db, header)
        mycursor.execute(requete, args)
    mydb.commit()
    mycursor.close()


if (mydb.is_connected()):  # Création de la DB et des tables si besoin
    print("Connected")
    with open('./static/init.sql', 'r') as sql_file:
        mycursor = mydb.cursor()
        result_iterator = mycursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            pass
        mydb.commit()
        mycursor.close()
        initDB('./static/csv/pokemons.csv', 'pokemons')
        initDB('./static/csv/types.csv', 'types')
else:
    print("Not connected")


def requestSelect_From(table, column, where, value):
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT {column} FROM {table} WHERE {where}='{value}';")
    result = cursor.fetchone()
    cursor.close()
    return result[0]


def requestSelectColumn(table, column, where="", value="", condition=False):
    cursor = mydb.cursor()
    if (condition):
        cursor.execute(
            f"SELECT {column} FROM {table} WHERE {where}='{value}';")
    else:
        cursor.execute(f"SELECT {column} FROM {table};")
    result = cursor.fetchall()
    cursor.close()
    return result


if (mydb.is_connected()):  # Création de la DB et des tables si besoin
    print("Connected")
    with open('./static/init.sql', 'r') as sql_file:
        mycursor = mydb.cursor()
        result_iterator = mycursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            pass
        mydb.commit()
        mycursor.close()
        initDB('./static/csv/pokemons.csv', 'pokemons')
        initDB('./static/csv/types.csv', 'types')
else:
    print("Not connected")
