
Digito = int(input(" Ingrese el ultimo digito de su codigo: " ))
A= Digito +3
C=0
for i in range (1,A+1):
    
    B=int(input (f"\nIngrese el {i} numero: "))
    C=C+B
    
D=C/A

print("\n")
while D != 1:
    if D % 2 == 0:
        D = D/2
        print (D)
        
    else: 
        
        D = (D*3)+1
        print (D)
        
    
    