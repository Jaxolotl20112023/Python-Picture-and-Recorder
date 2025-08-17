import numpy as np
import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
import turtle

# position of the picture button
xpos1 = -200
ypos1 = 0 

# position of the video button
xpos2 = 100
ypos2 = 0 

# labels for the windows
amount_img = 0
amount_video = 0 

# set up the window screen
wn = turtle.Screen()
wn.bgcolor("white")

# set up the turtle/pen
pen = turtle.Turtle()
pen.color("black")
pen.speed(30)
pen.hideturtle()

# Create loading screen
pen.up()
pen.goto(-115,30)
pen.down()

pen.write("LOADING...", font=('Courier', 30, 'normal'))
pen.color("white")

# Write title of the program on screen
pen.up()
pen.goto(-315,100)
pen.down()

pen.write("Jaxon's Photo And Recorder", font=('Courier', 30, 'normal'))

# Writes the info at the bottom left corner
pen.up()
pen.goto(-365,-350)
pen.down()

pen.write("Press ESC to stop recording/taking picture", font=('Courier', 10, 'normal'))

# get the camera to be used to take pictures and videos
cap = cv2.VideoCapture(1)

# function that will take the pictures
def take_picture(cap) :
    # pop up input window to put the name of the picture
    IMGname = turtle.textinput("Name Picture", "Name of IMG File: ") 
    nameIMG = IMGname+".png"   

    # taking a picture using the camera
    print("creating frame")
    ret, frame = cap.read()

    # checks if it took the picture successfully 
    if ret:
        # if so, show the picture on screen in 'Picture Webcam' 
        cv2.imshow('Picture Webcam', frame)       

        # save the picture to the folder the program is in
        cv2.imwrite(nameIMG, frame)  

        # wait till any key is pressed before closing window
        if cv2.waitKey(0) & 0xFF == 27:                      
            cv2.destroyWindow('Picture Webcam')    
    else:
        # if the camera couldn't take a pic
        print("Failed to capture image.")

    
# function that will take the videos
def take_video(cap) :
    # request the name of the video recording
    Videoname = turtle.textinput("Name Video", "Name of Video File: ") 
    nameVideo = Videoname+".avi" # add the .avi file type 

    # create the file where the video will be saved
    video = VideoWriter(nameVideo, VideoWriter_fourcc(*'MP42'), 25.0,(640,480))

    # record
    while True: 
        ret, frame = cap.read() # start recording

        # checks if recording was successful
        if ret :   
            cv2.imshow('Video Webcam', frame) # show the video feed in a window
            video.write(frame) # save the video to a file 
        else :
            # if failed then print 'Recording failed' 
            print("Recording failed") 
        
        # checks if the escape key is pressed
        if cv2.waitKey(1) & 0xFF == 27: 
            break

    # destroys the window
    cv2.destroyAllWindows()

# function that makes the buttons
def makeButton(x_pos, y_pos, width, height, text) : 
    # move the turtle to the correct location 
    pen.up() 
    pen.setx(x_pos)
    pen.sety(y_pos) 
    pen.down()

    # draws the box of the button
    for i in range(2) :
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

    # goes to the left side of the button 
    pen.up()
    pen.goto(x_pos+7,y_pos+6)
    # writes the text
    pen.write(text, font=('Courier', 12, 'normal'))

# function that checks if either button was clicked
def button_click(x,y) :
    # checks if the mouse is touching the picture button
    if x < 0 and x > xpos1 and y > 0 and y < 30 :
        print("Start") 
        take_picture(cap) # if true call the take_picture function
    elif x > 0 and x < 201 and y > 0 and y < 30 : # checks if the mouse is touching the video button
        print("Start Recording")
        take_video(cap) # if true call the take_video function

# calls the two button functions 
makeButton(xpos1, ypos1, 130, 30, "Take Picture")
makeButton(xpos2, ypos2, 115, 30, "Take Video")

# changes the window background to black to see the text
wn.bgcolor("black")

# actively checking if a click happened 
wn.onscreenclick(button_click, 1)
wn.listen()
turtle.done()

# enables the turtle window to close
wn.exitonclick()
