
import turtle
import math
import random
import time
#import winsound

window = turtle.Screen()
window.setup(width = 1200, height=750)
window.title("star wars game")
window.bgcolor('black')
window.bgpic("star wars.gif") # you can use any image in gif format and put it in the same folder in which your code file exists. #if you are not using any images you can just comment out this line.
window.tracer(0)

t = turtle.Turtle()
t.write('', font = (1))
time.sleep(3)
t.hideturtle()

window.bgpic("midfinal.gif") # again you can use any images as per your choice
shape1 = ((0,70),(0,60),(-2.5,60),(2.5,60),(0,60),(0,57),(-3.5,57),(3.5,57),(0,57),(0,45),(2.5,40),(2.5,35),(5,30),(5,5),(10,2.5),(25,0),(25,10),(27.5,10),(27.5,25),(27.5,10),(30,10),(30,-15),(35,-20),(35,-25),(30,-20),(15,-15),(20,-30),(10,-20),(-10,-20),(-20,-30),(-15,-15),(-30,-20),(-35,-25),(-35,-20),(-30,-15),(-30,10),(-27.5,10),(-27.5,25),(-27.5,10),(-25,10),(-25,0),(-10,2.5),(-5,5),(-5,30),(-2.5,35),(-2.5,40),(0,45),(-5,5),(-15,-15),(0,0),(15,-15),(5,5),(0,45),(-5,5),(-30,-20),(-5,5),(0,45),(5,5),(30,-20),(5,5),(0,45),(-5,5),(-30,-15),(-5,5),(0,45),(5,5),(30,-15),(5,5),(0,45))
window.register_shape("gun", shape1)
shape2 = ((7,3),(3,7),(-3,7),(-7,3),(-7,-3),(-3,-7),(3,-7),(7,-3),(7,3))
window.register_shape("asteroid", shape2)
shape3 = ((0,7.2),(0.4,6.4),(0.8,5.2),(1.2,4),(1.2,0.8),(1.6,0),(1.6,-6),(-1.6,-6),(-1.6,0),(-1.2,0.8),(-1.2,4),(-0.8,5.2),(-0.4,6.4),(0,7.2))
window.register_shape("bullet", shape3)

# These coordinates above are for the shapes of the gun, bullets and asteroids...you can just draw it in a graph sheet and put the coordinates of you choice


gun = turtle.Turtle()
gun.setposition(0,0)
gun.shape("gun")
gun.color("red", "white")
gun.score = 0

bullets = []
for i in range(5):
	bullet = turtle.Turtle()
	bullet.shape("bullet")
	#bullet.speed(1)
	bullet.setposition(0,0)
	bullet.color("orange")
	bullet.hideturtle()
	bullet.speed = 10
	bullet.state = "ready"
	bullets.append(bullet)

pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0", False, align = "center", font = ("Times New Roman", 24, "normal"))

asteroids = []
for i in range(5):
	asteroid = turtle.Turtle()
	asteroid.shape("asteroid")
	asteroid.color("red")
	asteroid.penup()
	asteroid.setposition(0,0)
	asteroid.hideturtle()
	#asteroid.speed(1)
	asteroid.speed = 0.3  #you can change the speeed of the asteroids as per your wish..
	angle = random.randint(0,360)
	asteroid.setheading(angle)
	distance = random.randint(300,550)
	asteroid.forward(distance)
	asteroid.left(180)
	asteroid.showturtle()
	asteroids.append(asteroid)

def defense1():
	gun.left(10)
	for bullet in bullets:
		bullet.left(10)

def defense2():
	gun.right(10)
	for bullet in bullets:
		bullet.right(10)

def fire_bullet():
	for bullet in bullets:
		if bullet.state == "ready":
			bullet.penup()
			bullet.state = "fire"
			break
'''
#def play_sound():
	#winsound.PlaySound("machinegun.mp3")
'''
window.listen()
window.onkey(defense1, "Left")
window.onkey(defense2, "Right")
window.onkey(fire_bullet, "space")
#window.onkey(play_sound, "space")
window.onkeypress(defense1, "Left")
window.onkeypress(defense2, "Right")
window.onkeypress(fire_bullet, "space")

condition = True
while True: 
	window.update()

	for bullet in bullets:
		if bullet.state == "fire":
			#bullet.speed = 1
			bullet.showturtle()
			#bullet.forward(100)
			bullet.forward(bullet.speed)
			'''

			#if gun.distance(bullet)>70:
				#angle = math.atan2(bullet.ycor(), bullet.xcor())
				#degree = (180/3.14)*angle
				#bullet.setheading(degree)
			'''

			if bullet.xcor()>550 or bullet.xcor()<-550 or bullet.ycor()>550 or bullet.ycor()<-550:
				bullet.state = "ready"
					#bullet.showturtle()

		if bullet.state == "ready":
			bullet.setposition(0,0)

	for asteroid in asteroids:
		#asteroid.forward(0.1)
		#asteroid.speed(0.6)
		asteroid.forward(asteroid.speed)


		for bullet in bullets:
			if asteroid.distance(bullet)<20:
				angle = random.randint(0,360)
				asteroid.hideturtle()
				asteroid.setposition(0,0)
				asteroid.setheading(angle)
				asteroid.forward(distance)
				asteroid.left(180)
				asteroid.showturtle()
				asteroid.speed += 0.01
				bullet.state = "ready"
				
				gun.score += 10
				pen.clear()
				pen.write("Score: {}".format(gun.score), False, align = "center", font = ("Times New Roman",24,"normal"))



		if asteroid.distance(gun)<30:
			condition = False
			#gun.hideturtle()
			#bullet.hideturtle()
			#asteroid.hideturtle()

			#gun.score -= 30
			pen.clear()
			pen.write("Score: {}".format(gun.score), False, align = "center", font = ("Times New Roman",24, "normal"))

	if condition == False:
		pen.write("Score: {}".format(gun.score),False ,align = "center", font = ("Times New Roman",24, "normal"))
		window.bgpic("game over.gif")
		gun.hideturtle()
		#bullet.showturtle()
		#asteroid.showturtle()
		#pen.clear()
		break

window.mainloop()










