import customtkinter
from tkinter import IntVar


def crypt():
    entry.delete("1.0", "end")
    ratio = radiobutton_var.get()
    mytext = eingabe_entry.get()
    key = keyentry.get()

    mylst = []
    
    for x in range(0, len(mytext)):

        if ratio == 1:
            n_letter = ord(mytext[x])+int(key)
            c_item = chr(n_letter)
            mylst.append(c_item)

        if ratio == 2:
            n_letter = ord(mytext[x])-int(key)
            ch = chr(n_letter)
            mylst.append(ch)

    aus_text= "".join(mylst)

    #ausgabe.configure(text=aus_text)
    entry.insert("1.0", aus_text)
    


   

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



root = customtkinter.CTk()
root.geometry("500x500")
#root.resizable(False, False)
root.title("Caeser-Encryption")


frame = customtkinter.CTkFrame(master=root, width=480, height=480)
frame.place(y=10, x=10)



keyentry = customtkinter.CTkEntry(master=frame, placeholder_text="Key (Integer)", placeholder_text_color="grey", width=300, height=33, show="*")
keyentry.place(y=30, x=100)


eingabe_entry = customtkinter.CTkEntry(master=frame, width=300, height=33, text_color="black", placeholder_text="Input", placeholder_text_color="black", fg_color="grey")
eingabe_entry.place(y=80, x=100)

radiobutton_var = IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame, variable=radiobutton_var, value=1, text="encryt")
radiobutton_1.place(y=155, x=240)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame, variable=radiobutton_var, value=2, text="decrypt")
radiobutton_2.place(y=186, x=240)

button = customtkinter.CTkButton(master=frame, text="convert", command=crypt, width=100)
button.place(y=250, x=200)

entry = customtkinter.CTkTextbox(master=frame,width=460, height=170, font=("Arial", 20))
entry.place(y=300, x=10)

root.mainloop()