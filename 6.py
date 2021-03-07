# Import relevant modules
import time
import pyautogui

# Give some time before python runs the rest of the code
time.sleep(5)
# Finding your mouse's current position on the screen
#Point 1(x=1013, y=413) inicial
#Point 2(1145, 718)
#Point 3(x=993, y=487) instagram
#765,772,761,779,776
#Point4 (x=1198, y=883) menu android
#Point(x=1036, y=474) Seleccionar neutrino
#Point(x=1091, y=599) doble click neutrino 

#movernos a estrella

#regulares
 
#770,370
#770,430 
#770,400 
#770,450//link o click seguidor
#770,470//posible error lick seguidor si
#770,490
#770,530
#770,550

print ("comenzando movimientos")
print ("Movimiento 1, estrella")
pyautogui.click(pyautogui.locateCenterOnScreen("estrella.png", confidence=0.9))
for i in range(2):
    time.sleep(3)
    print ("click estrella")
    pyautogui.scroll(+8)
    #movernos 2do punto subscribirse
    time.sleep(4)
    print ("click subscribe 1\n")
    pyautogui.moveTo(938, 713,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #segunda fila
    print ("click subscribe 1\n")
    pyautogui.moveTo(1105, 715,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #click y scroll
    print ("click centro y scroll \n")
    pyautogui.moveTo(838, 733,duration=1)
    time.sleep(3) 
    pyautogui.click()
    time.sleep(3)
    pyautogui.scroll(-8)
    #tercera fila
    print ("click subscribe 1\n")
    pyautogui.moveTo(730, 275,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #4ta fila
    print ("click subscribe 1\n")
    pyautogui.moveTo(930, 275,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #5ta fila
    print ("click subscribe 1\n")
    pyautogui.moveTo(1100, 250,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #7.1ma
    print ("click subscribe 1\n")
    pyautogui.moveTo(730, 550,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #7ma
    print ("click subscribe 1\n")
    pyautogui.moveTo(930, 550,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    #8va
    print ("click subscribe 1\n")
    pyautogui.moveTo(1100, 550,duration=1)
    pyautogui.click()
    print ("buscando boton seguir \n")
    time.sleep(5)
    BottonIG1 = pyautogui.click(pyautogui.locateCenterOnScreen("boton.png", confidence=0.9))
    BottonIG2 = pyautogui.click(pyautogui.locateCenterOnScreen("boton_con_mail.png", confidence=0.9))
    if (BottonIG1 != BottonIG2):
        BottonIG2
        pyautogui.click()
    time.sleep(3)
    pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
    print ("mover al centro y click\n")
    pyautogui.moveTo(935, 552,duration=1)
    time.sleep(3)
    pyautogui.click()
    time.sleep(4)
    pyautogui.scroll(+12)
     