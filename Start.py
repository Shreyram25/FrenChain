import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import sys

# Initialize the main window
root = tk.Tk()
root.title("Start")
root.geometry("1920x1080")
root.attributes("-fullscreen", True)

remaining = 0



def countdown(time_left):
    global remaining
    minutes, seconds = divmod(time_left, 60)
    if time_left > 0:
        remaining = time_left
        root.after(1000, countdown, time_left - 1)
        print(f"Time Left: {minutes:02}:{seconds:02}")
        print(remaining)

def on_start():
    global remaining
    subprocess.Popen([sys.executable, "Difficulties.py", str(remaining)])
    sys.exit()

def on_achievements():
    global remaining
    subprocess.Popen([sys.executable, "Profile.py", str(remaining)])
    sys.exit()

def on_games():
    global remaining
    subprocess.Popen([sys.executable, "CurrentGames.py", str(remaining)])
    sys.exit()

def open_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.mainloop()

# Define the color variables
myyellow = "#FFD500"
mybrown = "#B27530"

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# Create font styles
allurabig = tkFont.Font(family="Allura", size=48, weight="bold")
button_font = tkFont.Font(family="Helvetica", size=18)  # Define button font
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def get_image(url, width, height):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)



# Load the main image
main_url = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/acf1cf423d2f579d1bf2a52fa90aad5a/IMG_6999.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfASmvLY8uiiXnM-TM_QHw4C26QJbqF1fpPy2OetH4EEGSv76uFczN2rWs1FjiRuKCSSBgnrQ58QITkb7yRB8mH2dKPpTdySMJJQD01USZLwIXElRoylnQcV-jTCZ0cKU3"
overlay_url = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/633e668c64f6bf13757f0e291c7f01f2/image.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5anUIQQrGYJUXVE27ttqtdnjyw1b9M9SXjEJyjxgsJMl7yTKeC97neUDH34KPl-02Vqrs3KB3aevxA0VBDCHINZZu2tnV6mBi11xe0uLxZDI="

avatar_canvas = tk.Canvas(root, width=screen_width//5, height=screen_height, bg=myyellow, highlightthickness=0)
avatar_canvas.pack(side="left", fill="y", padx=0, pady=0)
avatar_image = get_image(overlay_url, int(screen_width//5), int(screen_height/2))
avatar_canvas.create_image(0, (screen_height/2)-80, anchor="nw", image=avatar_image)

eiffel_canvas = tk.Canvas(root, width=screen_width*2//5, height=screen_height, bg=myyellow, highlightthickness=0)
eiffel_canvas.pack(side="left", fill="y", padx=0, pady=0)
eiffel_image = get_image(main_url, int(screen_width*2//5), int(screen_height))
eiffel_canvas.create_image(0, 0, anchor="nw", image=eiffel_image)

start_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/2ad5999f1192fe361fdd2c9a5450f896/IMG_7527.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfTObiilaDsI_hq4KXpaBL-8ii4P3fNdfgLuaooRsyhAm22Fw6oYOUp-24v0XPMhLSz-zrFz03SlDhkBJXFmBqiUtrpDj9fFjYR8WGqkd7Gzj9YKzXAd03oQVF1TzbpdNJw_2c5plck4VOcMp3H6rGg", screen_width//3, screen_height//6)
achievements_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/df9e9d5811c761e9d3d8ff1c70f2d3b2/IMG_7538.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdqOyto4Kc4wWO-KPNTRwzNXrhEkgoPJTgIgC4FoGL5EQgLKScY-2690zzVhllOJ2gL07LdUAMoLyyvQBwz0MaoAXDaK87dgEqLvimuz9ev-Oqgy8NQjjMcnOD8h0Njo68uy2AgXHpu1zEqWaz6DgCS", screen_width//3, screen_height//6)
games_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/e082572c30f77b74a6e870f7b3055dd1/IMG_7529.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzd5ipp8wJ0jQxjmOFcT-PFjIz8a_MhZi4foD7jpBgWChyT-bF4jDOygfZBgwnIr8tRXIHifqkz_-ASoL2kESyFOdAG02YC1-_wwh1629Qxsc0o7NXNO9w6ufErfFCj0TJJ5G1o9IamGfuw-sy7KiIBE", screen_width//3, screen_height//6)

buttons_canvas = tk.Canvas(root, width=screen_width*2//5, height=screen_height, bg=myyellow, highlightthickness=0)
buttons_canvas.pack(side="left", fill="y", padx=0, pady=0)
label = tk.Label(buttons_canvas, text="FrenChain", font=allurabig, bg=myyellow)
label.place(x=screen_width//10, y=screen_height//6)
start_btn = tk.Button(buttons_canvas, command=on_start, image = start_image)
start_btn.place(x=20, y=screen_height//3 - 50)
achievements_btn = tk.Button(buttons_canvas, command=on_achievements, image = achievements_image)
achievements_btn.place(x=20, y=screen_height//2)
games_btn = tk.Button(buttons_canvas, command=on_games, image = games_image)
games_btn.place(x=20, y=screen_height*2//3 + 50)

if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
    countdown(int(time_left))
else:
    print("No variable received.")
    countdown(2700)

root.mainloop()