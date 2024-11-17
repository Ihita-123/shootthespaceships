import pgzrun

WIDTH= 500
HEIGHT= 700

ship = Actor("ship")
ship.x= WIDTH//2
ship.y= HEIGHT-100
ship.dead=False
enemy=[]

for x in range (8):
    for y in range(4):
        enemy.append(Actor("enemy"))
        enemy[-1].x=100+40*x
        enemy[-1].y=0+20*y

def update():
    if ship.dead==False:
        if keyboard.left:
            ship.x-=2
        if keyboard.right:
            ship.x+=2



def draw():
    screen.fill("blue")
    ship.draw()
    for enemies in enemy:
        enemies.draw()

pgzrun.go()