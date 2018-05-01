import functions_fehlerfortpflanzung.py as ff
from sympy import*
from sympy import init_printing
import pylab as py
init_printing(use_latex=True)





### Werte importieren ###

x, y, z = symbols('x y z')
f = x**3 + y



def get_Spalten():
    return 5
def get_Zeilen():
    return 5

spalte = [0,42,42,21,21,4,2,241,21,4,2,22]
### Werte analysieren ###

for j in range(0,zahl_spalten):
    #HIER WEITER
mittelwert = ff.get_mittelwert(spalte)
standardabweichung = ff.get_standardabweichung(spalte,mittelwert)
s_d_m = ff.get_standardabweichung_mittelwert(spalte,standardabweichung)
v_d_m = ff.get_vertrauensabweichung_mittelwert(spalte,standardabweichung)








#Form: Name1,Mittelwert1,Standardabweichung1,Standardabweichung des Mittelwertes1,Vertrauensabweichung des Mittelwertes1...
info = ["x",1,1,1,1, "y",2,1,4,5]

### Berechnung_Ungenauigkeit ###
u_y = 0
for k in range(0,int(len(info)/5)):
    diff_f = diff(f, info[k*5])
    diff_f = lambdify(info[k*5],diff_f)
    diff_f_wert = diff_f(info[(k*5)+1])
    u_y = u_y + abs(diff_f_wert * info[(k*5)+2])


print(u_y)

    



