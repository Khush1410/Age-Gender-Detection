import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy as np

from keras.models import load_model
model=load_model('Age_sex_detection.h5')

top=tk.Tk()
top.geometry('800x600')
top.title('Age and Gender Detector')
top.configure(background='#CDCDCD')

label1=Label(top,background='#CDCDCD',font=('arial',25,'bold'))
label2=Label(top,background='#CDCDCD',font=('arial',25,'bold'))
sign_image=Label(top)

def Detect(file_path):
    global label_packed
    # image=Image.open(file_path)
    # image=image.resize(48,48)
    # image=np.expand_dims(image,axis=0)
    # image=np.array(image)
    # image=np.delete(image,0,1)
    # image=np.resize(image,(48,48,3))
    # print(image.shape)
    # sex_f=['Male','Female']
    # image=np.array([image])/255
    # pred=model.predict(image)
    # age=int(np.round(pred[1][0]))
    # sex=int(np.round(pred[0][0]))
    # print("Predicted age is " + str(age))
    # print("Predicted gender is " + sex_f[sex])
    image = cv2.imread(file_path)
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image=cv2.resize(image,(48,48))


    print(image.shape)
    sex_f=['Male','Female']
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print("Predicted age is " + str(age))
    print("Predicted gender is " + sex_f[sex])
    label1.configure(foreground="#011638",text=str(age))
    label2.configure(foreground="#011638",text=sex_f[sex])


#defining show_detect button function
def show_Detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background='#364156',foreground='white',font=('arial',10,'bold'))
    Detect_b.place(relx=0.79,rely=0.46)


def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')

        show_Detect_button(file_path)
    except:
        pass

upload=Button(top,text='Upload an Image',command=upload_image,padx=10,pady=15)
upload.configure(background="#364156",foreground="white",font=('arial',10,'bold'))
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand='true')

label1.pack(side='bottom',expand='true')
label2.pack(side='bottom',expand='true')
heading=Label(top,text='Age and Gender',pady=20,font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()