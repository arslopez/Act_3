# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:48:42 2023

@author: mitcy

"""

import tkinter as tk #importar tkinter
#Iniciando el programa de plan de vuelo
#Crear una ventana visible con tkinter

ventana = tk.Tk()
ventana.geometry("1000x800")

##Añadir color al fondo
ventana.config(bg='blue')

#Agregar etiquetas a la ventana

# 
etitulo = tk.Label(ventana, text='PLAN DE VUELO', font= 'Helvetica 20',  bg='black',  fg='white')
etitulo.grid(row = 0, column = 1)

##############################################################################

#ALTURA DE VUELO
ealvuelo=tk.Label(ventana, text='INGRESE LA ALTURA DE VUELO', bg='black', fg='white')
ealvuelo.grid(row = 4, column = 1)


enalvuelo = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enalvuelo.grid(row = 4, column = 4)

#FOCAL CAMARA
efocal=tk.Label(ventana, text='INGRESE EL PUNTO FOCAL', bg='black',  fg='white')
efocal.grid(row = 10, column = 1)

enfocal = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enfocal.grid(row = 10, column = 4)



#ANCHO DEL SENSOR
eAnchoS=tk.Label(ventana, text='INGRESE EL ANCHO DEL SENSOR', bg='black',  fg='white')
eAnchoS.grid(row = 15, column = 1)

enAnchoS = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enAnchoS.grid(row = 15, column = 4)

#ALTO DEL SENSOR
eAltoS=tk.Label(ventana, text='INGRESE EL AlTO DEL SENSOR', bg='black',  fg='white')
eAltoS.grid(row = 20, column = 1)

enAltoS = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enAltoS.grid(row = 20, column = 4)


#SOLAPE LONGITUDINAL
eSolL=tk.Label(ventana, text='INGRESE EL SOLAPE LONGITUDINAL', bg='black',  fg='white')
eSolL.grid(row = 25, column = 1)

enSolL = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enSolL.grid(row = 25, column = 4)

#SOLAPE TRANSVERSAL
eSolT=tk.Label(ventana, text='INGRESE EL SOLAPE TRANSVERSAL', bg='black',  fg='white')
eSolT.grid(row = 30, column = 1)

enSolT = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enSolT.grid(row = 30, column = 4)

#LARGO PARCELA
eLarP=tk.Label(ventana, text='INGRESE EL LARGO DE LA PARCELA', bg='black',  fg='white')
eLarP.grid(row = 35, column = 1)

enLarP = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enLarP.grid(row = 35, column = 4)

#ANCHO DE LA PARCELA
eAncP=tk.Label(ventana, text='INGRESE EL ANCHO DE LA PARCELA', bg='black',  fg='white')
eAncP.grid(row = 40, column = 1)

enAncP = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enAncP.grid(row = 40, column = 4)


#VELOCIDAD DE VUELO
eVelo=tk.Label(ventana, text='INGRESE LA VELOCIDAD', bg='black',  fg='white')
eVelo.grid(row = 45, column = 1)

enVelo = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enVelo.grid(row = 45, column = 4)

#DISTANCIAS DE PASADAS
eDisP=tk.Label(ventana, text='INGRESE DISTANCIA DE PASADAS', bg='black',  fg='white')
eDisP.grid(row = 50, column = 1)

enDisP = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enDisP.grid(row = 50, column = 4)


#LARGO PASADAS
eLargP=tk.Label(ventana, text='INGRESE LARGO DE PASADAS', bg='black',  fg='white')
eLargP.grid(row = 55, column = 1)

enLargP = tk.Entry(ventana, font= 'Helvetica 15', justify = 'center')
enLargP.grid(row = 55, column = 4)


#################################################
#Resultado de medición
textResult = tk.Text(ventana)
textResult.grid(row = 60, column = 4, columnspan = 2)


#######################################################3
'Funciones que permitiran el uso adecuado del programa'
    
def escalaVuelo():
    focalcamara= float(enfocal.get())
    alturavuelo=float(enalvuelo.get())
    escalaV=1/((focalcamara/1000)/alturavuelo)
    return escalaV

def AnchoImagen():
    anchosensor=float(enAnchoS.get())
    escalaV=escalaVuelo()
    anchoImagen=(anchosensor*escalaV)/1000
    return anchoImagen    
    
def GSD():
    alturavuelo= float(enalvuelo.get())
    focalcamara=float(enfocal.get())
    anchosensor=float(enAnchoS.get())
    anchoi=AnchoImagen()
    RSI=anchosensor/anchoi
    gsd=(alturavuelo/focalcamara)*RSI
    return gsd

def altoImagen():
    altoS=float(enAltoS.get())
    escalaV=escalaVuelo()
    altoImagen=altoS*escalaV
    return altoImagen
    
def baseArea():
    anchoI=AnchoImagen()
    solLon=float(enSolL.get())
    baseA=anchoI*(1-(solLon/100))
    return baseA

def distpasada():
    altoI=altoImagen()
    solT=float(enSolT.get())
    distP=altoI*(1-(solT/100))
    return distP

def tiempofotos():
    tiempoF=baseArea()/float(enVelo.get())
    return tiempoF

def nPasadas():
    nPas=float(enAncP.get())/distpasada()
    return nPas

def nfotosPas():
    nfotos=float(enLargP.get())/baseArea()
    return nfotos

def nfotosvu():
    nfotoV=nfotosPas()*nPasadas()
    return nfotoV

def distvuelo():
    dv=(nPasadas()*float(enLarP.get()))+ float(enAncP.get())
    return dv

def duracionvuelo():
    duracV=(nfotosvu()*tiempofotos())/60
    return duracV

def imprimir():
    textResult.delete(1.0, tk.END)
    gsd=GSD()
    escalaV=escalaVuelo()
    anchoI=AnchoImagen()
    altoima=altoImagen()
    base=baseArea()
    distP=distpasada()
    velo=enVelo.get()
    time=tiempofotos()
    nPas=nPasadas()
    nFot=nfotosPas()
    nfotv=nfotosvu()
    disvu=distvuelo()
    dura=duracionvuelo()
    impresion=f'Este es el resultado del plan del vuelo \n ########### \n GSD = {gsd} \n Escala de Vuelo=  {escalaV}\n Ancho de Imagen del terreno={anchoI}\n'\
         f' Alto de Imagen sobre el Terreno={altoima} \n Base Aerea={base} \n Distancia entre pasadas={distP} \n Velocidad en vuelo={velo} m/s \n' \
             f' Tiempo entre fotos={time} s\n Número de pasadas= {nPas}\n Numero de fotos por pasada= {nFot} \n Numero de por vuelo= {nfotv}\n Distancia de vuelo= {disvu} \n Duracion de vuelo= {dura}'    
    textResult.insert(tk.END, impresion)
    

    


#Añadir Botón
botonRes = tk.Button(text = "CALCULAR", font= 'Helvetica 20', command=imprimir)
botonRes.grid(row = 10, column = 5)


##Añadir un título a la ventana
ventana.title("PLAN DE VUELO LCTIG")




#Lanzar el GUI
ventana.mainloop()