import customtkinter as ctk
import webbrowser

root = ctk.CTk()
root.title("Codédex Random Exercise")
root.geometry("350x250")

video = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

def play_video():
    webbrowser.open(video)


label = ctk.CTkLabel(root, text="Welcome to the\nawesome random\nexercise from\nCodédex", font=("Consolas", 24))
label.pack(pady= 25)

button = ctk.CTkButton(root, text="Hit Me!", font=("Consolas", 18), command=play_video).pack()


root.mainloop()
