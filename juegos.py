import PySimpleGUI as sg
import TaTeTi 
import Ahorcado2
import reverse
import json
otra_vez = 'si'
while (otra_vez == 's' or otra_vez == 'si'):
  texto = 'Es hora de jugar! A que queres jugar:' 
  layout = [[sg.Text(texto)], 
            [sg.OK('TaTeTi')], 
            [sg.OK('Ahorcado')], 
            [sg.OK('Reverse')]]
  window = sg.Window('Pequeña ventanita').Layout(layout)
  evento = window.Read()
  window.Close()
  f = open ('DatosDeLaPartida.txt','w')
  print('Ingrese su nombre: ')
  nom = input()
  datos = {}
  juegos=[]
  juegos.append(evento[0])
  datos[nom] = juegos
  json.dump(datos, f)
  f.close()
  if (evento [0]== 'TaTeTi'):
    TaTeTi.emp(True)
  elif (evento[0] == 'Ahorcado'):
      Ahorcado2.comenzar(True)
  else:
    reverse.empezar(True)
  print('Nueva partida? (si o no)')
  otra_vez = input()
