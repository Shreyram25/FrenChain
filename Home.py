import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import sys

myyellow = "#FFD500"
mybrown = "#B27530"

# Create the main window
root = tk.Tk()
root.title("Home")
root.attributes("-fullscreen", True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to full screen
root.geometry(f"{screen_width}x{screen_height}")

def on_q_key(event):
    global time_left, remaining, proceed
    remaining = 0
    proceed = True
    open_script("Break.py")

def open_script(script_name):
    global remaining, proceed
    try:
        if script_name == "CurrentGames.py":
            proceed = messagebox.askokcancel("...", "Are you sure you want to proceed with your current level?")
        elif script_name == "PreviousGames.py":
            proceed = messagebox.askokcancel("...", "Are you sure you want to redo your previous level? All progress in the current level will be lost.")
        elif script_name == "RestartGames.py":
            proceed = messagebox.askokcancel("...", "Are you sure you want to restart the entire unit? All progress in the current unit will be lost.")
        if proceed == True:
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
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")
    time_left = 2700

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

# Create the first canvas
canvas1 = tk.Canvas(root, width=screen_width, height=screen_height // 2, bg=myyellow, highlightthickness=0)
canvas1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

image_url1 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/d311d0f95174d15e58d5cc3617a9e602/IMG_7424.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdqOyto4Kc4wWO-KPNTRwzNCJzPTrKxQbysCVbTwRl1KJtgcPP4rAMvAJPNw7gj1GzSORAu5ldv0mMXeCualn2sC-ZMlKNybpMAeSYE10qxzsHV-VHtCa86IL4n_YcHq9k="
try:
    response = requests.get(image_url1)
    image = Image.open(BytesIO(response.content))
    new_width = int(screen_width)
    new_height = int(screen_height // 2)
    image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, anchor="nw", image=photo)
    canvas1.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

# Create the second canvas
canvas2 = tk.Canvas(root, width=screen_width, height=screen_height // 2, bg=myyellow)
canvas2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

child_canvas1_width = screen_width // 5
child_canvas2_width = 3 * (screen_width // 5)
child_canvas3_width = screen_width // 5
child_canvas_height = screen_height // 2
grandchild_canvas_height = child_canvas_height // 3

# Create three child canvases inside canvas2
child_canvas1 = tk.Canvas(canvas2, width=child_canvas1_width, height=child_canvas_height, bg=myyellow, highlightthickness=0)
child_canvas2 = tk.Canvas(canvas2, width=child_canvas2_width, height=child_canvas_height, bg=myyellow, highlightthickness=0)
child_canvas3 = tk.Canvas(canvas2, width=child_canvas3_width, height=child_canvas_height, bg=myyellow, highlightthickness=0)

canvas2.create_window((0, 0), window=child_canvas1, anchor="nw")
canvas2.create_window((child_canvas1_width, 0), window=child_canvas2, anchor="nw")
canvas2.create_window((child_canvas1_width + child_canvas2_width, 0), window=child_canvas3, anchor="nw")

# Load and place the image on child_canvas1
image_url2 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/6b3f9629f911603538f69896c899087d/IMG_7425.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5CwHvNILc5MKT9cAEpMfX-WAGddgv_Rh2K8297RwBb0rngCWFSELv3Ss8Ttm15wWnA4-hpAUpc-1MvtHLslwYKEl-kc7HA2P0JtSCIjKB7W4="  # Replace with your image URL
try:
    response = requests.get(image_url2)
    image = Image.open(BytesIO(response.content))
    image = image.resize((child_canvas1_width, child_canvas_height-20), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    child_canvas1.create_image(0, 0, anchor="nw", image=photo)
    child_canvas1.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

image_url3 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/5716ba5e4364c939e897a4062e7e4201/IMG_7426.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfhUhZTA5OeWcEGM3iGX6ZoC2O6C-UTLJF9KmMbWJI4o2fpxsc59UB1z7CIK1sxscrgkxmvVfYLtFICoElWPn-z6-ftj5MyH5Pxi-4Ww9MEd1V2_zDawkHJ3ml2qEZGhBQ="  # Replace with your image URL
try:
    response = requests.get(image_url3)
    image = Image.open(BytesIO(response.content))
    image = image.resize((child_canvas3_width, child_canvas_height-20), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    child_canvas3.create_image(0, 0, anchor="nw", image=photo)
    child_canvas3.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

grandchild_canvas1 = tk.Canvas(child_canvas2, width=child_canvas2_width, height=grandchild_canvas_height, bg=myyellow, highlightthickness=0)
grandchild_canvas2 = tk.Canvas(child_canvas2, width=child_canvas2_width, height=grandchild_canvas_height, bg=myyellow, highlightthickness=0)
grandchild_canvas3 = tk.Canvas(child_canvas2, width=child_canvas2_width, height=grandchild_canvas_height, bg=myyellow, highlightthickness=0)

child_canvas2.create_window((0, 0), window=grandchild_canvas1, anchor="nw")
child_canvas2.create_window((0, grandchild_canvas_height), window=grandchild_canvas2, anchor="nw")
child_canvas2.create_window((0, 2 * grandchild_canvas_height), window=grandchild_canvas3, anchor="nw")


button1 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/981ca090672bfe5310c4758cf68ed59c/IMG_7427.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MNGi100RWk9JMZE-zjkjOvjrMpH12qiLGoffX4_2qxL4WKuaS8nTe0g5QCm6E90NuTAX2-Xqorl9D_etjbxOxdvsQn2xbHr_61DKhUxz6SG9wONyZRR3CXa7FayA20cuG"  # Replace with your image URL

# Download the image from the URL
response = requests.get(button1)
img_data = BytesIO(response.content)

# Open the image using PIL
image = Image.open(img_data)

# Resize the image to desired dimensions (e.g., 100x100)
resized_image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)

# Convert the resized image to a format that Tkinter can use
tk_image = ImageTk.PhotoImage(resized_image)

# Create a button with the resized image inside the canvas
button1_widget = tk.Button(grandchild_canvas1, image=tk_image, command=lambda: open_script("CurrentGames.py"))
button1_widget.image = tk_image  # Keep a reference to avoid garbage collection

# Place the button inside the canvas at a specific position
grandchild_canvas1.create_window(child_canvas2_width//2, grandchild_canvas_height//2, window=button1_widget)


button2 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/48435c96f74c1b6c6fc9203cf7b2f194/IMG_7428.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzenSVTIzXx48zpMtveqC8NmwHRJYB5cp2C3YGKIGjX5PQOePxbg0jRe3SXKB3KuqBIL75HWEknx8PRE-GFUGivwhACufYKmAE8xnEdU2YM6Vei_LTYw_mfRbDmgY-KomTmG8XVFpnuSoLthwRWZkP0z"  # Replace with your image URL

# Download the image from the URL
response = requests.get(button2)
img_data = BytesIO(response.content)

# Open the image using PIL
image = Image.open(img_data)

# Resize the image to desired dimensions (e.g., 100x100)
resized_image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)

# Convert the resized image to a format that Tkinter can use
tk_image = ImageTk.PhotoImage(resized_image)

# Create a button with the resized image inside the canvas
button1_widget = tk.Button(grandchild_canvas2, image=tk_image, command=lambda: open_script("PreviousGames.py"))
button1_widget.image = tk_image  # Keep a reference to avoid garbage collection

# Place the button inside the canvas at a specific position
grandchild_canvas2.create_window(child_canvas2_width//2, grandchild_canvas_height//2, window=button1_widget)


button3 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c37a6ff8cf447f5c97ae73453d35c745/IMG_7429.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RTeQL-BcEtXc77vqZtd_hEhr4CSAozFOE1_dxplo_RKALbPQwbIvgm9goMZVqc0XRvB6Uu0A_FuuaiVFdpsyb3SBu8_y5W4gqJ66Q7Be8JXS4izuFcyza5PdgOn90PCFW"  # Replace with your image URL

# Download the image from the URL
response = requests.get(button3)
img_data = BytesIO(response.content)

# Open the image using PIL
image = Image.open(img_data)

# Resize the image to desired dimensions (e.g., 100x100)
resized_image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)

# Convert the resized image to a format that Tkinter can use
tk_image = ImageTk.PhotoImage(resized_image)

# Create a button with the resized image inside the canvas
button1_widget = tk.Button(grandchild_canvas3, image=tk_image, command=lambda: open_script("RestartGames.py"))
button1_widget.image = tk_image  # Keep a reference to avoid garbage collection

# Place the button inside the canvas at a specific position
grandchild_canvas3.create_window(child_canvas2_width//2, grandchild_canvas_height//2, window=button1_widget)


'''button1 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/981ca090672bfe5310c4758cf68ed59c/IMG_7427.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MNGi100RWk9JMZE-zjkjOvjrMpH12qiLGoffX4_2qxL4WKuaS8nTe0g5QCm6E90NuTAX2-Xqorl9D_etjbxOxdvsQn2xbHr_61DKhUxz6SG9wONyZRR3CXa7FayA20cuG"  # Replace with your image URL
try:
    response = requests.get(button1)
    image = Image.open(BytesIO(response.content))
    image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    grandchild_canvas1.create_image(0, 0, anchor="nw", image=photo)
    grandchild_canvas1.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

button2 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/48435c96f74c1b6c6fc9203cf7b2f194/IMG_7428.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzenSVTIzXx48zpMtveqC8NmwHRJYB5cp2C3YGKIGjX5PQOePxbg0jRe3SXKB3KuqBIL75HWEknx8PRE-GFUGivwhACufYKmAE8xnEdU2YM6Vei_LTYw_mfRbDmgY-KomTmG8XVFpnuSoLthwRWZkP0z"  # Replace with your image URL
try:
    response = requests.get(button2)
    image = Image.open(BytesIO(response.content))
    image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    grandchild_canvas2.create_image(0, 0, anchor="nw", image=photo)
    grandchild_canvas2.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

button3 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c37a6ff8cf447f5c97ae73453d35c745/IMG_7429.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RTeQL-BcEtXc77vqZtd_hEhr4CSAozFOE1_dxplo_RKALbPQwbIvgm9goMZVqc0XRvB6Uu0A_FuuaiVFdpsyb3SBu8_y5W4gqJ66Q7Be8JXS4izuFcyza5PdgOn90PCFW"  # Replace with your image URL
try:
    response = requests.get(button3)
    image = Image.open(BytesIO(response.content))
    image = image.resize((child_canvas2_width, grandchild_canvas_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    grandchild_canvas3.create_image(0, 0, anchor="nw", image=photo)
    grandchild_canvas3.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")'''

# Run the Tkinter event loop
root.bind('<q>', lambda event: on_q_key(event))

countdown(time_left)
root.mainloop()