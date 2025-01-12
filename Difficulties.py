import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import sys

# Define constants
myyellow = "#FFD500"
image_refs = []  # Keep references to images to avoid garbage collection

# Create the main window
root = tk.Tk()
root.title("Difficulties")
root.geometry("1920x1080")
root.attributes("-fullscreen", True)

screen_height = root.winfo_screenheight()
screen_width = root.winfo_screenwidth()

# Calculate the widths of the canvases
canvas1_width = int(screen_width * (1 / 4))
canvas2_width = int(screen_width * (1 / 2))
canvas3_width = int(screen_width * (1 / 4))

# Create the canvases
canvas1 = tk.Canvas(root, width=canvas1_width, height=1080, bg=myyellow, highlightthickness=0)
canvas2 = tk.Canvas(root, width=canvas2_width, height=1080, bg=myyellow, highlightthickness=0)
canvas3 = tk.Canvas(root, width=canvas3_width, height=1080, bg=myyellow, highlightthickness=0)

# Arrange the canvases horizontally
canvas1.pack(side="left", fill="y", padx=0, pady=0)
canvas2.pack(side="left", fill="y", padx=0, pady=0)
canvas3.pack(side="left", fill="y", padx=0, pady=0)

# Load and display the image in canvas1 from a URL
image_url1 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/1b83d07e1cb42ffa5aa7175717ffb862/image_2_2.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxvy3UQHPwxtzT0ukNhvQDAd2ThTu0uFCDuHq_yjuMM11SFHJVdhHUzzUdDpeDtqdbY7Y2DATBafRjbLtmKbyEBILc0Ef0DCqAPWqHjbs6_M6Legg4sPayHXje_p5MT1Vs9J2Igdb0ntud2Mo7rAiq"
try:
    response = requests.get(image_url1)
    image = Image.open(BytesIO(response.content))
    new_width = int(screen_width * (1 / 4))
    new_height = int(screen_height - (0.13 * screen_height))
    image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas1.create_image(0, 0, anchor="nw", image=photo)
    canvas1.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

# Define a function to open different Python scripts
# Define a function to open different Python scripts and exit the current one
def open_script(script_name):
    try:
        # Launch the specified script
        subprocess.Popen([sys.executable, script_name, str(remaining)])
        # Exit the current script
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")

# Load and display three images as buttons in canvas2
def add_button(canvas, image_url, script_name, y_offset):
    try:
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
        new_width = screen_width // 2
        new_height = int((1 / 3) * (screen_height - (0.13 * screen_height)))
        image = image.resize((new_width, new_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_refs.append(photo)  # Keep a reference to avoid garbage collection

        # Create the button with the image as its background
        button = tk.Button(
            canvas,
            image=photo,               # Set the button image
            command=lambda: open_script(script_name),
            bd=0,                      # No border
            highlightthickness=0,      # No focus border
            bg=myyellow,               # Match the canvas background
            activebackground=myyellow  # Prevent color change on click
        )
        canvas.create_window(0, y_offset, anchor="nw", window=button)
        return new_height
    except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
        messagebox.showerror("Image Error", f"The image could not be loaded: {e}")
        return 0

    
if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")

def countdown(time_left):
    global remaining
    minutes, seconds = divmod(time_left, 60)
    if time_left > 0:
        remaining = time_left
        root.after(1000, countdown, time_left - 1)
        print(f"Time Left: {minutes:02}:{seconds:02}")
        print(remaining)

# Image URLs and corresponding scripts
button1 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/932f694eda5d400b3e60dded53dd71da/Image_30_12_2024_at_8_03_PM.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MFTuFlnFilKGUGpiIRsCrs9syux8she9xNpH8rCugeG2iDkAS5EWpgT95OSUnx3F0ilopIiLfmja8co1fZnGUxz1vPH3jjrOYp90DB_MUlB_78SKd7DTHHnwzw7L-EWB1UlaLwsrThDl7uN1tRYgWTA=="
button2 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/6e332f4ed3088c4c97dbacd70a78ed00/Image_30_12_2024_at_8_04_PM.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5EtT-EQuMAetsMYpeOE0O_uoTdWEusUaa2-geOibEPtAU9FfkARr7yC741TM3K9V_GY0HZvSxF2FdIqXHI3OM0ZlDbvHo9wZJTK4oDsZr_fRH-g7RdjoRb2JdBj3mJ9gJ3ZbrY-jKTAwiRhlSMJrTHA=="
button3 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/cebc3637451780fbdc4c11670fee8ef4/Image_30_12_2024_at_8_05_PM.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RFYKriLej5puMuG0jX0VlWsgAUVSo1wqoToGcJaRO8d-_WOpcnB9_ZZ39EuuN16FYO_11757PL48fT8qdWMQUX_4vZmkOhHOA4r_HLVFlrX1h8ofrcOx8R7nL_JFkBK5htcxjNDyYE2XUTu0mUmy-YQ=="

y_offset = 0
y_offset += add_button(canvas2, button1, "Home.py", y_offset)
y_offset += add_button(canvas2, button2, "Home.py", y_offset)
y_offset += add_button(canvas2, button3, "Home.py", y_offset)

# Load and display the image in canvas3
image_url2 = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/06cdd9097b1cb3b92db448c29484f45d/Image_31_12_2024_at_12_08_AM.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvFruWGnmZO-gNivEDY3fg19gTwfP_fNSxX4svwT0Y4VW8wIGYY1EPRyYv6Ev1u5oDiFCLeT_GylmXJ6uX-nELXgMBFZVoCmUkGc3HiU5CKNphcUmLQIUHiPIqZggshLKXZCCo3R4iYWo5OYMQcEYbAA=="
try:
    response = requests.get(image_url2)
    image = Image.open(BytesIO(response.content))
    new_width = int(screen_width * (1 / 4))
    new_height = int(screen_height - (0.13 * screen_height))
    image = image.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    canvas3.create_image(0, 0, anchor="nw", image=photo)
    canvas3.image = photo  # Keep a reference
except (UnidentifiedImageError, requests.exceptions.RequestException) as e:
    messagebox.showerror("Image Error", f"The image could not be loaded: {e}")

countdown(int(time_left))
# Run the application
root.mainloop()