from sympy import*
from sympy import init_printing
import pylab as py
init_printing(use_latex=True)
import functions_fehlerfortpflanzung as ff



### Werte importieren ###

x, y, z = symbols('x y z')
f = x**3 + 2 * y + z**2



def get_Spalten():
    return 5
def get_Zeilen():
    return 5

data = np.loadtxt('asdf.dat')# Daten aus einfacher Textdatei laden. Hier einfach namen der dat datei einfügen.
numrows = len(data[:,1])
numcolumns = len(data[1,:])
liste = []
for i in range(0,numcolumns):
    hans = []
    liste.append(hans)
    for k in range(0,numrows):
        hans.append(data[k,i])

alle_werte = [[1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,2,4,5,1],[2,4,5]]
# !alle_werte=liste! <- kann man auf die Liste setzen um auf die Werte der dat datei zugreifen zu können. 
variabeln = ["x","y","z"]
info = []
### Werte analysieren ###

for j in range(0,len(alle_werte)):
    #HIER WEITER
    variabel = variabeln[j]
    mittelwert = ff.get_mittelwert(alle_werte[j])
    standardabweichung = ff.get_standardabweichung(alle_werte[j],mittelwert)
    s_d_m = ff.get_standardabweichung_mittelwert(alle_werte[j],standardabweichung)
    v_d_m = ff.get_vertrauensabweichung_mittelwert(alle_werte[j],standardabweichung)
    info_neu = [variabel,mittelwert,standardabweichung,s_d_m,v_d_m]
    info = info + info_neu

print("Reihenfolge: Variabel, Mittelwert, Standardabweichung, S_d_M, V_d_M:", info)


#Form: Name1,Mittelwert1,Standardabweichung1,Standardabweichung des Mittelwertes1,Vertrauensabweichung des Mittelwertes1...
#info = ["x",1,1,1,1, "y",2,1,4,5]

### Berechnung_Ungenauigkeit ###
u_y = 0

for k in range(0,int(len(info)/5)):
    #f nach einer der Variabel ableiten
    diff_f = diff(f, info[k*5])
    
    print()
    print("diff(f nach", info[k*5], "): ", diff_f, "mit", info[k*5],"=",info[k*5+1],"(Mittelwert)")
    
    #Mittelwert in abgeleitete Funktion einsetzen und berechnen
    diff_f = lambdify(info[k*5],diff_f) #info[k*5] = Name der Variabel
    diff_f_wert = diff_f(info[(k*5)+1]) #info[(k*5)+1] = Mittelwert
    
    print("u_",info[k*5],": ",info[k*5+2])
    print("(",k,"):","|",diff(f, info[k*5]),"*","u_",info[k*5],"|","=",abs(diff_f_wert * info[(k*5)+2]))
    
    #ausgerechneter Wert mit der Standardabweichung multiplizieren und mit dem bisherigem u_y addieren
    u_y = u_y + abs(diff_f_wert * info[(k*5)+2]) #info[(k*5)+2] = Standardabweichung
    

print()
print("u_y =", u_y, ("((1),(2),(3),(4).... addiert)"))

    



