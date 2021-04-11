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
print ("Movimiento 1 inicio hikketop  like")
pyautogui.click(pyautogui.locateCenterOnScreen("ventana2.png", confidence=0.9))
time.sleep(4)
print ("click ventana likes 1\n")
pyautogui.click(pyautogui.locateCenterOnScreen("likes.png", confidence=0.9))
for i in range(60):
        time.sleep(7)
        pyautogui.moveTo(1030, 915,duration=1)
        print ("click corazon\n")
        time.sleep(3)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(900, 500,duration=1)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(1030, 930,duration=1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.scroll(-30)
        time.sleep(2)
        pyautogui.scroll(-30)
        time.sleep(2)
        pyautogui.scroll(-20)
        time.sleep(8)
        pyautogui.click(pyautogui.locateCenterOnScreen("corazon.png", confidence=0.9))
        time.sleep(2)
        pyautogui.click(pyautogui.locateCenterOnScreen("menu_app.png", confidence=0.9))
        print ("mover al centro y click\n")
        pyautogui.moveTo(935, 552,duration=1)
        time.sleep(3)
        pyautogui.click()
                 







    
