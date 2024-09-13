import math
import cmath    
import numpy as np # type: ignore 

Vsmag = 277 
Vsphase = 0
S1mag = 6900
S1phase = 17 
S2mag = 5000
S2phase = 25
Vk1mag = 277
Vk1phase = 0
Vk2mag = 277
Vk2phase = 0
Zf1 = 1j
Zf2 = 1j
kmax = 10

#conversions to rectangular

Vrad = np.radians(Vsphase)
Vsreal = Vsmag * np.cos(Vrad)
Vsimag = Vsmag * np.sin(Vrad)

Vs = complex(Vsreal, Vsimag) #our V source in rectangular form converted from the angle given in the initial variables

S1rad = np.radians(S1phase)
S1real = S1mag * np.cos(S1rad)
S1imag = S1mag * np.sin(S1rad)

S1 = complex(S1real, S1imag) #S1 in rectangular

S2rad = np.radians(S2phase)
S2real = S2mag * np.cos(S2rad)
S2imag = S2mag * np.sin(S2rad)

S2 = complex(S2real, S2imag) #S2 in rectangular

Vk1rad = np.radians(Vk1phase)
Vk1real = Vk1mag * np.cos(Vk1rad)
Vk1imag = Vk1mag * np.sin(Vk1rad)

Vk1 = complex(Vk1real, Vk1imag) #Vk1 in rectangular

Vk2rad = np.radians(Vk2phase)
Vk2real = Vk2mag * np.cos(Vk2rad)
Vk2imag = Vk2mag * np.sin(Vk2rad)

Vk2 = complex(Vk2real, Vk2imag) #Vk2 in rectangular

print(f"V1 and V2 through all iterations 1 to {kmax}")

#iteration loop
for k in range(0, kmax):

    S1conj = np.conj(S1)
    Vk1conj = np.conj(Vk1)
    S2conj = np.conj(S2)
    Vk2conj = np.conj(Vk2)

    V1 = Vs-((S1conj/Vk1conj)+(S2conj/Vk2conj))*Zf1 #V1(k+1) equation
    V2 = V1 - (S2conj/Vk2conj)*Zf2 #V2(k+1) equation

    V1r = np.angle(V1)
    V1ph = np.degrees(V1r)
    V1pol = np.abs(V1)

    V2r = np.angle(V2)
    V2ph = np.degrees(V2r)
    V2pol = np.abs(V2)   

    print(f"iteration {k+1}: V1 = {V1pol} angle {V1ph} V")
    print(f"iteration {k+1}: V2 = {V2pol} angle {V2ph} V\n")

    Vk1 = V1
    Vk2 = V2

#end of loop, final values
print("final current values")

I1rect = np.conj(S1) / np.conj(V1)
I1pol = np.abs(I1rect)
I1rad = np.angle(I1rect)
I1ang = np.degrees(I1rad)
print(f"If1: I1 = {I1pol} angle {I1ang} A")

I2rect = np.conj(S2) / np.conj(V2)
I2pol = np.abs(I2rect)
I2rad = np.angle(I2rect)
I2ang = np.degrees(I2rad)
print(f"If2: I2 = {I2pol} angle {I2ang} A\n")

print("final load impedence values")

Z1rect = V1 / I1rect
print(f"Zf1: {Z1rect} Ohms")

Z2rect = V2 / I2rect
print(f"Zf2: {Z2rect} Ohms\n")
