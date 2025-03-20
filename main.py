#Modules
import tkinter
from tkinter import*
import os
from PIL import Image, ImageTk
import cv2

#We create the main window
mw=Tk()
mw.geometry('800x600')
icon = tkinter.PhotoImage(file="icon.png")
mw.iconphoto(True, icon)
mw.title('Choose your pokemon and see how they evolve!')
mw.config(bg='Black')

#Heading of the window
headingFrame=Frame(mw,bg='black',bd=5)
headingFrame.place(relx=0.11,rely=0.05,relwidth=0.75,relheight=0.1)
headingLabel=Label(headingFrame,text='Choose your pokemon and see how they evolve!',bg='white',font=('lato',18,'bold'))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

cur_path=os.getcwd()+'\\images'
#We create the buttons to choose a pokemon
img1=Image.open(cur_path+'\\Bulbasaur\\001.png')
img1 = img1.resize((120, 120))
img1 = ImageTk.PhotoImage(img1)
button1 = Button(mw, image=img1, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Bulbasaur'))
button1.place(relx=0.15, rely=0.3, relwidth=0.2, relheight=0.2)

img2=Image.open(cur_path+'\\Charmander\\004.png')
img2 = img2.resize((120, 120))
img2 = ImageTk.PhotoImage(img2)
button2 = Button(mw, image=img2, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Charmander'))
button2.place(relx=0.38, rely=0.3, relwidth=0.2, relheight=0.2)

img3=Image.open(cur_path+'\\Squirtle\\007.png')
img3 = img3.resize((120, 120))
img3 = ImageTk.PhotoImage(img3)
button3 = Button(mw, image=img3, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Squirtle'))
button3.place(relx=0.61, rely=0.3, relwidth=0.2, relheight=0.2)

img4=Image.open(cur_path+'\\Chikorita\\152.png')
img4 = img4.resize((120, 120))
img4 = ImageTk.PhotoImage(img4)
button4 = Button(mw, image=img4, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Chikorita'))
button4.place(relx=0.15, rely=0.52, relwidth=0.2, relheight=0.2)

img5=Image.open(cur_path+'\\Cyndaquil\\155.png')
img5 = img5.resize((120, 120))
img5 = ImageTk.PhotoImage(img5)
button5 = Button(mw, image=img5, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Cyndaquil'))
button5.place(relx=0.38, rely=0.52, relwidth=0.2, relheight=0.2)

img6=Image.open(cur_path+'\\Totodile\\158.png')
img6 = img6.resize((120, 120))
img6 = ImageTk.PhotoImage(img6)
button6 = Button(mw, image=img6, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Totodile'))
button6.place(relx=0.61, rely=0.52, relwidth=0.2, relheight=0.2)

img7=Image.open(cur_path+'\\Treecko\\252.png')
img7 = img7.resize((120, 120))
img7 = ImageTk.PhotoImage(img7)
button7 = Button(mw, image=img7, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Treecko'))
button7.place(relx=0.15, rely=0.74, relwidth=0.2, relheight=0.2)

img8=Image.open(cur_path+'\\Torchic\\255.png')
img8 = img8.resize((120, 120))
img8 = ImageTk.PhotoImage(img8)
button8 = Button(mw, image=img8, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Torchic'))
button8.place(relx=0.38, rely=0.74, relwidth=0.2, relheight=0.2)

img9=Image.open(cur_path+'\\Mudkip\\258.png')
img9 = img9.resize((120, 120))
img9 = ImageTk.PhotoImage(img9)
button9 = Button(mw, image=img9, font='Lato 12 bold', bg='gray', fg='white', padx=2,command= lambda:evolution('Mudkip'))
button9.place(relx=0.61, rely=0.74, relwidth=0.2, relheight=0.2)

#We define an array that will be used in the evolution function
array=[]

#We define the evolution function, that has as argument the name of the pokemon that the user chose.
#The function creates a video with the pokemon images and their evolutions.
def evolution(pokemon):
    path = os.path.join(cur_path, pokemon)
    file=os.listdir(path)
    #With a for loop we join all the images of the pokemon chosen in an array.
    for i in range(0,3):
        nameFile=file[i]
        pathFile=path+'\\'+nameFile
        img = cv2.imread(pathFile)
        array.append(img)

    #Later we create a video with the images of the array.
    video = cv2.VideoWriter('video.mp4', cv2.VideoWriter.fourcc(*'mp4v'), 0.5, (475, 475))

    for i in range(0,len(array)):
        video.write(array[i])
    video.release()

    #We call the show_video function
    show_video()

    #After the evolutions are displayed, the main window (or mw) is closed.
    mw.destroy()

#We define the show_video function.
#This function shows the images of the video that was created in the evolution function.
def show_video():
    #We open the video that was created.
    cap=cv2.VideoCapture('video.mp4')
    while cap.isOpened():
        ret,im=cap.read()
        if ret==False: break
        cv2.putText(im, 'Press any key to see how evolves!  ', (30, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                    (155, 155, 155), 2, cv2.LINE_4)
        #Every image is showed until the video is over.
        cv2.imshow('image',im)
        #To change the image of the window the user can use any key.
        cv2.waitKey(0)


mw.mainloop()