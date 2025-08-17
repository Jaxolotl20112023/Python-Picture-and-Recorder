import numpy as np
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import turtle

xpos1 = -200
ypos1 = 0 

xpos2 = 100
ypos2 = 0 
amount_img = 0
amount_video = 0

wn = turtle.Screen()
wn.bgcolor("white")

pen = turtle.Turtle()
pen.color("black")
pen.speed(30)
pen.hideturtle()

pen.up()
pen.goto(-115,30)
pen.down()

pen.write("LOADING...", font=('Courier', 30, 'normal'))
pen.color("white")

pen.up()
pen.goto(-315,100)
pen.down()

pen.write("Jaxon's Photo And Recorder", font=('Courier', 30, 'normal'))


cap = cv2.VideoCapture(1)

def take_picture(cap) :

    global amount_img
    name = str(amount_img) 

    print("creating frame")
    ret, frame = cap.read()
    print(ret)

    if ret:
        cv2.imshow(name, frame)     
        IMGname = turtle.textinput("Name Picture", "Name of IMG File: ") 
        nameIMG = IMGname+".png"   
        cv2.imwrite(nameIMG, frame)  
        cv2.waitKey(0)                      
        cv2.destroyWindow(name)    
    else:
        print("Failed to capture image.")

    amount_img += 1
    
def take_video(cap) :
    Videoname = turtle.textinput("Name Video", "Name of Video File: ")
    nameVideo = Videoname+".avi"

    video = VideoWriter(nameVideo, VideoWriter_fourcc(*'MP42'), 25.0,(640,480))
    while True: 
        stream, frame = cap.read()

        if stream :
            cv2.imshow('Webcam', frame)
            video.write(frame)
        
        if cv2.waitKey(1) & 0xFF == 27: break

    cv2.destroyAllWindows()

def makeButton(x_pos, y_pos, width, height, text) : 
    pen.up()
    pen.setx(x_pos)
    pen.sety(y_pos) 
    pen.down()

    for i in range(2) :
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.up()
    pen.goto(x_pos+7,y_pos+6)
    pen.write(text, font=('Courier', 12, 'normal'))

def button_click(x,y) :
    if x < 0 and x > xpos1 and y > 0 and y < 30 :
        print("Start")
        take_picture(cap)
    elif x > 0 and x < 201 and y > 0 and y < 30 :
        print("Start Recording")
        take_video(cap)

makeButton(xpos1, ypos1, 130, 30, "Take Picture")
makeButton(xpos2, ypos2, 115, 30, "Take Video")
wn.bgcolor("black")

wn.onscreenclick(button_click, 1)
wn.listen()
turtle.done()

wn.exitonclick()
