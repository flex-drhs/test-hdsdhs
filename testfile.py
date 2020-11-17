import tkinter

window=tkinter.Tk()
window.title("연습장")
window.geometry("400x400")

def 글자나오기():
    entry1.insert("end", "글자가 나와요")

def 글자지우기():
    entry1.delete(0, "end")

def 끄기():
    window.destroy()

entry1=tkinter.Entry(window, width=50)
entry1.grid(row=0, columnspan=3)

button1=tkinter.Button(window, width=10, text="출 력", command=lambda:글자나오기())
button1.grid(row=1, column=0)

button2=tkinter.Button(window, width=10, text="삭 제", command=lambda:글자지우기())
button2.grid(row=1, column=1)

button3=tkinter.Button(window, width=10, text="종 료", command=lambda:끄기())
button3.grid(row=1, column=2)


tkinter.mainloop() #요건 항상 맨 밑에 위치해야한다.


