# -*- coding: utf-8 -*-
"""Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, 2017, 2018, 2019, 2020 Caleb Bell
<Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from numpy.testing import assert_allclose
import pytest
from math import *
from chemicals.iapws import *
from fluids.numerics import assert_close, linspace, logspace, derivative
from chemicals.iapws import REGION_3A, REGION_3B, REGION_3C, REGION_3D, REGION_3E, REGION_3F, REGION_3G, REGION_3H, REGION_3I, REGION_3J, REGION_3K, REGION_3L, REGION_3M, REGION_3N, REGION_3O, REGION_3P, REGION_3Q, REGION_3R, REGION_3S, REGION_3T, REGION_3U, REGION_3V, REGION_3W, REGION_3X, REGION_3Y, REGION_3Z
from chemicals.vapor_pressure import Psat_IAPWS


### IAPWS Naive Functions
### Regoin 1
nis1 = [0.14632971213167, -0.84548187169114, -0.37563603672040E1,
       0.33855169168385E1, -0.95791963387872, 0.15772038513228,
       -0.16616417199501E-1, 0.81214629983568E-3, 0.28319080123804E-3,
       -0.60706301565874E-3, -0.18990068218419E-1, -0.32529748770505E-1,
       -0.21841717175414E-1, -0.52838357969930E-4, -0.47184321073267E-3,
       -0.30001780793026E-3, 0.47661393906987E-4, -0.44141845330846E-5,
       -0.72694996297594E-15, -0.31679644845054E-4, -0.28270797985312E-5,
       -0.85205128120103E-9, -0.22425281908000E-5, -0.65171222895601E-6,
       -0.14341729937924E-12, -0.40516996860117E-6, -0.12734301741641E-8,
       -0.17424871230634E-9, -0.68762131295531E-18, 0.14478307828521E-19,
       0.26335781662795E-22, -0.11947622640071E-22, 0.18228094581404E-23,
       -0.93537087292458E-25]
lis1 = [0., 0., 0., 0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1., 2., 2., 2., 2., 2., 3., 3., 3., 4., 4., 4., 5., 8., 8., 21., 23., 29., 30., 31., 32.]
lis1 = [int(i) for i in lis1]
Jis1 = [-2., -1., 0., 1., 2., 3., 4., 5., -9., -7., -1., 0., 1., 3., -3., 0., 1., 3., 17., -4., 0., 6., -5., -2., 10., -8., -11., -6., -29., -31., -38., -39., -40., -41.]
Jis1 = [int(i) for i in Jis1]


def iapws97_G_region1_naive(tau, pi):
    return sum([nis1[i]*(7.1-pi)**lis1[i]*(tau-1.222)**Jis1[i] for i in range(34)])

def iapws97_dG_dpi_region1_naive(tau, pi):
    return sum([-nis1[i]*lis1[i]*(7.1-pi)**(lis1[i]-1)*(tau-1.222)**Jis1[i] for i in range(34)])

def iapws97_d2G_d2pi_region1_naive(tau, pi):
    return sum([nis1[i]*lis1[i]*(lis1[i]-1)*(7.1-pi)**(lis1[i]-2)*(tau-1.222)**Jis1[i] for i in range(34)])

def iapws97_dG_dtau_region1_naive(tau, pi):
    return sum([nis1[i]*Jis1[i]*(7.1-pi)**lis1[i]*(tau-1.222)**(Jis1[i]-1) for i in range(34)])

def iapws97_d2G_d2tau_region1_naive(tau, pi):
    return sum([nis1[i]*Jis1[i]*(Jis1[i]-1)*(7.1-pi)**lis1[i]*(tau-1.222)**(Jis1[i]-2) for i in range(34)])

def iapws97_d2G_dpidtau_region1_naive(tau, pi):
    return sum([-nis1[i]*Jis1[i]*lis1[i]*(7.1-pi)**(lis1[i]-1)*(tau-1.222)**(Jis1[i]-1) for i in range(34)])

### Region 2
# Section 2 - ideal gas part
J0is2 = [0., 1., -5., -4., -3., -2., -1., 2., 3.]
J0is2 = [int(i) for i in J0is2]

def iapws97_G0_region2_naive(tau, pi):
    return log(pi) + sum( [n0is2[i]*tau**J0is2[i] for i in range(9)] )

def iapws97_dG0_dtau_region2_naive(tau, pi):
    return sum([n0is2[i]*J0is2[i]*tau**(J0is2[i]-1) for i in range(9)])

def iapws97_d2G0_d2tau_region2_naive(tau, pi):
    return sum([n0is2[i]*J0is2[i]*(J0is2[i]-1)*tau**(J0is2[i]-2) for i in range(9)])

n0is2 = [-0.96927686500217E1, 0.10086655968018E2, -0.56087911283020E-2,
        0.71452738081455E-1, -0.40710498223928, 0.14240819171444E1,
        -0.43839511319450E1, -0.28408632460772, 0.21268463753307E-1]
# Section 2 - residual part

lis2 = [1., 1., 1., 1., 1., 2., 2., 2., 2., 2., 3., 3., 3., 3., 3., 4., 4., 4.,
        5., 6., 6., 6., 7., 7., 7., 8., 8., 9., 10., 10., 10., 16., 16., 18.,
        20., 20., 20., 21., 22., 23., 24., 24., 24.]
lis2 = [int(i) for i in lis2]
Jis2 = [0., 1., 2., 3., 6., 1., 2., 4., 7., 36., 0., 1., 3., 6., 35., 1., 2.,
        3., 7., 3., 16., 35., 0., 11., 25., 8., 36., 13., 4., 10., 14., 29.,
        50., 57., 20., 35., 48., 21., 53., 39., 26., 40., 58.]
Jis2 = [int(i) for i in Jis2]
nis2 = [-0.17731742473213E-2, -0.17834862292358E-1, -0.45996013696365E-1,
        -0.57581259083432E-1, -0.50325278727930E-1, -0.33032641670203E-4,
        -0.18948987516315E-3, -0.39392777243355E-2, -0.43797295650573E-1,
        -0.26674547914087E-4, 0.20481737692309E-7, 0.43870667284435E-6,
        -0.32277677238570E-4, -0.15033924542148E-2, -0.40668253562649E-1,
        -0.78847309559367E-9, 0.12790717852285E-7, 0.48225372718507E-6,
        0.22922076337661E-5, -0.16714766451061E-10, -0.21171472321355E-2,
        -0.23895741934104E2, -0.59059564324270E-17, -0.12621808899101E-5,
        -0.38946842435739E-1, 0.11256211360459E-10, -0.82311340897998E1,
        0.19809712802088E-7, 0.10406965210174E-18, -0.10234747095929E-12,
        -0.10018179379511E-8, -0.80882908646985E-10, 0.10693031879409,
        -0.33662250574171, 0.89185845355421E-24, 0.30629316876232E-12,
        -0.42002467698208E-5, -0.59056029685639E-25, 0.37826947613457E-5,
        -0.12768608934681E-14, 0.73087610595061E-28, 0.55414715350778E-16,
        -0.94369707241210E-6]

def iapws97_Gr_region2_naive(tau, pi):
    return sum([nis2[i]*pi**lis2[i]*(tau-0.5)**Jis2[i] for i in range(43)])

def iapws97_dGr_dpi_region2_naive(tau, pi):
    return sum([nis2[i]*lis2[i]*pi**(lis2[i]-1)*(tau-0.5)**Jis2[i] for i in range(43)])

def iapws97_d2Gr_d2pi_region2_naive(tau, pi):
    return sum([nis2[i]*lis2[i]*(lis2[i]-1)*pi**(lis2[i]-2)*(tau-0.5)**Jis2[i] for i in range(43)])

def iapws97_dGr_dtau_region2_naive(tau, pi):
    return sum([nis2[i]*pi**lis2[i]*Jis2[i]*(tau-0.5)**(Jis2[i]-1) for i in range(43)])

def iapws97_d2Gr_d2tau_region2_naive(tau, pi):
    return sum([nis2[i]*pi**lis2[i]*Jis2[i]*(Jis2[i]-1)*(tau-0.5)**(Jis2[i]-2) for i in range(43)])

def iapws97_d2Gr_dpidtau_region2_naive(tau, pi):
    return sum([nis2[i]*lis2[i]*pi**(lis2[i]-1)*Jis2[i]*(tau-0.5)**(Jis2[i]-1) for i in range(43)])

### Region 3
# Section 3 - In terms of density
lis3 = [None, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
        3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11]
Jis3 = [None, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2,
        4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26]
nis3 = [0.10658070028513E1, -0.15732845290239E2, 0.20944396974307E2,
        -0.76867707878716E1, 0.26185947787954E1, -0.28080781148620E1,
        0.12053369696517E1, -0.84566812812502E-2, -0.12654315477714E1,
        -0.11524407806681E1, 0.88521043984318, -0.64207765181607,
        0.38493460186671, -0.85214708824206, 0.48972281541877E1,
        -0.30502617256965E1, 0.39420536879154E-1, 0.12558408424308,
        -0.27999329698710, 0.13899799569460E1, -0.20189915023570E1,
        -0.82147637173963E-2, -0.47596035734923, 0.43984074473500E-1,
        -0.44476435428739, 0.90572070719733, 0.70522450087967,
        0.10770512626332, -0.32913623258954, -0.50871062041158,
        -0.22175400873096E-1, 0.94260751665092E-1, 0.16436278447961,
        -0.13503372241348E-1, -0.14834345352472E-1, 0.57922953628084E-3,
        0.32308904703711E-2, 0.80964802996215E-4, -0.16557679795037E-3,
        -0.44923899061815E-4]

def iapws97_A_region3_naive(tau, delta):
    return nis3[0]*log(delta) + sum([nis3[i]*delta**lis3[i]*tau**Jis3[i] for i in range(1, 40)])

def iapws97_dA_ddelta_region3_naive(tau, delta):
    return (nis3[0]/delta + sum([nis3[i]*lis3[i]*delta**(lis3[i]-1)*tau**Jis3[i] for i in range(1, 40)]))

def iapws97_d2A_d2delta_region3_naive(tau, delta):
    return (-nis3[0]/delta**2 + sum([nis3[i]*lis3[i]*(lis3[i]-1)*delta**(lis3[i]-2)*tau**Jis3[i] for i in range(1, 40)]))

def iapws97_dA_dtau_region3_naive(tau, delta):
    return (sum([nis3[i]*Jis3[i]*delta**lis3[i]*tau**(Jis3[i]-1) for i in range(1, 40)]))

def iapws97_d2A_d2tau_region3_naive(tau, delta):
    return (sum([nis3[i]*Jis3[i]*(Jis3[i]-1)*delta**lis3[i]*tau**(Jis3[i]-2) for i in range(1, 40)]))

def iapws97_d2A_ddeltadtau_region3_naive(tau, delta):
    return (sum([nis3[i]*lis3[i]*Jis3[i]*delta**(lis3[i]-1)*tau**(Jis3[i]-1) for i in range(1, 40)]))

### Region 5
# Section 5 - ideal gas part
J0is5 = [0., 1., -3., -2., -1., 2.]
n0is5 = [-0.13179983674201E2, 0.68540841634434E1, -0.24805148933466E-1,
        0.36901534980333, -0.31161318213925E1, -0.32961626538917]
# Section 5 - residual part
lis5 = [1, 1, 1, 2, 2, 3]
Jis5 = [1, 2, 3, 3, 9, 7]
nis5 = [0.15736404855259E-2, 0.90153761673944E-3, -0.50270077677648E-2,
        0.22440037409485E-5, -0.41163275453471E-5, 0.37919454822955E-7]

def iapws97_G0_region5_naive(tau, pi):
    return  log(pi) + sum( [n0is5[i]*tau**J0is5[i] for i in range(6)] )

def iapws97_dG0_dtau_region5_naive(tau, pi):
    return sum( [n0is5[i]*J0is5[i]*tau**(J0is5[i]-1) for i in range(6)] )

def iapws97_d2G0_d2tau_region5_naive(tau, pi):
    return sum( [n0is5[i]*J0is5[i]*(J0is5[i]-1)*tau**(J0is5[i]-2) for i in range(6)] )


def iapws97_Gr_region5_naive(tau, pi):
    return sum( [nis5[i]*pi**lis5[i]*tau**Jis5[i] for i in range(6)] )

def iapws97_dGr_dpi_region5_naive(tau, pi):
    return sum( [nis5[i]*lis5[i]*pi**(lis5[i]-1)*tau**Jis5[i] for i in range(6)] )

def iapws97_d2Gr_d2pi_region5_naive(tau, pi):
    return sum( [nis5[i]*lis5[i]*(lis5[i]-1)*pi**(lis5[i]-2)*tau**Jis5[i] for i in range(6)] )

def iapws97_dGr_dtau_region5_naive(tau, pi):
    return sum( [nis5[i]*pi**lis5[i]*Jis5[i]*tau**(Jis5[i]-1) for i in range(6)] )

def iapws97_d2Gr_d2tau_region5_naive(tau, pi):
    return sum( [nis5[i]*pi**lis5[i]*Jis5[i]*(Jis5[i]-1)*tau**(Jis5[i]-2) for i in range(6)] )

def iapws97_d2Gr_dpidtau_region5_naive(tau, pi):
    return sum( [nis5[i]*lis5[i]*pi**(lis5[i]-1)*Jis5[i]*tau**(Jis5[i]-1) for i in range(6)] )


### Fast equation fuzz tests
# check that floating points are behaving nicely
# The only two constants in this world are death and floating point error.
    
@pytest.mark.slow
def test_iapws97_region1_fuzz():
    funcs_naive = [iapws97_dG_dpi_region1_naive, iapws97_G_region1_naive, iapws97_d2G_d2pi_region1_naive,
                   iapws97_dG_dtau_region1_naive, iapws97_d2G_d2tau_region1_naive, iapws97_d2G_dpidtau_region1_naive]
    funcs_fast = [iapws97_dG_dpi_region1, iapws97_G_region1, iapws97_d2G_dpi2_region1,
                  iapws97_dG_dtau_region1, iapws97_d2G_d2tau_region1, iapws97_d2G_dpidtau_region1]
    atols = [0, 1e-14, 0, 3e-15, 0.0, 1e-16]
    rtols = [2e-13, 1e-12, 3e-12, 1e-13, 1e-12, 2e-12]

    # for testing faster
#    funcs_naive = [iapws97_d2G_dpidtau_region1_naive]
#    funcs_fast = [iapws97_d2G_dpidtau_region1]
#    atols = [1e-16]
#    rtols = [2e-12]
    
    N = 500
    Ts = linspace(273.15, 623.15, N)
    def test_Ps(T, N):
        Psat = Psat_IAPWS(T)
        return logspace(log10(Psat), log10(100e6), N)
    
    for naive, fast, rtol, atol in zip(funcs_naive, funcs_fast, rtols, atols):
        for T in Ts:
            tau = 1386.0/T
            for P in test_Ps(T, N):
                pi = P/16.53E6
                assert_close(naive(tau, pi),
                             fast(tau, pi), rtol=rtol, atol=atol)


@pytest.mark.slow
def test_iapws97_region2_fuzz():
    funcs_naive = [iapws97_d2G0_d2tau_region2_naive, iapws97_dG0_dtau_region2_naive, iapws97_G0_region2_naive, iapws97_d2Gr_dpidtau_region2_naive, iapws97_d2Gr_d2tau_region2_naive, iapws97_dGr_dtau_region2_naive, iapws97_d2Gr_d2pi_region2_naive, iapws97_Gr_region2_naive, iapws97_dGr_dpi_region2_naive]
    funcs_fast = [iapws97_d2G0_d2tau_region2, iapws97_dG0_dtau_region2, iapws97_G0_region2, iapws97_d2Gr_dpidtau_region2, iapws97_d2Gr_d2tau_region2, iapws97_dGr_dtau_region2, iapws97_d2Gr_d2pi_region2, iapws97_Gr_region2, iapws97_dGr_dpi_region2]
    atols = [0, 0, 1e-14, 0, 0, 0.0, 3e-18, 0, 0, ]
    rtols = [1e-14, 1e-14, 5e-15, 2e-14, 2e-14, 2e-15, 1e-14, 2e-15, 2e-15]
    
    N = 100
    P_lim = 1e-6
    Ts = linspace(273.15, 1073.15, N)
    def test_Ps(T, N):
        upper_P = iapws97_boundary_2_3(T)
        if T <= 623.15:
            upper_P = min(Psat_IAPWS(T), upper_P)
        
        if upper_P < P_lim or upper_P > 100e6:
            # No valid points in region 2
            return []

        return logspace(log10(P_lim), log10(upper_P), N)

    for naive, fast, rtol, atol in zip(funcs_naive, funcs_fast, rtols, atols):
#        print(fast)
        for T in Ts:
            tau = 540.0/T
            for P in test_Ps(T, N):
                pi = P/1E6
                assert_close(naive(tau, pi),
                             fast(tau, pi), rtol=rtol, atol=atol)

#test_iapws97_region2_fuzz()
                
@pytest.mark.slow
def test_iapws97_region3_fuzz():
    funcs_naive = [iapws97_d2A_ddeltadtau_region3_naive, iapws97_d2A_d2tau_region3_naive, iapws97_dA_dtau_region3_naive, iapws97_d2A_d2delta_region3_naive, iapws97_dA_ddelta_region3_naive, iapws97_A_region3_naive]
    funcs_fast = [iapws97_d2A_ddeltadtau_region3, iapws97_d2A_d2tau_region3, iapws97_dA_dtau_region3, iapws97_d2A_d2delta_region3, iapws97_dA_ddelta_region3, iapws97_A_region3]
    atols = [0, 0, 0, 1e-13, 0.0, 0, ]
    rtols = [3e-12, 1e-11, 5e-13, 1e-12, 2e-12, 5e-14]
    N = 500
    Ts = linspace(623.15, 1073.15, N)
    
    for naive, fast, rtol, atol in zip(funcs_naive, funcs_fast, rtols, atols):
#        print(fast)
        # Do some points near where more region transitions are, and then up to the limit.
        for P_lim in (25.5e6, 100e6):
            def test_Ps(T, N):
                 # Do not check too low to the boundary
                 # Sometimes CoolProp says a different region
                lower_P = iapws97_boundary_2_3(T)
                if lower_P >= P_lim:
                    # No valid points in region 3
                    return []
                upper_P = iapws97_boundary_2_3(T)*10.0
                upper_P = min(upper_P, P_lim)
                return logspace(log10(lower_P), log10(upper_P), N)
        
            for T in Ts:
                tau = 647.096/T
                for P in test_Ps(T, N):
                    rho = iapws97_rho(T, P)
                    delta = rho/322.0
                    assert_close(naive(tau, delta),
                                 fast(tau, delta), rtol=rtol, atol=atol)
#test_iapws97_region3_fuzz()
                    
@pytest.mark.slow
def test_iapws97_region5_fuzz():
    funcs_naive = [iapws97_d2G0_d2tau_region5_naive, iapws97_dG0_dtau_region5_naive, iapws97_G0_region5_naive, iapws97_d2Gr_dpidtau_region5_naive, iapws97_d2Gr_d2tau_region5_naive, iapws97_dGr_dtau_region5_naive, iapws97_d2Gr_d2pi_region5_naive, iapws97_Gr_region5_naive, iapws97_dGr_dpi_region5_naive]
    funcs_fast = [iapws97_d2G0_d2tau_region5, iapws97_dG0_dtau_region5, iapws97_G0_region5, iapws97_d2Gr_dpidtau_region5, iapws97_d2Gr_d2tau_region5, iapws97_dGr_dtau_region5, iapws97_d2Gr_d2pi_region5, iapws97_Gr_region5, iapws97_dGr_dpi_region5]
    atols = [0, 0, 0, 0, 0, 0, 5e-21, 4e-17, 1e-18]
    rtols = [1e-15, 1e-15, 1e-15, 5e-15, 2e-15, 1e-14, 1e-14, 2e-14, 2e-14]
    N = 500
    Ts = linspace(1073.15, 2273.15, N)
    def test_Ps(T, N):
        return logspace(log10(1e-6), log10(50e6), N)
    
    for naive, fast, rtol, atol in zip(funcs_naive, funcs_fast, rtols, atols):
#        print(naive)
        for T in Ts:
            tau = 1000.0/T
            for P in test_Ps(T, N):
                pi = P/1E6
                assert_close(naive(tau, pi),
                             fast(tau, pi), rtol=rtol, atol=atol)
#test_iapws97_region5_fuzz()
### Fast tests

def test_iapws97_dG_dpi_region1():
    assert_close(iapws97_dG_dpi_region1_naive(1386/277.15, 101325/16.53E6),
                 iapws97_dG_dpi_region1(1386/277.15, 101325/16.53E6), rtol=1e-14)
    
    assert_close(iapws97_dG_dpi_region1(1386/277.15, 101325/16.53E6),
                 0.12923271825448354, rtol=1e-14)
    
    # Point that had bad error with horner's method
    assert_close(iapws97_dG_dpi_region1(1386 / 600.15, 10001325 / 16.53E6),
                 0.09345587583404263, rtol=1e-14)
    assert_close(iapws97_dG_dpi_region1(1386/277.15, 101325/16.53E6),
                 iapws97_dG_dpi_region1_naive(1386/277.15, 101325/16.53E6), rtol=1e-14)


def test_iapws97_dG_dpi_region2():
    assert_close(iapws97_dGr_dpi_region2(.656, 16), -0.006292631931275252, rtol=1e-14)
    
    
    # Point that had bad error with horner's method
    assert_close(iapws97_dGr_dpi_region2(0.788009171330091, 26.87134177929712), -0.018525334158583723, rtol=1e-14)

def test_iapws97_dG_dpi_region5():
    assert_close(iapws97_dGr_dpi_region5(.5, 30.0), 0.0004009761854002751, rtol=1e-14)

def test_iapws_boundary_equations():
    assert_close(iapws97_boundary_2_3(0.623150000E3), 16529164.252621626, rtol=1e-13)
    
    assert_close(iapws97_boundary_3uv(22.3E6), 647.7996121480069, rtol=1e-14)
    
    assert_close(iapws97_boundary_3ef(40E6), 713.959399239744, rtol=1e-14)
    
    assert_close(iapws97_boundary_3cd(25E6), 649.3659208321279, rtol=1e-14)
    
    assert_close(iapws97_boundary_3gh(25E6), 656.6980572261236, rtol=2e-14)
    
    assert_close(iapws97_boundary_3ij(25E6), 660.7865756716819, rtol=1e-14)
    
    assert_close(iapws97_boundary_3jk(25E6), 668.1915358826951, rtol=1e-14)
    
    assert_close(iapws97_boundary_3mn(22.8E6), 649.6054132953997, rtol=1e-14)
    
    assert_close(iapws97_boundary_3qu(22E6), 645.6355027340121, rtol=1e-14)
    
    assert_close(iapws97_boundary_3rx(22E6), 648.2622753670172, rtol=1e-14)
    
    assert_close(iapws97_boundary_3wx(log(22.3), 1 / log(22.3)), 648.204947950734, rtol=1e-14)
    
    assert_close(iapws97_boundary_3ab(log(40), 1 / log(40)), 693.0341408296053, rtol=1e-14)
    
    assert_close(iapws97_boundary_3op(log(22.8), 1 / log(22.8)), 650.010694314133, rtol=1e-14)
    
def test_iapws97_region_3_misc():
    assert iapws97_region_3(630, 50e6) == REGION_3A
    assert iapws97_region_3(709.5013, 50e6) == REGION_3B
    assert iapws97_region_3(709.5012, 50e6) == REGION_3A
    
    assert iapws97_region_3(700.0, 30e6) == REGION_3F
    
    # CoolProp differs but http://twt.mpei.ac.ru/MCS/Worksheets/iapws/IAPWS-IF97-Region3-VPT.xmcd confirms it is C here.
    # A test with IAPWS95 shows CoolProp matches the correct answer better
    # We are right next to a transition point / huge discontinuity here.
    assert iapws97_region_3(623.1500000001, 16529164.269161053) == REGION_3C



def test_iapws97_region_full_table():
    assert iapws97_region_3(630, 50e6) == REGION_3A
    assert_close(1/iapws97_region3_rho(T=630, P=50e6), 0.001470853100110911, rtol=1e-13)
    assert iapws97_region_3(670, 80e6) == REGION_3A
    assert_close(1/iapws97_region3_rho(T=670, P=80e6), 0.0015038313585404727, rtol=1e-13)
    
    assert iapws97_region_3(710.0, 50e6) == REGION_3B
    assert_close(1/iapws97_region3_rho(T=710, P=50e6), 0.0022047285870574838, rtol=1e-13)
    assert iapws97_region_3(750.0, 80e6) == REGION_3B
    assert_close(1/iapws97_region3_rho(T=750, P=80e6), 0.0019736929401211155, rtol=1e-13)
    
    assert iapws97_region_3(630.0, 20e6) == REGION_3C
    assert_close(1/iapws97_region3_rho(T=630, P=20e6), 0.0017616964055295276, rtol=1e-13)
    assert iapws97_region_3(650.0, 30e6) == REGION_3C
    assert_close(1/iapws97_region3_rho(T=650, P=30e6), 0.0018195606165288332, rtol=1e-13)
    
    assert iapws97_region_3(656.0, 26e6) == REGION_3D
    assert_close(1/iapws97_region3_rho(T=656, P=26e6), 0.002245587720029806, rtol=1e-13)
    assert iapws97_region_3(670.0, 30e6) == REGION_3D
    assert_close(1/iapws97_region3_rho(T=670, P=30e6), 0.002506897701629579, rtol=1e-13)
    
    assert iapws97_region_3(661.0, 26e6) == REGION_3E
    assert_close(1/iapws97_region3_rho(T=661, P=26e6), 0.0029702259620031472, rtol=1e-13)
    assert iapws97_region_3(675.0, 30e6) == REGION_3E
    assert_close(1/iapws97_region3_rho(T=675, P=30e6), 0.0030046270863580073, rtol=1e-13)
    
    assert iapws97_region_3(671.0, 26e6) == REGION_3F
    assert_close(1/iapws97_region3_rho(T=671, P=26e6), 0.00501902940104471, rtol=1e-13)
    assert iapws97_region_3(690.0, 30e6) == REGION_3F
    assert_close(1/iapws97_region3_rho(T=690, P=30e6), 0.004656470141685632, rtol=1e-13)
    
    assert iapws97_region_3(649.0, 23.6e6) == REGION_3G
    assert_close(1/iapws97_region3_rho(T=649, P=23.6e6), 0.0021631983783137196, rtol=1e-13)
    assert iapws97_region_3(650.0, 24e6) == REGION_3G
    assert_close(1/iapws97_region3_rho(T=650, P=24e6), 0.0021660441609564836, rtol=1e-13)
    
    assert iapws97_region_3(652.0, 23.6e6) == REGION_3H
    assert_close(1/iapws97_region3_rho(T=652, P=23.6e6), 0.002651081406573861, rtol=1e-13)
    assert iapws97_region_3(654.0, 24e6) == REGION_3H
    assert_close(1/iapws97_region3_rho(T=654, P=24e6), 0.0029678023349397832, rtol=1e-13)
    
    assert iapws97_region_3(653.0, 23.6e6) == REGION_3I
    assert_close(1/iapws97_region3_rho(T=653, P=23.6e6), 0.003273916815935874, rtol=1e-13)
    assert iapws97_region_3(655.0, 24e6) == REGION_3I
    assert_close(1/iapws97_region3_rho(T=655, P=24e6), 0.0035503298636594843, rtol=1e-13)
    
    assert iapws97_region_3(655.0, 23.5e6) == REGION_3J
    assert_close(1/iapws97_region3_rho(T=655, P=23.5e6), 0.004545001141649382, rtol=1e-13)
    assert iapws97_region_3(660.0, 24e6) == REGION_3J
    assert_close(1/iapws97_region3_rho(T=660, P=24e6), 0.005100267703573203, rtol=1e-13)
    
    assert iapws97_region_3(660.0, 23e6) == REGION_3K
    assert_close(1/iapws97_region3_rho(T=660, P=23e6), 0.006109525996886692, rtol=1e-13)
    assert iapws97_region_3(670.0, 24e6) == REGION_3K
    assert_close(1/iapws97_region3_rho(T=670, P=24e6), 0.0064273256447015745, rtol=1e-13)
    
    assert iapws97_region_3(646.0, 22.6e6) == REGION_3L
    assert_close(1/iapws97_region3_rho(T=646, P=22.6e6), 0.0021178608506781027, rtol=1e-13)
    assert iapws97_region_3(646.0, 23e6) == REGION_3L
    assert_close(1/iapws97_region3_rho(T=646, P=23e6), 0.002062374674146725, rtol=1e-13)
    
    assert iapws97_region_3(648.6, 22.6e6) == REGION_3M
    assert_close(1/iapws97_region3_rho(T=648.6, P=22.6e6), 0.002533063780421483, rtol=1e-13)
    assert iapws97_region_3(649.3, 22.8e6) == REGION_3M
    assert_close(1/iapws97_region3_rho(T=649.3, P=22.8e6), 0.0025729717809150347, rtol=1e-13)
    
    assert iapws97_region_3(649, 22.6e6) == REGION_3N
    assert_close(1/iapws97_region3_rho(T=649, P=22.6e6), 0.0029234327109982578, rtol=1e-13)
    assert iapws97_region_3(649.7, 22.8e6) == REGION_3N
    assert_close(1/iapws97_region3_rho(T=649.7, P=22.8e6), 0.0029133114940412745, rtol=1e-13)
    
    assert iapws97_region_3(649.1, 22.6e6) == REGION_3O
    assert_close(1/iapws97_region3_rho(T=649.1, P=22.6e6), 0.003131208996006528, rtol=1e-13)
    assert iapws97_region_3(649.9, 22.8e6) == REGION_3O
    assert_close(1/iapws97_region3_rho(T=649.9, P=22.8e6), 0.003221160277936286, rtol=1e-13)
    
    assert iapws97_region_3(649.4, 22.6e6) == REGION_3P
    assert_close(1/iapws97_region3_rho(T=649.4, P=22.6e6), 0.0037155961864873133, rtol=1e-13)
    assert iapws97_region_3(650.2, 22.8e6) == REGION_3P
    assert_close(1/iapws97_region3_rho(T=650.2, P=22.8e6), 0.0036647547896187177, rtol=1e-13)
    
    assert iapws97_region_3(640, 21.1E6) == REGION_3Q
    assert_close(1/iapws97_region3_rho(T=640, P=21.1E6), 0.001970999271891958, rtol=1e-13)
    assert iapws97_region_3(643, 21.8E6) == REGION_3Q
    assert_close(1/iapws97_region3_rho(T=643, P=21.8E6), 0.002043919160913867, rtol=1e-13)
    
    assert iapws97_region_3(644, 21.1E6) == REGION_3R
    assert_close(1/iapws97_region3_rho(T=644, P=21.1E6), 0.00525100992110033, rtol=1e-13)
    assert iapws97_region_3(648, 21.8E6) == REGION_3R
    assert_close(1/iapws97_region3_rho(T=648, P=21.8E6), 0.00525684474078012, rtol=1e-13)
    
    assert iapws97_region_3(635.0, 19.1e6) == REGION_3S
    assert_close(1/iapws97_region3_rho(T=635, P=19.1e6), 0.0019328290790263667, rtol=1e-13)
    assert iapws97_region_3(638.0, 20e6) == REGION_3S
    assert_close(1/iapws97_region3_rho(T=638, P=20e6), 0.0019853872274726695, rtol=1e-13)
    
    assert iapws97_region_3(626, 17e6) == REGION_3T
    assert_close(1/iapws97_region3_rho(T=626, P=17e6), 0.008483262001139871, rtol=1e-13)
    assert iapws97_region_3(640, 20e6) == REGION_3T
    assert_close(1/iapws97_region3_rho(T=640, P=20e6), 0.006227528101006945, rtol=1e-13)
    
    assert iapws97_region_3(644.6, 21.5e6) == REGION_3U
    assert_close(1/iapws97_region3_rho(T=644.6, P=21.5e6), 0.002268366646629464, rtol=1e-13)
    assert iapws97_region_3(646.1, 22e6) == REGION_3U
    assert_close(1/iapws97_region3_rho(T=646.1, P=22e6), 0.0022963505532551556, rtol=1e-13)
    
    assert iapws97_region_3(648.6, 22.5e6) == REGION_3V
    assert_close(1/iapws97_region3_rho(T=648.6, P=22.5e6), 0.002832373260251989, rtol=1e-13)
    assert iapws97_region_3(647.9, 22.3e6) == REGION_3V
    assert_close(1/iapws97_region3_rho(T=647.9, P=22.3e6), 0.0028114244045568644, rtol=1e-13)
    
    assert iapws97_region_3(647.5, 22.15e6) == REGION_3W
    assert_close(1/iapws97_region3_rho(T=647.5, P=22.15e6), 0.003694032280598682, rtol=1e-13)
    assert iapws97_region_3(648.1, 22.3e6) == REGION_3W
    assert_close(1/iapws97_region3_rho(T=648.1, P=22.3e6), 0.0036222263053987108, rtol=1e-13)
    
    assert iapws97_region_3(648, 22.11e6) == REGION_3X
    assert_close(1/iapws97_region3_rho(T=648, P=22.11e6), 0.004528072648832488, rtol=1e-13)
    assert iapws97_region_3(649, 22.3e6) == REGION_3X
    assert_close(1/iapws97_region3_rho(T=649, P=22.3e6), 0.004556905798876878, rtol=1e-13)
    
    assert iapws97_region_3(646.84, 22e6) == REGION_3Y
    assert_close(1/iapws97_region3_rho(T=646.84, P=22e6), 0.0026983547189247956, rtol=3e-13)
    assert iapws97_region_3(647.05, 22.064e6) == REGION_3Y
    assert_close(1/iapws97_region3_rho(T=647.05, P=22.064e6), 0.0027176556481596707, rtol=3e-12)
    
    assert iapws97_region_3(646.89, 22e6) == REGION_3Z
    assert_close(1/iapws97_region3_rho(T=646.89, P=22e6), 0.003798732962152225, rtol=2e-12)
    assert iapws97_region_3(647.15, 22.064e6) == REGION_3Z
    assert_close(1/iapws97_region3_rho(T=647.15, P=22.064e6), 0.003701940009172692, rtol=2e-12)



def test_iapws97_rho(): 
    assert_close(iapws97_rho(T=330, P=8e5), 985.1049808079207)
    assert_close(iapws97_rho(T=823, P=14e6), 40.39293607288123)
    assert_close(iapws97_rho(T=2000, P=3e7), 32.11456228328856)
    assert_close(iapws97_rho(648.6, 22.5e6), 353.06081088726)

@pytest.mark.CoolProp
@pytest.mark.slow
def test_iapws97_region_3_rho_coolprop():
    from CoolProp.CoolProp import PropsSI
    Ts = linspace(623.15+1e-10, 1073.15, 100)
    # Do some points near where more region transitions are, and then up to the limit.
    for P_lim in (25.5e6, 100e6):
        def test_Ps(T, N):
             # Do not check too low to the boundary
             # Sometimes CoolProp says a different region
            lower_P = iapws97_boundary_2_3(T)*(1+4e-6)
            if lower_P >= P_lim:
                # No valid points in region 3
                return []
            upper_P = iapws97_boundary_2_3(T)*10.0
            upper_P = min(upper_P, P_lim)
            return logspace(log10(lower_P), log10(upper_P), N)
    
        for T in Ts:
            for P in test_Ps(T, 100):
                assert iapws97_identify_region_TP(T, P) == 3
                rho_implemented = iapws97_rho(T=T, P=P)
                rho_CoolProp = PropsSI('DMASS','T',T,'P',P,'IF97::Water')
    #            try:
                assert_close(rho_CoolProp, rho_implemented, rtol=1e-10)
    #            except:
    #                print([T, P, 1-rho_CoolProp/rho_implemented])
#test_iapws97_region_3_rho_coolprop()
    
    
@pytest.mark.CoolProp
@pytest.mark.slow
def test_iapws97_region_5_rho_coolprop():
    # Working great!
    from CoolProp.CoolProp import PropsSI
    Ts = linspace(1073.15+1e-10, 2273.15, 100)
    def test_Ps(T, N):
        return logspace(log10(1e-6), log10(50e6), N)

    for T in Ts:
        for P in test_Ps(T, 100):
            assert iapws97_identify_region_TP(T, P) == 5
            rho_implemented = iapws97_rho(T=T, P=P)
            rho_CoolProp = PropsSI('DMASS','T',T,'P',P,'IF97::Water')
            assert_close(rho_CoolProp, rho_implemented, rtol=1e-10)


def iapws97_dGr_dpi_region2_fastest(tau, pi):
    '''Fastest implementation, maybe near possible. Horner's method in places
    has caused issues however and this has some error in some regions.
    '''
    taut = tau - 0.5
    pi2 = pi*pi
    taut2 = taut*taut
    taut3 = taut*taut2
    taut4 = taut2*taut2
    taut6 = taut4*taut2
    taut8 = taut4*taut4
    taut13 = taut6*taut4*taut3
    taut21 = taut13*taut8
    taut29 = taut21*taut8
    # 53 from 13*13*!3*!3*3
    # 57 from 
    return (pi*(pi*(pi*(pi*(pi*(pi*(pi*(pi*(pi*(pi2*pi2*pi2*(pi2*(pi2
        *(pi*(pi*(pi*(pi*taut13*taut13*(taut13*taut*(1.32995316841867198e-15 - 0.0000226487297378903988*taut13*taut4*taut)
        + 1.75410265428146418e-27) - 2.93678005497663003e-14*taut29*taut8*taut2) + 0.0000832192847496054092*taut*taut21*taut29*taut3)
    - 1.24017662339841913e-24*taut21) + taut8*taut8*taut4*(taut13*taut2*(6.1258633752463995e-12
    - 0.0000840049353964159951*taut13) + 1.78371690710842005e-23)) - 6.05920510335077989*taut21*taut21*taut13*taut2) 
    + taut29*(1.71088510070543998*taut21 - 1.29412653835175996e-9)) + taut4*(taut6
    *(-1.00181793795109993e-8*taut4 - 1.02347470959289996e-12) + 1.04069652101739995e-18))
    + 1.78287415218792009e-7*taut13) + taut4*taut4*(9.00496908836719986e-11 - 65.8490727183984035*taut13*taut13*taut2))
    + taut6*taut4*taut*(-0.27262789705017304*taut6*taut6*taut2 - 8.83526622937069987e-6) - 4.13416950269890026e-17)
    + taut3*(taut13*(-143.374451604623999*taut13*taut6 - 0.012702883392812999) - 1.00288598706366e-10))
    + 0.0000114610381688305001*taut6*taut) + taut*(taut*(1.92901490874028006e-6*taut + 5.11628714091400033e-8)
    - 3.15389238237468004e-9)) + taut*(taut2*(taut3*(-0.122004760687946995*taut21*taut8 
    - 0.00451017736264439952) - 0.0000968330317157100001) + 1.31612001853305008e-6) + 6.14452130769269999e-8)
    + taut*(taut*(taut2*(taut3*(-0.0000533490958281740028*taut21*taut8 - 0.0875945913011459965) 
    - 0.00787855544867100029) - 0.000378979750326299998) - 0.000066065283340406)) 
    + taut*(taut*(taut*(-0.0503252787279300021*taut3 - 0.0575812590834320001) - 0.0459960136963650026) 
    - 0.0178348622923579989) - 0.00177317424732129992)


@pytest.mark.CoolProp
@pytest.mark.slow
def test_iapws97_region_2_rho_coolprop():
    from CoolProp.CoolProp import PropsSI
    P_lim = 1e-6
    Ts = linspace(273.15+1e-10,  1073.15-1e-10, 100)
    def test_Ps(T, N):
        upper_P = iapws97_boundary_2_3(T)*(1.0-1e-10)
        if T <= 623.15:
            upper_P = min(Psat_IAPWS(T)*(1.0-1e-10), upper_P)
        
        
        if upper_P < P_lim or upper_P > 100e6:
            # No valid points in region 2
            return []

        return logspace(log10(P_lim), log10(upper_P), N)

    for T in Ts:
        for P in test_Ps(T, 100):
            assert iapws97_identify_region_TP(T, P) == 2
            rho_implemented = iapws97_rho(T=T, P=P)
            rho_CoolProp = PropsSI('DMASS','T',T,'P',P,'IF97::Water')
#            try:
            assert_close(rho_CoolProp, rho_implemented, rtol=2e-15)
#            except:
#                print([T, P, 1-rho_implemented/rho_CoolProp])


@pytest.mark.CoolProp
@pytest.mark.slow
def test_iapws97_region_1_rho_coolprop():
    from CoolProp.CoolProp import PropsSI
    Ts = linspace(273.15+1e-10,  623.15-1e-10, 500)
    def test_Ps(T, N):
        Psat = Psat_IAPWS(T)*(1+1e-10)
        return logspace(log10(Psat), log10(100e6), N)

    for T in Ts:
        for P in test_Ps(T, 500):
            assert iapws97_identify_region_TP(T, P) == 1
            rho_implemented = iapws97_rho(T=T, P=P)
            rho_CoolProp = PropsSI('DMASS','T',T,'P',P,'IF97::Water')
            try:
                assert_close(rho_CoolProp, rho_implemented, rtol=2e-13)
            except:
                print([T, P, 1-rho_implemented/rho_CoolProp])


def test_iapws97_P():
    rho = iapws97_rho(273.15, 999)
    assert_close(iapws97_P(273.15, rho), 999, rtol=1e-10)
    
    rho = iapws97_rho(289.47653061224486, 145.6348477501249)
    assert_close(iapws97_P(289.47653061224486, rho), 145.6348477501249, rtol=1e-10)
    
    iapws97_identify_region_TP(1032.9489949748788, 1702.7691722259083)
    rho = iapws97_rho(1032.9489949748788, 1702.7691722259083)
    P_calc = iapws97_P(1032.9489949748788, rho)
    assert_close(P_calc, 1702.7691722259083, rtol=1e-10)
    
    rho = iapws97_rho(273.9508008008008, 696.3744730627147)
    assert_close(iapws97_P(273.9508008008008, rho), 696.3744730627147, rtol=5e-9)
    
    
    rho = iapws97_rho(275.5524024024024, 749.6781874965719)
    assert_close(iapws97_P(275.5524024024024, rho), 749.6781874965719, rtol=5e-9)
    
    rho = iapws97_rho(1500, 20e6)
    assert_close(iapws97_P(1500, rho), 20e6, rtol=5e-9)

    
    T_spec = 300
    rho_spec = .02
    for i in range(15):
        P_calc = iapws97_P(T_spec, rho_spec)
        assert_close(iapws97_rho(T_spec, P_calc), rho_spec, rtol=1e-10)
        rho_spec *= .25
        

@pytest.mark.slow
@pytest.mark.fuzz
def test_iapws97_P_fuzz():
    N = 40
    Ts = linspace(273.15, 623.15, N)
    # Ts = linspace(273.15, 1073.15, N)
    Ps = logspace(log10(1e-5), log10(100e6), N)
    for T in Ts:
        for P in Ps:
            rho = iapws97_rho(T, P)
            P_calc = iapws97_P(T, rho)
            assert_close(P, P_calc, rtol=1e-9)
            
    
    # Region 1 and 2 general - Good, working great!
    N = 100
    Ts = linspace(273.15, 1073.15, N)
    Ps = logspace(log10(1e-8), log10(100e6), N)
    for T in Ts:
        for P in Ps:
            if iapws97_identify_region_TP(T, P) != 3:
                rho = iapws97_rho(T, P)
                P_calc = iapws97_P(T, rho)
                # 5e-9 is best solvers can do
                assert_close(P, P_calc, rtol=5e-9)
    
    # Region 5 - works great
    N = 100
    Ts = linspace(1073.15, 2273.15, N)
    Ps = logspace(log10(1e-8), log10(50e6), N)
    for T in Ts:
        for P in Ps:
            rho = iapws97_rho(T, P)
            P_calc = iapws97_P(T, rho)
            assert_close(P, P_calc, rtol=1e-9)
            
            
def test_iapws_97_Trho_err_region():
    from chemicals.iapws import iapws_97_Trho_err_region1, iapws_97_Trho_err_region2, iapws_97_Trho_err_region5
    drho_dP_num = derivative(lambda P, *args: iapws_97_Trho_err_region1(P, *args)[0], 1e5, args=(400, 940), dx=1e-1)
    rho_err, drho_dP_analytical = iapws_97_Trho_err_region1(1e5, T=400.0, rho=940)
    assert_close(drho_dP_num, drho_dP_analytical)
    assert_close(drho_dP_analytical, 5.139076806770276e-07)
    assert_close(rho_err, -2.590879183496895)
    
    drho_dP_num = derivative(lambda P, *args: iapws_97_Trho_err_region2(P, *args)[0], 1e5, args=(400, .5), dx=1e-1)
    rho_err, drho_dP_analytical = iapws_97_Trho_err_region2(1e5, T=400.0, rho=.5)
    assert_close(drho_dP_num, drho_dP_analytical)
    assert_close(drho_dP_analytical, 5.5373377906291985e-06,)
    assert_close(rho_err, 0.04758348314889638)
    
    drho_dP_num = derivative(lambda P, *args: iapws_97_Trho_err_region5(P, *args)[0], 1e6, args=(2200, 50), dx=1)
    rho_err, drho_dP_analytical = iapws_97_Trho_err_region5(1e6, T=2200, rho=50)
    assert_close(drho_dP_num, drho_dP_analytical)
    assert_close(drho_dP_analytical, 9.84028484195585e-07)
    assert_close(rho_err, -49.01554810610934)


def test_iapws_97_Prho_err_region():
    from chemicals.iapws import iapws_97_Prho_err_region3, iapws_97_Prho_err_region2, iapws_97_Prho_err_region5, iapws_97_Prho_err_region1
    drho_dP_num = derivative(lambda T, *args: iapws_97_Prho_err_region2(T, *args)[0], 400, args=(1e5, 3), dx=1e-5)
    rho_err, drho_dP_analytical = iapws_97_Prho_err_region2(400, P=1e5, rho=3)
    assert_close(drho_dP_analytical, -0.0014400334536077983)
    assert_close(rho_err, -2.4524165168511036)
    assert_close(drho_dP_num, drho_dP_analytical)
    
    drho_dP_num = derivative(lambda T, *args: iapws_97_Prho_err_region5(T, *args)[0], 2000, args=(1e6, 300), dx=1e-2)
    rho_err, drho_dP_analytical = iapws_97_Prho_err_region5(2000, P=1e6, rho=3)
    assert_close(drho_dP_num, drho_dP_analytical)
    assert_close(rho_err, -1.9170536728150382, rtol=1e-10)
    assert_close(drho_dP_analytical, -0.0005418228178000102, rtol=1e-10)
    
    drho_dP_num = derivative(lambda T, *args: iapws_97_Prho_err_region1(T, *args)[0], 300, args=(1e6, 990), dx=1e-4)
    rho_err, drho_dP_analytical = iapws_97_Prho_err_region1(300, P=1e6, rho=990)
    assert_close(drho_dP_num, drho_dP_analytical)
    assert_close(rho_err, 6.960320342238447, rtol=1e-10)
    assert_close(drho_dP_analytical, -0.2744655492373509, rtol=1e-10)
    
    dP_dT_numerical = derivative(lambda T, *args: iapws_97_Prho_err_region3(T, *args)[0], 620, args=(40e6, 400), dx=.01, order=15)
    P_err, dP_dT_analytical = iapws_97_Prho_err_region3(620, P=40e6, rho=400)
    assert_close(dP_dT_numerical, dP_dT_analytical)
    assert_close(dP_dT_analytical, 215319.4089751701)
    assert_close(P_err, -25505787.520883154)


def test_iapws97_T():
    # region 5
    assert_close(iapws97_T(1e7, iapws97_rho(T=1600, P=1e7)), 1600)
    
    # region 2 top
    assert_close(iapws97_T(60e6, iapws97_rho(T=1000, P=60e6)), 1000)
    
    # region 3 top
    rho = iapws97_rho(T=640, P=60e6)
    P = iapws97_P(640, rho)
    assert_close(iapws97_T(P, rho), 640)
    
    # region 1
    rho = iapws97_rho(T=400, P=40e6)
    assert_close(iapws97_T(40e6, rho), 400)
    
    # region 2 bottom
    rho = iapws97_rho(T=800, P=1e5)
    iapws97_T(1e5, rho)
    assert_close(iapws97_T(1e5, rho), 800)
    
    # region 1 bottom
    rho = iapws97_rho(T=300, P=1e5)
    iapws97_T(1e5, rho)
    assert_close(iapws97_T(1e5, rho), 300)
    
    rho = iapws97_rho(T=273.15, P=1e-08)
    iapws97_T(1e-08, rho)
    assert_close(iapws97_T(1e-08, rho), 273.15)
    
    
    rho = iapws97_rho(273.15, 0.0065793322465757635)
    assert_close(iapws97_T(0.0065793322465757635, rho), 273.15)
    
    rho = iapws97_rho(273.15, 673.4150657750918)
    assert_close(iapws97_T(673.4150657750918, rho), 273.15)
    
    iapws97_identify_region_TP(273.15, 22570197.196339723)
    rho = iapws97_rho(273.15, 22570197.196339723)
    assert_close(iapws97_T(22570197.196339723, rho), 273.15)
    
    iapws97_identify_region_TP(1073.15, 68926121.04349865)
    rho = iapws97_rho(1073.15, 68926121.04349865)
    assert_close(iapws97_T(68926121.04349865, rho), 1073.15)
    
    rho = iapws97_rho(273.9508008008008, 17030650.2925232)
    assert_close(iapws97_T(17030650.2925232, rho), 273.9508008008008)
    
    # region 5 border requiring calc
    rho = iapws97_rho(1073.150000000001, 34705199.859195136)
    assert_close(iapws97_T(34705199.859195136, rho), 1073.150000000001)
    
    # region 5 border requiring equation 2 calc
    rho = iapws97_rho(1073.15, 52396013.53002634)
    assert_close(iapws97_T(52396013.53002634, rho), 1073.15)

@pytest.mark.slow
@pytest.mark.fuzz
def test_iapws97_T_fuzz():
    # region 2 and 1
    N = 100
    Ts = linspace(273.15, 1073.15, N)
    Ps = logspace(log10(1e-8), log10(100e6), N)
    for T in Ts:
        for P in Ps:
            if iapws97_identify_region_TP(T, P) != 3:
                rho = iapws97_rho(T, P)
                T_calc = iapws97_T(P, rho)
                try:
                    # 5e-9 is best solvers can do
                    assert_close(T, T_calc, rtol=5e-9)
                except:
                    # multiple solutions
                    rho_recalc = iapws97_rho(T_calc, P)
                    assert_close(rho, rho_recalc, rtol=5e-9)
    # region 5
    N = 100
    Ts = linspace(1073.15+1e-12, 2273.15, N)
    Ps = logspace(log10(1e-8), log10(50e6), N)
    for T in Ts:
        for P in Ps:
            assert iapws97_identify_region_TP(T, P) == 5
            rho = iapws97_rho(T, P)
            T_calc = iapws97_T(P, rho)
            assert_close(T, T_calc, rtol=5e-9)


def test_rho_iapws95_CoolProp():
    from CoolProp.CoolProp import PropsSI
    N = 40
    Ts = linspace(273.16+1e-10,  1073.15-1e-10, N)
    Ps = logspace(log10(1e-3), log10(100e6), N)
    
    for T in Ts:
        for P in Ps:
            rho_implemented = iapws95_rho(T, P)
            rho_CoolProp = PropsSI('DMASS', 'T', T, 'P', P, 'water')
            assert_close(rho_implemented, rho_CoolProp, rtol=1e-10)
            # some points found to fail near Psat curve as expected.