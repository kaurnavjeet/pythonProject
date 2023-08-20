import customtkinter

# Create a random password generator
# On clicking generate, create a 8-12 character long password
#  contains at least 1 special character and 1 number

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")


def random_password_generator():
    print("Password Generated")


button = customtkinter.CTkButton(master=app, text="Generate Random Password", command=random_password_generator())
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()