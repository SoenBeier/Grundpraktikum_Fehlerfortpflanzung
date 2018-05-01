# -*- coding: utf-8 -*-
"""
Created on Tue May  1 17:58:01 2018

@authors: S.H.B, J.S
"""
from sympy import*
import pylab as py

### Berechnung des Studentenfaktors ###
def get_t(anzahl_werte): 
    if anzahl_werte <= 3:
        t = 1.32
    elif anzahl_werte <= 5:
        t = 1.15
    elif anzahl_werte <= 6:
        t = 1.11
    elif anzahl_werte <= 10:
        t = 1.06
    else:
        t = 1
    return t


### Berechnung Mittelwert ###

def get_mittelwert(werte):
    mittelwert = 0
    for i in range (0,len(werte)):
        mittelwert = mittelwert + werte[i]
    mittelwert = mittelwert / len(werte)
    return mittelwert
### Berechnung Standardabweichung ###

def get_standardabweichung(werte, mittelwert):
    s = 0
    for i in range(0,len(werte)):
        s = s + (werte[i] - mittelwert)**2
    s = py.sqrt(1/(len(werte)-1) * s)
    return s
        
### Berechnung Standardabweichung des Mittelwertes ###

def get_standardabweichung_mittelwert(werte, standardabweichung):
    sdm = standardabweichung / py.sqrt(len(werte))
    return sdm

### Berechnung Vertrauensabweichung des Mittelwertes ###

def get_vertrauensabweichung_mittelwert(werte,standardabweichung):
    vdm = get_t(len(werte)) * standardabweichung / py.sqrt(len(werte))
    return vdm
    
    
    
    
    