
print("----BIENVENIDO----")
print("_________")
# PREGUNTA y VALIDACION
diagnostico=''
diag1=''
diag2=''
resp = str((input("Responde a estimulos [S/N]")).upper())
while  resp != str('S') and resp !=str('N'):
    resp = str((input("Ingrese S / N : ")).upper())

if resp==str('S'): 
    print(( "Paciente responde a estímulos, evalue llevarlo al Hospital más cercano"))
else: 
    print("Abrir vias aereas")
    diagnostico=( "Paciente no responde a estímulos, se abren vias aereas, ")

    resp = str((input("Respira?? [S/N]")).upper())
    while  resp != str('S') and resp !=str('N'):
        resp = str((input("Ingrese S / N : ")).upper())
    
    if resp==str('S'): 
        diagnostico=diagnostico+( " logra respirar, y se llama la ambulancia.")
        print ("Permitirle posición de suficiente ventilación")
    else: 
        print("Administrar 5 ventilaciones y llamar ambulancia")
        diagnostico= diagnostico +("y no logra respirar, se administran 5 ventilaciones y llama ambulancia.")  
        ambu='N'  
        while  ambu=='N':
            diag1=''
            diag2=''
            resp = str((input("Tiene signos vitales?? [S/N]")).upper())
            while  resp != str('S') and resp !=str('N'):
                resp = str((input("Ingrese S / N : ")).upper())  
            if ambu=="S":break                
            if resp==str('S'): 
                diag2=''
                diag1 = "Pcte con signos vitales se espera hasta que llegue la ambulancia"
                print( "Reevaluar al paciente  y se esperar la ambulancia")
            else: 
                print("Administrar compresiones toracicas hasta que llegue la ambulancia")
                diag2= "Pcte sin signos vitales. Compresiones hasta que llegue la ambulancia"
                diag1=''
            
            resp = str((input("Llego la ambulancia [S/N]")).upper())
            while  resp != str('S') and resp !=str('N'):
                    resp = str((input("Ingrese S / N : ")).upper())
            if resp==str('S'): 
                ambu="S"
                print("SUERTE")
                break
            else: 
                print ("seguir esperando")

print(f"{diagnostico} {diag1} {diag2}")                



