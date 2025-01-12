import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
import requests
from io import BytesIO
import subprocess
import sys

# Constants
MY_YELLOW = "#FFD500"
MY_BROWN = "#B27530"

# Create the main window
root = tk.Tk()
root.title("Games Page")
root.attributes("-fullscreen", True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to full screen
root.geometry(f"{screen_width}x{screen_height}")
allurabig = tkFont.Font(family="Allura", size=48 , weight="bold")
allurabig2 = tkFont.Font(family="Allura", size=36, weight="bold")

def open_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)

def on_q_key(event):
    open_script("Home.py")

def get_image(url, width, height):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        img = img.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except (requests.RequestException, UnidentifiedImageError) as e:
        messagebox.showerror("Image Error", f"Could not load image from {url}. Error: {e}")
        return None

def open_script(script_name):
    try:
        # Launch the specified script
        subprocess.Popen([sys.executable, script_name, str(remaining)])
        # Exit the current script
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")

def countdown(time_left):
    global remaining
    time_left = int(time_left)
    minutes, seconds = divmod(time_left, 60)
    if time_left > 0:
        remaining = time_left
        root.after(1000, countdown, time_left - 1)
        print(f"Time Left: {minutes:02}:{seconds:02}")
        print(remaining)
    else:
        open_script("Break.py")

heading_canvas = tk.Canvas(root, width=screen_width, height=screen_height//10, bg=MY_YELLOW, highlightthickness=0)
heading_canvas.pack(side="top", fill="x", padx=0, pady=0)
heading_canvas1 = tk.Canvas(heading_canvas, width=screen_width//5, height=screen_height//10, bg=MY_YELLOW, highlightthickness=0)
heading_canvas1.pack(side="left", fill="x", padx=0, pady=0)
back_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/a1d58dd0574d842308f9ca60833757f8/IMG_7532.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfEPp3hxI_w39Fh2FHabXnFH5IJ9GW93ZRHWtq5fyshP3fRQSXT9NO_Nq5iYL9x7IC0Na1zEJd16fjfv4clG9UmSAR9uJl8vdsh-tl1DNqmikiF9Ov6ejz0DKsr7ujF6nX", screen_width//10, screen_height//10)
back_button = tk.Button(heading_canvas1, command=lambda: open_script("Home.py"), highlightthickness=0, image = back_image)
back_button.pack(side="left", fill="x", padx=0, pady=0)
heading_label = tk.Label(heading_canvas, text="Level 1", font=allurabig, bg=MY_YELLOW)
heading_label.pack(side="right", fill="x", padx=500, pady=0)
heading_canvas2 = tk.Canvas(heading_canvas, width=screen_width*4//5, height=screen_height//10, bg=MY_YELLOW, highlightthickness=0)
heading_canvas2.pack(side="right", fill="x", padx=0, pady=0)
matching_canvas = tk.Canvas(root, width=screen_width, height=screen_height*9//20, bg=MY_YELLOW, highlightthickness=0)
matching_canvas.pack(side="top", fill="x", padx=0, pady=0)
matching_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/7d734d72db96df2f7c54770e1f98f969/IMG_7530.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzebLajaIv9b92DI7GQgO4Rr8KhxVH_blzoM3KnckanP9gylcnsj_LtZP5UB2VK7Z-VScWJVoNVkH8jqN025WPmFSyCErY4cIc5Au9j6htyh87-PWU-z4sqZhC77-EpPR-YXIoEYgNFR-bRkcQuZu8V-", screen_width, screen_height*9//20)
matching_button = tk.Button(matching_canvas, command=lambda: open_script("Matching Game.py"), image=matching_image, highlightthickness=0)
matching_button.pack(side="top", fill="x", padx=0, pady=0)
catching_canvas = tk.Canvas(root, width=screen_width, height=screen_height*9//20, bg=MY_YELLOW, highlightthickness=0)
catching_canvas.pack(side="bottom", fill="x", padx=0, pady=0)
catching_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/0fa439716c8582acad952ec580c55b05/IMG_7531.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvRV2p4W1Tmr74Y33qZay7N2rihHnfTVBcHovEsDv12Mn7PwnQS1G1U6uytXmmTcHtB97UAwM-Jwum9iIKZt4hJak7oS38g8zS-zr_bW1UcjyTFL_RqhzoDM2bWEeO_bJr", screen_width, screen_height*9//20 - 10)
catching_button = tk.Button(catching_canvas, command=lambda: open_script("Catching Game.py"), image=catching_image, highlightthickness=0)
catching_button.pack(side="bottom", fill="x", padx=0, pady=0)

countdown(time_left)  # 10 minutes in seconds
root.bind('<q>', on_q_key) 
root.mainloop()