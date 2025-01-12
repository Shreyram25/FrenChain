import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import sys

# Constants
MY_YELLOW = "#FFD500"
MY_BROWN = "#B27530"

# Create the main window
root = tk.Tk()
root.title("Achievements")
root.attributes("-fullscreen", True)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to full screen
root.geometry(f"{screen_width}x{screen_height}")
allurabig = tkFont.Font(family="Allura", size=48, weight="bold")
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

heading_canvas = tk.Canvas(root, bg=MY_YELLOW, width=screen_width, height=screen_height//5)
heading_canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
heading_label = tk.Label(heading_canvas, text="Vos Plaques", font=allurabig, bg=MY_YELLOW, fg="black")
heading_label.pack(pady=20, padx=500, side="right")
back_image = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/a1d58dd0574d842308f9ca60833757f8/IMG_7532.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfEPp3hxI_w39Fh2FHabXnFH5IJ9GW93ZRHWtq5fyshP3fRQSXT9NO_Nq5iYL9x7IC0Na1zEJd16fjfv4clG9UmSAR9uJl8vdsh-tl1DNqmikiF9Ov6ejz0DKsr7ujF6nX", screen_width//10, screen_height//10)
back_button = tk.Button(heading_canvas, command=lambda: open_script("Home.py"), highlightthickness=0, image = back_image)
back_button.pack(side="left", fill="x", padx=0, pady=20)

# Create a frame for the top canvases
top_frame = tk.Frame(root, bg=MY_YELLOW)
top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Manually create top canvases
top_canvas1 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture1 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/24842e8cd400a29975f6de97e688d396/IMG_7539.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfTObiilaDsI_hq4KXpaBL-ZSiKodKbwJmnio7fX0zrCNxZuzRIIirfH_RnVYhK29WQaUR7TawJ-j6SIE571sCa0rGXQ4XUv9oAm6Q1uNNyyCBzaUeuIcfB1ulFaU5l2yQ=", screen_width//5, screen_height*2//5)
top_canvas1.create_image(0, 0, anchor=tk.NW, image=picture1)

top_canvas2 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture2 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/69eb43323ecd2754ccc5b09057de8c01/IMG_7540.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOze6pA6LabDCC03MP4Ernxo5SRIiIvyrgR5NPcsZthe9yAl3b_LzITFdMkZ0UmoCilRUPeCYcvgsnwWgqwEHtIdPqKJFsCoVJAgGEII_oFN_A8Yy8h_LRfk_PM6LvQ368rs=", screen_width//5, screen_height*2//5)
top_canvas2.create_image(0, 0, anchor=tk.NW, image=picture2)

top_canvas3 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture3 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/02a2e1fbd18cf9f593deb03466af34ac/IMG_7541.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYv8qvckilovo84pYEMxUEKOcABIv63UME4pfVMbQtszbgGBMLVaGpWG9LFOP4I-xwRQ-3JwQiAwrzaw085i9LLv1k276gHH8k87HUOHOgk0v8=", screen_width//5, screen_height*2//5)
top_canvas3.create_image(0, 0, anchor=tk.NW, image=picture3)

top_canvas4 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture4 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/9f858faa075510a603fca73b02cb5036/IMG_7542.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0M6evLT5L1I_AGjy8AKgqnTL6-ediDjxSyS842J54--ntjtPyU7jvc22xBCILJidIW5M-oLpfayVJWxmffo8ENsu-Qv_8y84msi5tXePfBYK8=", screen_width//5, screen_height*2//5)
top_canvas4.create_image(0, 0, anchor=tk.NW, image=picture4)

top_canvas5 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture5 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/98a1d721339906fc30b2ab3b23c0d286/IMG_7543.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MxuKYkMuVZ4rlo2eYvtgUm7fVZ_y6J4w4PKQGG-JhZ7H0H64F-RnRpynQuJ0npGl2x9cubTS3VvrU4ZlFcjUAj7gjaWNg3xalikFNNkDQoG0=", screen_width//5, screen_height*2//5)
top_canvas5.create_image(0, 0, anchor=tk.NW, image=picture5)

# Create a frame for the bottom canvases
bottom_frame = tk.Frame(root, bg=MY_YELLOW)
bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Manually create bottom canvases
bottom_canvas1 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture6 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/91fd0b42f97f50cfdd67c9acbfdeb166/IMG_7544.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxNPzey2dY6CC76EftXJ0MmKsK3DUNbSe4GB6aGt-jOGXx44VdkE7GP6LvdpsWxfZUOwUKQvoKgUk2eetgrBU6CXUdxGXA9V9RKjKI7oJJQLv901x3Q8GyOI-tX1dga9E=", screen_width//5, screen_height*2//5)
bottom_canvas1.create_image(0, 0, anchor=tk.NW, image=picture6)

bottom_canvas2 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture7 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/ab22b62da1b47d81b3df83ed4e0ceb00/IMG_7545.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcttbWblVBcrtjzlrLfyvWfNkn7OtS_6P3_KQYL989CYRyXMMIHoC4fYDBHCodIwiuoTtPogkPg-AWjlNlnn_wpaA_uN3VlWbwOjaiXOodTKmU1U60KZKbfT5SMiCJbqVc=", screen_width//5, screen_height*2//5)
bottom_canvas2.create_image(0, 0, anchor=tk.NW, image=picture7)

bottom_canvas3 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture8 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/40d75e58cb2373c90ffffb4ba1178708/IMG_7546.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzenSVTIzXx48zpMtveqC8NmB6Exh6k0d0B0qyAFA1txb-Kue9VKLM1rVFA6BwCsyC7q153v7UFwVJpnxd-oLDzXPkAONp7-RaYWJ8FxrYpicPDH7DsjnXup8M1vi8DnHWk=", screen_width//5, screen_height*2//5)
bottom_canvas3.create_image(0, 0, anchor=tk.NW, image=picture8)

bottom_canvas4 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture9 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/7700645d3167db292bc3fe103be4ec70/IMG_7547.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzebLajaIv9b92DI7GQgO4RrsugFrFL947Mp1fChD3NtLn5xLsCtNhfy_2yI2_MejDiGBaaA5J6Azd7Tlhk2sJzF9gLUhqvZX5467kfVm5QYJCzPdAG4Gucvk7TUyPlHbXg=", screen_width//5, screen_height*2//5)
bottom_canvas4.create_image(0, 0, anchor=tk.NW, image=picture9)

bottom_canvas5 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture10 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c1dece3848e88581b17b76581c5fceac/IMG_7548.jpg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RkZovlM4x6FkuXMbCeS7tlaIxw01OFBOPo1H2dXUa2dXJXeg2_bvWu9ktMH6nV77X5Eyq_kOYeD8dHJ4ERBxurV16hOu9j0Me9gZgMPXu8xo=", screen_width//5, screen_height*2//5)
bottom_canvas5.create_image(0, 0, anchor=tk.NW, image=picture10)

countdown(time_left)

root.mainloop()
