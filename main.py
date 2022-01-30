from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=250)
window.configure(bg="white")
window.config(padx=20, pady=40)

# text
miles = Label(text="Miles", font=("Arial", 18, "bold"), bg='white', fg='black')
miles.grid(column=3, row=0)
miles.config(pady=2, padx=2)

# text
km = Label(text="Km", font=("Arial", 18, "bold"), bg='white', fg='black')
km.grid(column=3, row=1)
km.config(pady=2, padx=2)

# text
equal_to = Label(text="is equal to", font=("Arial", 18, "bold"), bg='white', fg='black')
equal_to.grid(column=0, row=1)
equal_to.config(pady=2, padx=2)


# button
def button_clicked():
    new_text = input.get()
    finished_text = round(float(new_text) * 1.60934, 2)
    output.config(text=finished_text)


button = Button(text="Calculate", font=("Arial", 18), bg='white', fg='black', relief="raised", command=button_clicked)
button.grid(column=1, row=2)
button.config(pady=2, padx=2)

# input
input = Entry(width=10, bg='white', fg='black')
print(input.get())
input.grid(row=0, column=1)

# output
output = Label(text="0", font=("Arial", 18, "bold"), bg='white', fg='black')
output.grid(column=1, row=1)
output.config(pady=2, padx=2)

window.mainloop()
