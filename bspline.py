from geomdl import utilities
import numpy as np
degree = 4
Ncpts = 9

ti = utilities.generate_knot_vector(degree,Ncpts+1)



P = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,51,52,53,54,55,56,57,58,59,60]


def getABsis(cpt,ti,t):
    if t>=ti[cpt] and t<ti[cpt+1]:
        return 1
    else:
        return 0

Nij=np.zeros([len(P),Ncpts+2+degree,degree+1])

for deg in range(degree+1):
    if deg == 0:
        for cpt in range(Ncpts+degree+1):
            for pt,t in enumerate(P):
                Nij[pt][cpt][deg] = getABsis(cpt,ti,t/P[-1])
    else:
        for cpt in range(Ncpts+degree+2-deg):
            for pt,t in enumerate(P):
                try:
                    LEFT = (t/P[-1] - ti[cpt]) / (ti[cpt+deg]-ti[cpt])
                    RIGHT = (ti[cpt+deg+1] - t/P[-1]) / (ti[cpt+deg+1]-ti[cpt+1])
                    Nij[pt][cpt][deg] = LEFT*Nij[pt][cpt][deg-1] + RIGHT*Nij[pt][cpt+1][deg-1]
                except ZeroDivisionError:
                    Nij[pt][cpt][deg] = 0


a= Nij[...,2]
pass







