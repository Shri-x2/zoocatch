import pgzrun, random, time

WIDTH, HEIGHT = 800, 600
TITLE = "Animal Connection"

lion = []
n=random.randint(5,10)
for i in range(n):
    lion.append(Actor("lion", (random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30))))
timebeg = time.time()
print(timebeg)
nextlion = 0

def draw():
    screen.blit("zoo2", (0, 0))
    for i,s in enumerate(lion):
        s.draw()
        screen.draw.text(str(i+1), (s.x, s.y+20), color="blue", fontsize=20)
pgzrun.go()
            