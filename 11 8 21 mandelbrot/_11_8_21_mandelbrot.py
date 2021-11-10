#Mandelbrot Set Program
#Graphs the Mandelbrot set iteratively (function is NOT recursive)
#Written by Dr. Mo, Fall 2019
import pygame
import math
import cmath
import threading

pygame.init()  
pygame.display.set_caption("mandelbrot")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))

#mandelbrot function definition------------------------ 
def mandelbrot(c, zoomLevel,resolution):
    z = complex(0,0);
    count = 0;
    while abs(z) < 2 and count < 80 and int(resolution*zoomLevel*200+400)+count < 800 and int(zoomLevel*resolution * 200 + 400) > 0: 
        z = z * z + c;
        count+=1;
    return count;
#end mandelbrot function--------------------------------

#-------------------------------------------------------
#in C++, this would be the start of main

def run():
    #pygame.init()
    zoomLevel = 3
    t = -2/zoomLevel #lower bound for real axis
    offset = 0
    
    events=pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    while t<2/(zoomLevel): #upper bound for real (horizontal) axis
        
        t+=.001 #make this number SMALLER to increase picture resolution

        m = -2/zoomLevel #lower bound for imaginary axis
        while m<2/(zoomLevel): #upper bound for imaginary (vertical) axis
            
                    
            m+=.001 #make this number SMALLER to increase picture resolution
        
            c = complex(t, m) #create a complex number from iterators
            num = mandelbrot(c, zoomLevel, t) #call the function

            #these if statements are just to differentiate the colors more, not needed if you want black & white image
            if num < 20:
                screen.set_at(((int(zoomLevel * t * 200 + 400)+offset), (int(zoomLevel * m * 200 + 400))+offset), (num*6, num*12, num*12))
            elif num<40:
               screen.set_at(((int(zoomLevel * t * 200 + 400)+offset), (int(zoomLevel * m * 200 + 400))+offset), (num*2, num/2, num*4))
            elif num is 80:
               screen.set_at(((int(zoomLevel * t * 200 + 400)+offset), (int(zoomLevel * m * 200 + 400))+offset), (2,255,255))
            else:
               screen.set_at(((int(zoomLevel * t * 200 + 400)+offset), (int(zoomLevel * m * 200 + 400))+offset), (num*3, num/2, num*2))

        pygame.display.flip()#this actually puts the pixel on the screen
        

t1 = threading.Thread(target=run)
t2 = threading.Thread(target=run)
#t3 = threading.Thread(target=run)
#t4 = threading.Thread(target=run)
t1.start()
t2.start()
pygame.time.wait(10000)
#t3.start()
#t4.start()
#pygame.time.wait(10000)#pause to see the picture
#pygame.quit()#quit pygame
