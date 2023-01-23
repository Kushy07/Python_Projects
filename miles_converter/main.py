from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to km Converter")
window.minsize(width=40, height=120)
window.config(padx=20,pady=20)


# Labels
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)
label_1.config(padx=10)
label_1.config(font=('Helvetica bold', 16))


label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)
label_2.config(padx=10)
label_2.config(font=('Helvetica bold', 16))
label_3 = Label(text=0)

label_3.grid(row=1, column=1)
label_3.config(padx=10)
label_3.config(font=('Century 12', 26))

label_4 = Label(text="kms")
label_4.grid(row=1, column=2)
label_4.config(padx=10)
label_4.config(font=('Helvetica bold', 16))
# Buttons
def action():
    # print("Do something")
    kms = round(1.609*int(entry.get()))
    label_3.config(text=f"{kms}")


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column= 1)
button.config(padx=10)
button.config(font=('Helvetica bold', 15))


# new_button.config(padx=10, pady=20)

# So, then it is not congest the place. Have some space around it.

# Entries
entry = Entry(width=10)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(row=0, column=1)


window.mainloop()