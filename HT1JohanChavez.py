peso = input ("Ingrese su peso en kilogramos ")
estatura = input ("Ingrese su estatura en metros ")
IMC = round(float(peso)/(float(estatura)**2),2)
print ("Tu índice de masa corporal es ", IMC)