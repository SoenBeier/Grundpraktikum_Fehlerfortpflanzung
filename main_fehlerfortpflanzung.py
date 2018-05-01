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


alle_werte = [[1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,2,4,5,1],[2,4,5]]
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
    diff_f = diff(f, info[k*5])
    diff_f = lambdify(info[k*5],diff_f)
    diff_f_wert = diff_f(info[(k*5)+1])
    u_y = u_y + abs(diff_f_wert * info[(k*5)+2])


print(u_y)

    



