# -*- coding: utf-8 -*-
"""
Created on Tue May  1 19:23:39 2018

@author: Julian
"""

from pylab import *
import pandas as pd   # fuer die Darstellung der Messergebnisse und abgeleiteten Groessen in Tabellen
import sympy as sym   # fuer die symbolische Berechnung der Ausdruecke fuer die Fehler
from IPython.display import display # Ausgabe eines Objekts im Notebook (Art der Ausgabe haengt vom Objekt ab)
from sympy import init_printing     
init_printing()                     # Rendering von Latexausdruecken im Notebook

data = np.loadtxt('test.dat')# Daten aus einfacher Textdatei laden
#Tabelle aus werten
#Erstelle die Tabelle der Messergebnisse
df = pd.DataFrame()
# df['#'] = np.array(data[:,0],dtype=int)
df["t"] = data[:,1] #nimmt werte aus der zweiten Spalte der dat datei
df["s"] = data[:,2] # nimmt werte aus der dritten Spalte der dat datei
#data[:,1],df,len(data[1,:])
numrows = len(data[:,1])
numcolumns = len(data[1,:])
liste = []
for i in range(0,numcolumns):
    liste.append(hans)
    hans = []
    for k in range(0,numrows):
        hans.append(data[k,i])

print(liste)

#lustige rumrechnerei:
M = df["t"]+df["s"]
df["M"]=M

#M in die dat schreiben: bzw. Tabelle Exportieren
#df.to_excel("test_1.xls")
