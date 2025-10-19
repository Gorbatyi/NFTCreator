import keyboard
import random
import time
import interception
#Цвета
file1 = open("colors.txt","r")
colors = []
while True:
    line = file1.readline()

    if not line:
        break
    colors.append(line)
print(len(colors))
print(colors[162])





time.sleep(2)
#Сохранение
def save(iteration):
    with interception.hold_key("shift"):
        with interception.hold_key("ctrl"):
            interception.press("s")
    time.sleep(1)
    interception.click(413,477)
    time.sleep(0.1)
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("p")
    interception.press("enter")
    time.sleep(0.2)
    interception.click(421,454)
    time.sleep(0.2)
    interception.click(421,454)
    time.sleep(0.2)
    interception.press("space")
    time.sleep(0.1)
    keyboard.write(str(iteration))
    time.sleep(0.1)
    interception.click(491,68)
    time.sleep(0.1)
    interception.click(334,183)
    time.sleep(0.1)
    interception.press("enter")
    time.sleep(0.1)
    interception.click(884,648)
    time.sleep(0.1)
    interception.press("enter")
#Скрыть/открыть рисунок
def hideviev():
    interception.click(1500,740)
#Переключиться на заднийфон
def tobackground():
    interception.click(1600,781)
#Очистить текущий цвет
def clearcolor():
    interception.press("backspace")
    interception.press("backspace")
    interception.press("backspace")
    interception.press("backspace")
    interception.press("backspace")
    interception.press("backspace")
def changecolor(color):
    #Кнопка цвета
    interception.click(11,670)
    time.sleep(0.1)
    #В поле изменения цвета
    interception.click(469,504)
    #Очистка цвета
    clearcolor()
    time.sleep(0.1)
    #Ввод цвета
    keyboard.write(color)
    time.sleep(0.1)
    #Сохранить изменение цвета
    interception.click(556,202)
    time.sleep(0.1)
    #Поменять задний фон
    interception.click(655,512)
i = 0

while True:
    hideviev()
    time.sleep(0.1)
    tobackground()
    time.sleep(0.1)
    changecolor(colors[i])
    time.sleep(0.1)
    hideviev()
    time.sleep(0.1)
    save(i)
    time.sleep(1)

    i+=1
    if i == 163:
        break
