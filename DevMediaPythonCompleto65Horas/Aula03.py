import pygame


cols = ['#0000ff','#0000aa','#000088','#000055','#000033','#000011']

w, h = 700, 500
y = h/6

d = pygame.display.set_mode(w,h)

for i , c in enumerate(cols):
    d.fill(pygame.color(c), rect=(0,i*y,w,y*(i+1)))

pygame.display.flip()
pygame.image.save(d,'Gradient.png')
