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
LOGOUT_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/f2b41c0635bfe4f82ca49ac46aeffbcc/Image_03_01_2025_at_1_42_PM.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdrfw102NKhCFdQ4eCHKtNvjx71TWvL-MzYri82dNTkARkkAGlyifRFoyKyfbUaxkvStqqG5pBBe7lbneWvN5iojeZ0yjneXS6jzSuAC2I4ug55rzic5ZevwpK7cu4ThgyuP5i0HL-Ct9LqtkuU3K9fjkVn81iH99DTKcrd8QZE3g=="
PROFILE_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/66c8683152197f7ed7126d1655ce36df/New_Profile_Picture.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5gXGDn_xgJBo_S5acM3BlarZtOLNueq31txSBCPu5J-g0zIsgdykMZP_ZtVKVpad3Z9SefZ9VgxYOuc0skiRcvS7qW2m3r4lupeUGMljAaXUGDhbS7jMpiSI2tCHYOzOh"
LEVEL3_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/523ef8011f522556f1cd9e53d3d6cd50/IMG_7522.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfhUhZTA5OeWcEGM3iGX6ZoHwm_FZZgOSSmv3kdT8l5YnotjpTx_OQ-VGFpHo9yNgKZLMrlUAZMeBaI-7LcTdkb3BOKYAyEDEPp0fJZww6XkFxqCBxwHp3jySaBvrzs2Uo="
ACCURACY_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/e407ce0fb4db36d95ac7e16879c222cb/Image_03_01_2025_at_3_59_PM.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzd5ipp8wJ0jQxjmOFcT-PFjO_qZxtFkc9jKYrMQS070YEA7NeITm05msSskEk5ZYgZJe_pTO3FRhPYO_6DxTwuV4RfQnzGmx-VZ8JCqG2RzP0t1CFXqCT9SuRfVOPG8nah1OkLsJ3JKWUMeW_6K_-Kq4AFS91GTVG5wvxJhOlXXUA=="
ACCURACY_DETAILS_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/01f90ba0f45ea4d0eac9daaba2fa552c/Image_03_01_2025_at_4_21_PM.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvv9hVSVPKPxWR9c9bqsl7awO5H0cyF5wJZ7DcdSx7RHxaQ5MDlLjv54I-F6ushPvmj5xdJz9WVbODi3Ehmuk-Wzai3CpwZYh91OAcIElzpwprz5P87NdirPkOx9yhjxGEwcM_i69lLdnsTDBEWCtQnw=="
LEADERBOARD_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/939ed6d5fbb9d818277f734fecdf907e/IMG_7524.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MXH3L_qX75ZsAOUDz9WQ5hwWDoaD03VjERLp5gKk2nog-dbs0qpQIxifEUsormB8g5WOkf_mnJmdPpqF8-ChWkhnhV1fLeC0Ur6V7cQK6fTUOh0adhLWh9v7PE6UuOHTf"
LEADERBOARD_DETAILS_URL = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/a59057e81635e0adb1c4542589df6e91/IMG_7525.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfPaQ0SpSDcLSqvfuj4zUB6Lm-ocP078tL2HOMgsmUU_rKF6zprF8UgJXxeJR0S1O6SLaQRsmwZKfHbg8WqURSxsu3OuEac_aAMxxHM-gLe75_jr9haodBv1QJrtQ7OUqN"
remaining = None

# Create the main window
root = tk.Tk()
root.title("Profile")
root.attributes("-fullscreen", True)
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to full screen
root.geometry(f"{screen_width}x{screen_height}")
allurabig = tkFont.Font(family="Allura", size=48 , weight="bold")
allurabig2 = tkFont.Font(family="Allura", size=36, weight="bold")

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

def open_script(script_name, remaining):
    try:
        # Launch the specified script
        subprocess.Popen([sys.executable, script_name, str(remaining)])
        # Exit the current script
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

def open_script2(event, script_name, remaining):
    try:
        # Launch the specified script
        subprocess.Popen([sys.executable, script_name, str(remaining)])
        # Exit the current script
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

def open_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.mainloop()
    
if len(sys.argv) > 1:
    time_left = sys.argv[1]
    remaining = time_left
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

heading_canvas = tk.Canvas(root, bg=MY_YELLOW, highlightthickness=0)
heading_canvas.pack(side="top", fill="x")

heading_canvas1 = tk.Canvas(heading_canvas, bg=MY_YELLOW, highlightthickness=0)
heading_canvas1.pack(side="left", fill="both", expand=True)

greeting_label = tk.Label(heading_canvas1, text="Welcome to the Profile Page, Shreyram", font=allurabig, bg=MY_YELLOW)
greeting_label.pack(side="top", padx=10, pady=30)

heading_canvas2 = tk.Canvas(heading_canvas, bg=MY_YELLOW, highlightthickness=0)
heading_canvas2.pack(side="right", fill="both", expand=True)

logout_image = get_image(LOGOUT_URL, screen_width//4, screen_height//10)
logout_button = tk.Button(heading_canvas2, bg=MY_YELLOW, command=lambda: open_script("Start.py", remaining), image=logout_image)
logout_button.image = logout_image
logout_button.pack(side="top", pady=20)

banner_canvas = tk.Canvas(root, bg=MY_BROWN, highlightthickness=0, width=screen_width, height=(screen_height)//2)
banner_canvas.pack(side="top", fill="both", expand=True)

profile_image = get_image(PROFILE_URL, (screen_width*1)//5, (screen_height*4)//10)
banner_canvas1 = tk.Canvas(banner_canvas, bg=MY_BROWN, highlightthickness=0)
btn = tk.Button(banner_canvas1, bg=MY_BROWN, command=lambda: changepfp(), image=profile_image)
banner_canvas1.pack(side="left", fill="both", expand=True, padx=20)
btn.image = profile_image
btn.pack(side="left", fill="both", expand=True, padx=20)

# Create banner_canvas2 and pack it in the middle
banner_canvas2 = tk.Canvas(banner_canvas, bg=MY_BROWN, highlightthickness=0)
banner_canvas2.pack(side="left", fill="both", expand=True, padx = 60)  # Change to "left" to place it in the middle

# Create details_canvas1, details_canvas2, and details_canvas3 inside banner_canvas2
details_canvas1 = tk.Canvas(banner_canvas2, bg=MY_BROWN, highlightthickness=0)
details_canvas1.pack(side="top", fill="both", expand=True)
label1 = tk.Label(details_canvas1, text="Name: Shreyram Seetharaman", font=allurabig, bg=MY_BROWN, fg="white")
label1.pack(side="top", pady=10)

details_canvas2 = tk.Canvas(banner_canvas2, bg=MY_BROWN, highlightthickness=0)
details_canvas2.pack(side="top", fill="y", expand=True)
label2 = tk.Label(details_canvas2, text="Section: MYP 4 G", font=allurabig, bg=MY_BROWN, fg="white")
label2.pack(side="top", pady=10)

details_canvas3 = tk.Canvas(banner_canvas2, bg=MY_BROWN, highlightthickness=0)
details_canvas3.pack(side="top", fill="both", expand=True)
label3 = tk.Label(details_canvas3, text="ID: 12300400127396", font=allurabig, bg=MY_BROWN, fg="white")
label3.pack(side="top", pady=10)

# Create banner_canvas3 and pack it on the right
# Load the level3 image
level3_image = get_image(LEVEL3_URL, (screen_width*1)//5, (screen_height*4)//10)

# Create banner_canvas3 and pack it on the right
banner_canvas3 = tk.Canvas(banner_canvas, bg=MY_BROWN, highlightthickness=0, width=(screen_width*1)//5, height=(screen_height*4)//10)
btn = tk.Button(banner_canvas3, bg=MY_BROWN, command=lambda: open_script("CurrentGames.py"), image=level3_image)
banner_canvas3.pack(side="right", fill="both", expand=True)
btn.image = level3_image
btn.pack(side="right", fill="both", expand=True, padx=20)

boxes_canvas = tk.Canvas(root, bg=MY_YELLOW, highlightthickness=0, width=screen_width, height=screen_height//2)
boxes_canvas.pack(side="top", fill="x")

accuracy_canvas = tk.Canvas(boxes_canvas, bg=MY_BROWN, highlightthickness=0, height=(screen_height//2)-20, width=(screen_width//2)-10)
accuracy_canvas.pack(side="left", fill="y", expand=True, padx=10, pady=10)

accuracy_canvas1 = tk.Canvas(accuracy_canvas, bg=MY_BROWN, highlightthickness=0, width=(screen_width//10), height=(screen_height//2))
accuracy_canvas1.pack(side="left", fill="both", expand=True)
accuracy_image = get_image(ACCURACY_URL, (screen_width*1)//10, (screen_height*1)//10)
btn = tk.Button(accuracy_canvas1, bg=MY_BROWN, command=lambda: open_script("Achievements.py", remaining), image=accuracy_image, width=(screen_width*1)//10, height=(screen_height*1)//10)
btn.pack(side="top", fill="x", expand=True)
btn.image = accuracy_image
accuracy_canvas2 = tk.Canvas(accuracy_canvas, bg=MY_BROWN, highlightthickness=0)
accuracy_canvas2.pack(side="right", fill="both", expand=True)
accuracy_details_image = get_image(ACCURACY_DETAILS_URL, (screen_width*4)//10, (screen_height//2)-120)
btn = tk.Button(accuracy_canvas2, bg=MY_BROWN, command=lambda: open_script("Achievements.py", remaining), image=accuracy_details_image, width=(screen_width*4)//10, height=((screen_height//2)-100))
btn.pack(side="top", fill="x", expand=True)
btn.image = accuracy_details_image

leaderboard_canvas = tk.Canvas(boxes_canvas, bg=MY_BROWN, highlightthickness=0, height=(screen_height//2)-20, width=(screen_width//2)-10)
leaderboard_canvas.pack(side="right", fill="y", expand=True, padx=10, pady=10)

leaderboard_canvas1 = tk.Canvas(leaderboard_canvas, bg=MY_BROWN, highlightthickness=0, width=(screen_width//10), height=(screen_height//2))
leaderboard_canvas1.pack(side="left", fill="both", expand=True)
leaderboard_image = get_image(LEADERBOARD_URL, (screen_width*1)//10, (screen_height*1)//10)
btn = tk.Button(leaderboard_canvas1, bg=MY_BROWN, command=lambda: open_script("Achievements.py", remaining), image=leaderboard_image, width=(screen_width*1)//10, height=(screen_height*1)//10)
btn.pack(side="top", fill="x", expand=True)
btn.image = leaderboard_image
leaderboard_canvas2 = tk.Canvas(leaderboard_canvas, bg=MY_BROWN, highlightthickness=0)
leaderboard_canvas2.pack(side="right", fill="both", expand=True)
leaderboard_details_image = get_image(LEADERBOARD_DETAILS_URL, ((screen_width*4)//10)-50, (screen_height//2)-120)
btn = tk.Button(leaderboard_canvas2, bg=MY_BROWN, command=lambda: open_script("Achievements.py", remaining), image=leaderboard_details_image, width=((screen_width*4)//10)-50, height=((screen_height//2)-100))
btn.pack(side="top", fill="x", expand=True)
btn.image = leaderboard_details_image

root.bind('<q>', lambda event: open_script2(event, "Start.py", remaining))

countdown(time_left)
root.mainloop()