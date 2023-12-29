from tkinter import *
FONT=("Arial",14,"normal")

def miles_to_km():
    miles=float(input.get())
    km_value["text"]=str(round(miles*1.609,2))

window=Tk()
window.title("Miles to Kilometers")
window.config(padx=20,pady=20)

input=Entry(width=10)
input.focus()
input.grid(column=1,row=0)

miles_lbl=Label(text="Miles" , font=FONT)
miles_lbl.grid(padx=10,column=2,row=0)

equal_lbl=Label(text="is equal to" , font=FONT)
equal_lbl.grid(column=0,row=1)

km_value=Label(text="0" , font=FONT)
km_value.grid(padx=10,column=1,row=1)

km_lbl=Label(text="Km" , font=FONT)
km_lbl.grid(column=2,row=1)

calculate_btn=Button(text="Calculate",command=miles_to_km)
calculate_btn.grid(pady=10,column=1,row=2)

window.mainloop()