from tkinter import *

questions = [
    'What is the capital of spain?',
    'What is the capital of India?',
    'What is the capital of england',
    'Which state is the largest producer of sugarcane in India?',
    'What is the tallest mountain in the world?',
    'What is the largest ocean on Earth?',
    'What is the currency of Japan?',
    'Which is the longest river in the world?',
    'What is the capital of France?',
    'What is the driest desert in the world?',
    'What is the largest country in South America?',
    'What is the national language of China?',
    'What is the most populous city in the world?',
    'When was the first successful flight?',
    'Who painted the Mona Lisa?'
]

A = ['Madrid', 'Mumbai', 'Manchester', "Maharashtra", 'Mount Everest', 'Atlantic Ocean', 'Yen', 'Nile River', 'Paris', 'Atacama Desert', 'Brazil', 'Mandarin', 'Tokyo', '1903', 'Leonardo daVinci']
B = ['Barcelona', 'Delhi', 'Birmingham', "Karnataka", 'K2', 'Pacific Ocean', 'Yuan', 'Amazon River', 'Berlin', 'Sahara Desert', 'Argentina', 'Cantonese', 'Shanghai', '1912', 'Vincent van Gogh']
C = ['Valencia', 'Kolkata', 'London', "Madhya Pradesh", 'Kangchenjunga', 'Indian Ocean', 'Won', 'Yangtze River', 'Rome', 'Gobi Desert', 'Colombia', 'Wu', 'Mexico City', '1896', 'Michelangelo']
D = ['Seville', 'Chennai', 'Southampton', "Uttar Pradesh", 'Lhotse', 'Arctic Ocean', 'Rupee', 'Congo River', 'Vienna', 'Australian Desert', 'Peru', 'Japanese', 'New York City', '1900', 'Sandro Botticelli']

correct_ans = ['Madrid', 'Delhi', 'London', 'Uttar Pradesh', 'Mount Everest', 'Pacific Ocean', 'Yen', 'Nile River', 'Paris', 'Atacama Desert', 'Brazil', 'Mandarin', 'Tokyo', '1903', 'Leonardo daVinci']

def select(event):
    b=event.widget
    value=b['text']
    print(value)

    for i in range(15):
        if value==correct_ans[i]:
            if value==correct_ans[14]:

                def playagain():
                    winwindow.destroy()
                    qstntextarea.delete(1.0,END)
                    qstntextarea.insert(END,questions[0])

                    btnA.config(text=A[0])
                    btnB.config(text=B[0])
                    btnC.config(text=C[0])
                    btnD.config(text=D[0])

                    amountlabel.config(image=amountimg)

                def close():
                    winwindow.destroy()
                    window.destroy()

                winwindow=Toplevel()
                winwindow.title('You won!')
                winwindow.geometry('500x400+100+100')
                winwindow.config(bg='black')
                imglabel=Label(winwindow,image=centerimg,bg='black')
                imglabel.pack(pady=15)
                winlabel=Label(winwindow,text='You won!',bg='black',fg='white',font=('Arial',20))
                winlabel.pack()
                playagainbtn=Button(winwindow,text='Play again',font=('Arial',16,'bold'),width=15,fg='white',bg='black',bd=0,cursor='hand2',command=playagain)
                playagainbtn.pack()
                closebtn=Button(winwindow,text='Close',font=('Arial',16,'bold'),width=15,fg='white',bg='black',bd=0,cursor='hand2',command=close)
                closebtn.pack()

                happyimg=PhotoImage(file='happy.png')
                happylabel1=Label(winwindow,image=happyimg,bg='black')
                happylabel1.place(x=30,y=280)
                happylabel2=Label(winwindow,image=happyimg,bg='black')
                happylabel2.place(x=400,y=280)

                winwindow.mainloop()
                break

            qstntextarea.delete(1.0,END)
            qstntextarea.insert(END,questions[i+1])

            btnA.config(text=A[i+1])
            btnB.config(text=B[i+1])
            btnC.config(text=C[i+1])
            btnD.config(text=D[i+1])
            amountlabel.config(image=amtimages[i+1])

        if value not in correct_ans:

            def tryagain():
                newwindow.destroy()
                qstntextarea.delete(1.0,END)
                qstntextarea.insert(END,questions[0])

                btnA.config(text=A[0])
                btnB.config(text=B[0])
                btnC.config(text=C[0])
                btnD.config(text=D[0])

                amountlabel.config(image=amountimg)

            def close():
                newwindow.destroy()
                window.destroy()

            newwindow=Toplevel()
            newwindow.title('You lost')
            newwindow.geometry('500x400+100+100')
            newwindow.config(bg='black')
            imglabel=Label(newwindow,image=centerimg,bg='black')
            imglabel.pack(pady=15)
            lostlabel=Label(newwindow,text='That was the wrong answer!',bg='black',fg='white',font=('Arial',20))
            lostlabel.pack()
            tryagainbtn=Button(newwindow,text='Try again',font=('Arial',16,'bold'),width=15,fg='white',bg='black',bd=0,cursor='hand2',command=tryagain)
            tryagainbtn.pack()
            closebtn=Button(newwindow,text='Close',font=('Arial',16,'bold'),width=15,fg='white',bg='black',bd=0,cursor='hand2',command=close)
            closebtn.pack()

            sadimg=PhotoImage(file='sad.png')
            sadlabel1=Label(newwindow,image=sadimg,bg='black')
            sadlabel1.place(x=30,y=280)
            sadlabel2=Label(newwindow,image=sadimg,bg='black')
            sadlabel2.place(x=400,y=280)

            newwindow.mainloop()
            break

window=Tk()
window.geometry("1270x652+0+0")
window.config(bg="black")

leftframe=Frame(window,bg="black",padx=90)
leftframe.grid(row=0,column=0)

topframe=Frame(leftframe,bg="black",pady=15)
topframe.grid(row=0,column=0)

centerframe=Frame(leftframe,bg="black",pady=15)
centerframe.grid(row=1,column=0)

bottomframe=Frame(leftframe,bg='black')
bottomframe.grid(row=2,column=0)

rightframe=Frame(window,bg="black",padx=60,pady=15)
rightframe.grid(row=0,column=1)

# image50=PhotoImage(file="50-50.png")
# btn50=Button(topframe,image=image50,bg="black",bd=0,activebackground="black",width=180,height=80)
# btn50.grid(row=0,column=0)

# imageaudience=PhotoImage(file="audiencePole.png")
# btnaudience=Button(topframe,image=imageaudience,bg="black",bd=0,activebackground="black",width=180,height=80)
# btnaudience.grid(row=0,column=1)

# imagephone=PhotoImage(file="phone.png")
# btnphone=Button(topframe,image=imagephone,bg="black",bd=0,activebackground="black",width=180,height=80)
# btnphone.grid(row=0,column=2)

centerimg=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\center.png',width=300,height=200)
logolabel=Label(centerframe,image=centerimg,bg="black")
logolabel.grid(row=0,column=0)

amountimg=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture0.png')
amountimg1=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture1.png')
amountimg2=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture2.png')
amountimg3=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture3.png')
amountimg4=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture4.png')
amountimg5=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture5.png')
amountim6=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture6.png')
amountimg7=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture7.png')
amountimg8=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture8.png')
amountimg9=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture9.png')
amountimg10=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture10.png')
amountimg11=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture11.png')
amountimg12=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture12.png')
amountimg13=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture13.png')
amountimg14=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture14.png')
amountimg15=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\Picture15.png')

amtimages=[amountimg,amountimg1,amountimg2,amountimg3,amountimg4,amountimg5,amountim6,amountimg7,amountimg8,amountimg9,amountimg10,amountimg11,amountimg12,amountimg13,amountimg14,amountimg15]

amountlabel=Label(rightframe,image=amountimg,bg="black")
amountlabel.grid(row=0,column=0)

layoutimg=PhotoImage(file='C:\\Users\\ROSHAN\\Desktop\\Vs Code\\Python\\Tkinter\\KBC Random\\lay.png')
layoutlabel=Label(bottomframe,image=layoutimg,bg='black')
layoutlabel.grid(row=0,column=0)

qstntextarea=Text(bottomframe,font=('Arial',17,'bold'),wrap='word',height=2,width=35,bg='black',fg='white',bd=0)
qstntextarea.place(x=65,y=10)

qstntextarea.insert(END,questions[0])

optnA=Label(bottomframe,text='A.',font=('Arial'),bg="black",fg="white",bd=0)
optnA.place(x=65,y=110)

btnA=Button(bottomframe,text=A[0],font=('Arial'),bg="black",fg="white",bd=0,width=12,height=2)
btnA.place(x=97,y=96)

optnB=Label(bottomframe,text='B.',font=('Arial'),bg="black",fg="white",bd=0)
optnB.place(x=350,y=110)

btnB=Button(bottomframe,text=B[0],font=('Arial'),bg="black",fg="white",bd=0,width=12,height=2)
btnB.place(x=382,y=96)

optnC=Label(bottomframe,text='C.',font=('Arial'),bg="black",fg="white",bd=0)
optnC.place(x=65,y=195)

btnC=Button(bottomframe,text=C[0],font=('Arial'),bg="black",fg="white",bd=0,width=12,height=2)
btnC.place(x=97,y=182)

optnD=Label(bottomframe,text='D.',font=('Arial'),bg="black",fg="white",bd=0)
optnD.place(x=350,y=195)

btnD=Button(bottomframe,text=D[0],font=('Arial'),bg="black",fg="white",bd=0,width=12,height=2)
btnD.place(x=382,y=182)

btnA.bind('<Button-1>',select)
btnB.bind('<Button-1>',select)
btnC.bind('<Button-1>',select)
btnD.bind('<Button-1>',select)

window.mainloop()