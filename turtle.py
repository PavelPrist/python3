# import turtle
# turtle.hideturtle()
# turtle.fillcolor('blue')
# turtle.begin_fill()
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.end_fill()
# turtle.done()
#
# import turtle
# turtle.hideturtle()
# turtle.begin_fill()
# turtle.goto(120,120)
# turtle.goto(200,-100)
# turtle.end_fill()
# turtle.done()

# Эта программа наносит звезды созвездия Ориона,
# названия звезд и линии созвездия.

import turtle

# Задать размер окна.
turtle.setup(500, 600)
#Установить черепаху.
turtle.penup()
turtle.hideturtle()
# Создать именованные константы для звездных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X =  80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_КNЕЕ_X = -90
LEFT_КNЕЕ_Y = -180

RIGHT_КNЕЕ_X = 120
RIGHT_КNЕЕ_Y = -140

# Нанести звезды.

turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) # Левое плечо
turtle.dot ()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) # Правое плечо
turtle.dot ()
turtle.goto(LEFT_BELTSTAR_X,LEFT_BELTSTAR_Y) # Левая звезда в поясе
turtle.dot ()
turtle.goto(MIDDLE_BELTSTAR_X,MIDDLE_BELTSTAR_Y) # Средняя звезда
turtle.dot ()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #Правая звезда
turtle.dot ()
turtle.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y) #Левое колено
turtle.dot()
turtle.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y) # Правое колено
turtle.dot ()
# Вывести названия звезд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y) #Левое плечо
turtle.write('Бeтeльгeйзe')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y) #Правое плечо
turtle.write ('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) #Левая звезда в поясе
turtle.write('Aпьнитaк')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) # Средняя звезда
turtle.write('Aпьнилaм')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y) #Правая звезда
turtle.write ('Минтака')
turtle.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y) #Левое колено
turtle.write ('Саиф')
turtle.goto(RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y) # Правое колено
turtle.write('Pигeль')

# Нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X,RIGHT_BELTSTAR_Y)
turtle.penup()
# Нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_КNЕЕ_X, LEFT_КNЕЕ_Y)
turtle.penup()

# Нанести линию из правой звездЫ пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto (RIGHT_КNЕЕ_X, RIGHT_КNЕЕ_Y)

# Оставить окно открытым . (В среде IDLE не требуется.)
turtle.done()


