# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 21:48:42 2023

@author: mitcy

"""

import tkinter as tk #importar tkinter
#Iniciando el programa de plan de vuelo
#Crear una ventana visible con tkinter

ventana = tk.Tk()
ventana.geometry("800x600")

##Añadir color al fondo
ventana.config(bg='blue')

#Agregar etiquetas a la ventana

# 
etitulo = tk.Label(ventana, text='PLAN DE VUELO', bg='black',  fg='white')
etitulo.grid(row = 0, column = 6)

#ALTURA DE VUELO
ealvuelo=tk.Label(ventana, text='INGRESE LA ALTURA DE VUELO', bg='black', fg='white')
ealvuelo.grid(row = 4, column = 1)

#FOCAL CAMARA
efocal=tk.Label(ventana, text='INGRESE EL PUNTO FOCAL', bg='black',  fg='white')
efocal.grid(row = 8, column = 1)

#ANCHO DEL SENSOR
eAnchoS=tk.Label(ventana, text='INGRESE EL ANCHO DEL SENSOR', bg='black',  fg='white')
eAnchoS.grid(row = 12, column = 1)

#ALTO DEL SENSOR
eAltoS=tk.Label(ventana, text='INGRESE EL AlTO DEL SENSOR', bg='black',  fg='white')
eAltoS.grid(row = 16, column = 1)

#SOLAPE LONGITUDINAL
eSolL=tk.Label(ventana, text='INGRESE EL SOLAPE LONGITUDINAL', bg='black',  fg='white')
eSolL.grid(row = 20, column = 1)

#SOLAPE TRANSVERSAL
eSolT=tk.Label(ventana, text='INGRESE EL SOLPAE TRANSVERSAL', bg='black',  fg='white')
eSolT.grid(row = 24, column = 1)

#LARGO PARCELA
eLarP=tk.Label(ventana, text='INGRESE EL LARGO DE LA PARCELA', bg='black',  fg='white')
eLarP.grid(row = 28, column = 1)

#ANCHO DE LA PARCELA
eAncP=tk.Label(ventana, text='INGRESE EL ANCHO DE LA PARCELA', bg='black',  fg='white')
eAncP.grid(row = 32, column = 1)


#VELOCIDAD DE VUELO
eVelo=tk.Label(ventana, text='INGRESE LA VELOCIDAD', bg='black',  fg='white')
eVelo.grid(row = 36, column = 1)

#DISTANCIAS DE PASADAS
eDisP=tk.Label(ventana, text='INGRESE DISTANCIA DE PASADAS', bg='black',  fg='white')
eDisP.grid(row = 40, column = 1)

#LARGO PASADAS
eLargP=tk.Label(ventana, text='INGRESE LARGO DE PASADAS', bg='black',  fg='white')
eLargP.grid(row = 44, column = 1)




#Lanzar el GUI
ventana.mainloop()