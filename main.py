import customtkinter
import random
import string

# Create a random password generator
# On clicking generate, create a 8-12 character long password
#  contains at least 1 special character and 1 number

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("600x440")

output_label = customtkinter.CTkLabel(master=app, text="", font=("Arial", 18))


def random_password_generator():
    random_password = ""
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(13):
        random_password += ''.join(random.choice(characters))
    output_label.configure(text=random_password)


button = customtkinter.CTkButton(master=app, text="Generate Random Password", command=random_password_generator,
                                 border_spacing=10)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

output_label.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER, )

app.mainloop()
