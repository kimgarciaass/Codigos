import pyautogui
import time 
print("Bem vindo!")
programa=(input("Qual programa você quer abrir?:"))
time.sleep(1)
pyautogui.press("win")
pyautogui.write(programa)
pyautogui.press("enter")
