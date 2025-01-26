import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import requests
from io import BytesIO
import subprocess
import sys

MY_YELLOW = "#FFD500"
MY_BROWN = "#B27530"

root = tk.Tk()
root.title("Break")
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(f"{screen_width}x{screen_height}")
allurabig = tkFont.Font(family="Allura", size=48 , weight="bold")
allurabig2 = tkFont.Font(family="Allura", size=36, weight="bold")

def get_image(url, width, height):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except (requests.RequestException, UnidentifiedImageError) as e:
        messagebox.showerror("Image Error", f"Could not load image from {url}. Error: {e}")
        return None

def open_script(script_name):
    try:
        subprocess.Popen([sys.executable, script_name, str(2700)])
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

def startTimer():
    countdown(600)

def countdown(time_left):
    time_left = int(time_left)
    minutes, seconds = divmod(time_left, 60)
    row2_label3.config(text=f"Time Left: {minutes:02}:{seconds:02}")
    if time_left > 0:
        root.after(1000, countdown, time_left - 1)
    else:
        resume_button.config(state="normal") 

def on_q_key(event):
    resume_button.config(state="normal")

if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")

'''def countdown(time_left):
    global remaining
    time_left = int(time_left)
    minutes, seconds = divmod(time_left, 60)
    if time_left > 0:
        remaining = time_left
        root.after(1000, countdown, time_left - 1)
        print(f"Time Left: {minutes:02}:{seconds:02}")
        print(remaining)'''

row1_canvas = tk.Canvas(root, width=screen_width, height=screen_height//3 +20, bg=MY_YELLOW, highlightthickness=0)
row1_canvas.pack(side="top", fill="both", padx=0, pady=0)
row1_canvas.pack_propagate(False)
row1_label1 = tk.Label(row1_canvas, text="Wow! You've been at it", font=allurabig, bg=MY_YELLOW)
row1_label1.pack(side="top", fill="both", padx=0, pady=10)
row1_label2 = tk.Label(row1_canvas, text="for 45 minutes straight!", font=allurabig, bg=MY_YELLOW)
row1_label2.pack(side="top", fill="both", padx=0, pady=10)

row2_canvas = tk.Canvas(root, width=screen_width, height=screen_height//2, bg=MY_YELLOW, highlightthickness=0)
row2_canvas.pack(side="top", fill="both", padx=0, pady=0)

row2_canvas1 = tk.Canvas(row2_canvas, width=screen_width//3, height=screen_height//3, bg=MY_YELLOW, highlightthickness=0)
row2_canvas1.pack(side="left", fill="both", padx=80, pady=0)
row2_label1 = tk.Label(row2_canvas1, text="Be back in 10", font=allurabig, bg=MY_YELLOW)
row2_label1.pack(side="top", fill="both", padx=0, pady=0)
row2_label2 = tk.Label(row2_canvas1, text="minutes to", font=allurabig, bg=MY_YELLOW)
row2_label2.pack(side="top", fill="both", padx=0, pady=0)
row2_label3 = tk.Label(row2_canvas1, text="resume!", font=allurabig, bg=MY_YELLOW)
row2_label3.pack(side="top", fill="both", padx=0, pady=0)

row2_canvas2 = tk.Canvas(row2_canvas, width=screen_width//3, height=screen_height//3, bg=MY_YELLOW, highlightthickness=0)
row2_canvas2.pack(side="left", fill="both", padx=50, pady=0)

break_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/99a7e7714119855278648ef7dc82a4ff/IMG_7066.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MCDX1aOw3V1rqVjThqwbFifgjfMTgINDnYOOqIHnktUrfoYnr2XjTRNg_lt8lqVa6JK2LXgqy-NvtVcc6GEJx5VuY-7M0wcV1SSS8c14oFATKyelPutDtxcFeYyqqE6N2", screen_width//3, screen_height//3)

row2_canvas2.create_image(screen_width//6, screen_height//6, image=break_image, anchor='center')  

row2_canvas3 = tk.Canvas(row2_canvas, width=screen_width//3, height=screen_height//3, bg=MY_YELLOW, highlightthickness=0)
row2_canvas3.pack(side="left", fill="both", padx=0, pady=0)
row2_label3 = tk.Label(row2_canvas3, text="Time Left: 10:00", font=allurabig, bg=MY_YELLOW)
row2_label3.pack(side="top", fill="both", padx=0, pady=0)
resume_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/096dc112412b0475736d02ef151ba014/IMG_7535.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvvkT1aZphbD2tmGdIzjMtqGUExWZU5CTxfi_EayvjJZ13CrTrFgBE_O658xU0ZanZI_K42EW_QycJJD2PWXGg4YKMnR7a-_e8zTa859YbWCsrOJmjTKOUxUxjFe6z9b6o", screen_width//3 -20, screen_height//6)
resume_button = tk.Button(row2_canvas3, command=lambda: open_script("Home.py"), highlightthickness=0, image=resume_image, width=screen_width//3 -20, height=screen_height//6, state="disabled")
resume_button.pack(side="top", fill="both", padx=30, pady=0)  

row3_canvas = tk.Canvas(root, width=screen_width, height=screen_height//3, bg=MY_YELLOW, highlightthickness=0)
row3_canvas.pack(side="bottom", fill="both", padx=0, pady=0)
row3_canvas.pack_propagate(False)
row3_label1 = tk.Label(row3_canvas, text="It's time for you to take a break,", font=allurabig, bg=MY_YELLOW)
row3_label1.pack(side="top", fill="both", padx=0, pady=10)
row3_label2 = tk.Label(row3_canvas, text="unplug, take a walk, refil your", font=allurabig, bg=MY_YELLOW)
row3_label2.pack(side="top", fill="both", padx=0, pady=10)
row3_label3 = tk.Label(row3_canvas, text="water and relax your eyes.", font=allurabig, bg=MY_YELLOW)
row3_label3.pack(side="top", fill="both", padx=0, pady=10)

startTimer()
root.bind('<q>', on_q_key)
root.mainloop()
