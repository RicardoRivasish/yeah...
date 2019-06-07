#! /usr/bin/env pyhton
from pylab import * # se importa la libreria pylab
from scipy.integrate import * # se importa la libreria scipy.integrate
from numpy import * # se importa numpy
%matplotlib inline

def oscam(x,t,q,p):
    return array ((x[1],-(q**2)*x[0]-p*x[1]))
def oscam_1(x,t,q1,q2,F,p):
                   return array((x[1],F*cos(p*t)-(q1**2)*x[0]-q2*x[1]))
                 