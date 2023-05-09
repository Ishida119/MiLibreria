import random
################################################################################################################################################
def Titulo(mensaje):
    print("================================================================================================================================")
    print("UNIVERSIDAD NACIONAL DE SAN ANTONIO ABAD DEL CUSCO")
    print("================================================================================================================================")
    print("Alumno: David Daniel Huillca Llanque                                                                   Código: 221449           ")
    print("================================================================================================================================")
    print(mensaje)
    print("================================================================================================================================")
    print()
    return

###############################################################################################################################################
def LeerTiempo():
    n=3
    while n<4:
        H=LeerEntero(1,24,"Hora :")
        M=LeerEntero(1,60,"Minuto :")
        S=LeerEntero(1,60,"Segundo :")
    return H,M,S

################################################################################################################################################
def fecha1semana(texto):
    print(texto)
    año=LeerEntero(1900,2050,"Año: ")
    mes=LeerEntero(1,12,"Mes: ")
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        NroDiaMmes=31
    else:
        if mes == 2:
            if año%4==0:
                NroDiasMes=29
            else:
                NroDiasMes=28     
        else:
            NroDiasMes=30
    dia=LeerEntero(1,NroDiasMes,"Día: ")
    fechaFinal=dia, mes , año
    if mes==1: # Enero
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==2: # Febrero
        fechaFinal=28-dia
        dia=(fechaFinal-7)*-1
        if fechaFinal>31:
            mes=mes+1
    if mes==3: # Marzo
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==4: # Abril
        fechaFinal=30-dia
        dia=(fechaFinal-7)*-1
        if fechaFinal>31:
            mes=mes+1
    if mes==5: # Mayo
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==6: # Junio
        fechaFinal=30-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==7: # Julio
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==8: #Agosto
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==9: # Setiembre
        fechaFinal=30-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==10: # Octubre
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==11: # Noviembre
        fechaFinal=30-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1
    if mes==12: # Diciembre
        fechaFinal=31-dia
        dia=fechaFinal-7
        if fechaFinal>31:
            mes=mes+1     

################################################################################################################################################                  
    print(fechaFinal)
    def escribirFechaFinal(dia,mes,año):
        print(dia,"/",mes,"/",año)
    if mes==1:
        NombreMes="Enero"
    elif mes==2:
        NombreMes="Febrero"
    elif mes==3:
        NombreMes="Marzo"
    elif mes==4:
        NombreMes="Abril"
    elif mes==5:
        NombreMes="Mayo"
    elif mes==6:
        NombreMes="Junio"
    elif mes==7:
        NombreMes="Julio"
    elif mes==8:
        NombreMes="Agosto"
    elif mes==9:
        NombreMes="Setiembre"
    elif mes==10:
        NombreMes="Octubre"
    elif mes==11:
        NombreMes="Noviembre"
    elif mes==12:
        NombreMes="Diciembre"
    print(dia,"de",NombreMes,"del",año)

################################################################################################################################################
def LeerFecha(texto):
    print(texto)
    año=LeerEntero(1900,2050,"Año: ")
    mes=LeerEntero(1,12,"Mes: ")
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        NroDiasMes=31
    else:
        if mes == 2:
            if año%4==0:
                NroDiasMes=29
            else:
                NroDiasMes=28     
        else:
            NroDiasMes=30
    dia=LeerEntero(1,NroDiasMes,"Dia: ")
    return dia,mes,año


################################################################################################################################################
def escribirFecha(dia,mes,año):
    print(dia,"/",mes,"/",año)
    return 

################################################################################################################################################
def escribirFecha2(dia,mes,año):
    print(dia,"/",mes,"/",año)
    if mes==1:
        NombreMes="Enero"
    elif mes==2:
        NombreMes="Febrero"
    elif mes==3:
        NombreMes="Marzo"
    elif mes==4:
        NombreMes="Abril"
    elif mes==5:
        NombreMes="Mayo"
    elif mes==6:
        NombreMes="Junio"
    elif mes==7:
        NombreMes="Julio"
    elif mes==8:
        NombreMes="Agosto"
    elif mes==9:
        NombreMes="Setiembre"
    elif mes==10:
        NombreMes="Octubre"
    elif mes==11:
        NombreMes="Noviembre"
    elif mes==12:
        NombreMes="Diciembre"
    print(dia,"de",NombreMes,"del",año)

################################################################################################################################################
def MayorDos(A,B):
    if A>B:
        Mayor=A
    else:
        Mayor=B
    return Mayor
def MenorDos(A,B):
    if A<B:
        Menor=A
    else:
        Menor=B
    return Menor

################################################################################################################################################
def LeerEntero(Min, Max,Texto):

    N=int (input(Texto))
    while N<Min or N>Max:
        print ("Digite un número entre",Min,"y",Max)
        N=int(input(Texto))
    return N
def LeerReal(Min, Max,Texto):
    N=float(input(Texto))
    while N<Min or N>Max:
        print ("Digite un número entre",Min,"y",Max)
        N=float(input(Texto))
    return N

#     K=0
#     SumaDivisores=0
#     while K<N:
#         K=K+1
#         if N%K==0:
#             SumaDivisores=SumaDivisores+K
#     return SumaDivisores
# def SumaDivisoresPropios(N):
#     return SumaDivisoresPropios(N)-N

################################################################################################################################################
def Suma():
    print("Sumar 2 números")
    n1=int(input("Primer numero: "))
    n2=int(input("Segundo numero: "))
    s=n1+n2
    print("Al sumar",n1,"+",n2,"da como resultado: ",s)
    return

def Resta():
    print("Restar 2 números")
    n1=int(input("Primer numero: "))
    n2=int(input("Segundo numero: "))
    R=n1-n2
    print("Al restar",n1,"-",n2,"da como resultado: ",R)
    return

def Multiplicar():
    print("Multiplicar 2 números")
    n1=int(input("Primer numero: "))
    n2=int(input("Segundo numero: "))
    M=n1*n2
    print("Al multiplicar",n1,"x",n2,"da como resultado: ",M)
    return

def Dividir():
    print("Dividir 2 números")
    n1=int(input("Primer numero: "))
    n2=int(input("Segundo numero: "))
    D=n1/n2
    print("Al Dividir",n1,"/",n2,"da como resultado: ",D)
    return

#############################################################################
def LeerLista(N,texto):
    A=[]
    k=0
    while k < N:
        texto="Digite nota: "+str(k)+": "
        x=int(input(texto))
        A.append(x)
        k=k+1
    return A
def EscribirLista(A,texto):
    k=0
    while k<len(A):
        print(texto,"[",k,"]", "=",A[k])
        k=k+1
    return 

def GenerarLista(N):
    A=[]
    k=0
    while k<N:
        x=random.randint(0,100)
        A.append(x)
        k=k+1
    return A
    
def BúsquedaSecuencial(A,x):
    posición=-1
    k=0
    while k<len(A):
        if A[k]==x:
            posición=k
        k+=1
    return posición


def EliminarElemento(A,texto):
    x=int(input(texto))
    posición = BúsquedaSecuencial(A, x)
    if posición != -1:
        A = A[:posición] + A[posición+1:]
    return A

def EliminarTodos(A):
    A.clear()
    return A

def Intersección(A,B):
    C=[]
    k=0
    while k<len(A):
        if BúsquedaSecuencial(B,A[k])>-1:
            C.append(A[k])
        k+=1
    return set(C)

def Union(A,B):
    C=[]
    k=0
    while k<len(A):
        C.append(A[k])
        k+=1
    k=0
    while k<len(B):
        if BúsquedaSecuencial(A,B[k])==-1:
            C.append(B[k])
        k+=1
    return set(C)

def LeerListaSinDuplicar(N):
    A = []
    k = 0
    while k < N:
        texto = "Ingrese nota " + str(k) + ": "
        x = int(input(texto))
        if x not in A:
            A.append(x)
        k += 1
    return A

import random
def GenerarListaSinDoble(N):
    A = []
    k = 0
    while k < N:
        x = random.randint(0, 100)
        if x not in A:
            A.append(x)
            k=k+1
    return A

def menorListaSinDoble(N):
    A = GenerarListaSinDoble(N)
    menor = menorElemento(A)
    return menor

def mayorElemento(A):
    mayor = A[0]
    k = 0
    while k < len(A):
        if A[k] > mayor:
            mayor = A[k]
        k=k+1
    return mayor

def menorElemento(A):
    menor = A[0]
    k = 0
    while k < len(A):
        if A[k] < menor:
            menor = A[k]
        k=k+1
    return menor
    

def LeerConjunto(N,texto):
    A=[]
    k = 0
    while k < N:
        elemento = int(input(texto))
        A.append(elemento)
        k += 1
    return A

def DiferenciaConjuntos(N,texto):
    print("Conjunto A: ")
    conjunto1 = LeerConjunto(N,texto)
    print("Conjunto B: ")
    conjunto2= LeerConjunto(N,texto)
    diferencia = set(conjunto1) - set(conjunto2)
    return diferencia

def DiferenciaSimétrica(N,texto):
    print("Conjunto A: ")
    print("Conjunto B: ")
    conjunto1 = LeerConjunto(N,texto)
    conjunto2 = LeerConjunto(N,texto)
    diferenciaSimétrica = (Union(conjunto1,conjunto2) - Intersección(conjunto1,conjunto2))
    return diferenciaSimétrica

def sumarElementos(A):
    suma = 0
    k = 0
    while k < len(A):
        suma=suma+A[k]
        k=k+1
    return suma
#######################################################################################################
def promElementos(A):
    prom=sumarElementos(A)/len(A)
    return prom

############################################################################
def LeerSinDuplicar(N):
    A=[]
    k=0
    while k<N:
        x=random.randint(0,100)
        while BúsquedaSecuencial(A,x)>-1:
            x=random.randint(0,100000)
        A.append(x)
        k=k+1
    return A
        
def ListaAscendente(N):
    A=[]
    k=0
    x=LeerEntero(0,100,"Ingrese elemento"+str(k)+":")
    A.append(x)
    k=k+1
    while k<N:
        x=LeerEntero(0,100,"Ingrese elemento"+str(k)+":")
        while x>A[k-1]:
            x=LeerEntero(k,100,"Ingrese elemento"+str(k)+":")
        A.append(x)
        k=k+1
    return A

def OrdenarBurbuja(A):
    k=0
    while k<len(A):
        # Llevar el mayor a su posición definitiva
        j=0
        while j<len(A)-1:
            if A[j]>A[j+1]:
                T=A[j]
                A[j]=A[j+1]
                A[j+1]=T
            j=j+1
        k=k+1
    return A

def MCD(A,B):
    if A%B==0:
        return B
    else:
        return MCD(B,A%B)

def ProductoRecursivo(A,B):
    if B==0:
        return 0
    else:
        return A+ProductoRecursivo(A,B-1)

def Factorial(N):
    if N==0:
        return 1
    else:
        return N*Factorial(N-1)

def Potencia(b,N):
    if N==0 and b==0:
        return 1
    else:
        return b*Potencia(b,N-1)


# Mover discos de Hanoi
def moverDisco(n,origen,destino,auxiliar):
    if n>0:
        moverDisco(n-1,origen,auxiliar,destino)
        destino.append(origen.pop())
        moverDisco(n-1,auxiliar,destino,origen)

# pares impares de A
def paresImpares(A):
    pares=0
    impares=0
    k=0
    while k<len(A):
        if A[k]%2==0:
            pares=pares+1
        else:
            impares=impares+1
        k=k+1
    # mensaje
    if pares>impares:
        mensaje="Hay más pares"
    elif pares==impares:
        mensaje="Hay igual de pares e impares"
    else:
        mensaje="Hay más impares"
    return mensaje

def TotalDígitos2(N):
    Dígito2=0
    while N>0:
        Ud=N%10
        if Ud==2:
            Dígito2=Dígito2+1
        N=N//10
    return Dígito2

def TotalDígitos2R(N):
    if N==0:
        return 0
    else:
        if N%10==2:
            return TotalDígitos2R(N//10)+1
        else:
            return TotalDígitos2R(N//10)

def GrupoDeNotas(A):
    sobresaliente = 0
    muyBuena = 0
    aprobatoria = 0
    desaprobatoria = 0
    reprobatoria = 0
    k=0
    
    while k < len(A):
        nota = A[k]
        if nota >= 19 and nota <= 20:
            sobresaliente += 1
        elif nota >= 16 and nota <= 18:
            muyBuena += 1
        elif nota >= 14 and nota <= 15:
            aprobatoria += 1
        elif nota >= 10 and nota <= 13:
            desaprobatoria += 1
        elif nota >= 0 and nota <= 9:
            reprobatoria += 1
        k=k+1
    mayorGrupo = max(sobresaliente, muyBuena, aprobatoria, desaprobatoria, reprobatoria)
    if mayorGrupo == sobresaliente:
        return "Sobresaliente"
    elif mayorGrupo == muyBuena:
        return "Muy Buena"
    elif mayorGrupo == aprobatoria:
        return "Aprobatoria"
    elif mayorGrupo == desaprobatoria:
        return "Desaprobatoria"
    else:
        return "Reprobatoria"
    

def sumaDivisores(num):
    divisores = []
    k = 1
    while k < num:
        if num % k == 0:
            divisores.append(k)
        k += 1
    return sum(divisores)




