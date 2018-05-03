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
    
def Graph(mittelwert,s_d_m,v_d_m,alle_werte):
    x=py.linspace(-1,0.1,len(alle_werte[1]))
    y=(x/x)*mittelwert 
    s_d_m1=(x/x)*(s_d_m+mittelwert)
    s_d_m2=(x/x)*(mittelwert-s_d_m)
    v_d_m1=(x/x)*(v_d_m+mittelwert)
    v_d_m2=(x/x)*(mittelwert-v_d_m)
    fig,ax = py.subplots(ncols=1,nrows=1,num="Auswertung",figsize=(16,9))
    ax.set_title("Auswertung",fontsize=20)
    ax.plot(y,'-',label='Mittelwert',color="blue")   
    ax.plot(s_d_m1,'--',label="$\sigma$-Standartabweichung",color="red")
    ax.plot(s_d_m2,'--',label="$\sigma$-Standartabweichung",color="red")
    ax.plot(v_d_m1,'--',label="Vertrauensintervall",color="green")
    ax.plot(v_d_m2,'--',label="Vertrauensintervall",color="green")
    ax.plot(alle_werte[1],'+',label='Alle Werte',color="orange")
    py.xlabel('t in s',fontsize=20)
    py.ylabel('Messwerte',fontsize=20)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    ax.legend(bbox_to_anchor=(1, 1))
    fig.savefig("Auswertung.png",dpi=600)
   
