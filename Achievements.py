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
picture3 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/02a2e1fbd18cf9f593deb03466af34ac/IMG_7541.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ_-aRbpFRYF3k4iGjKgYDLAefPh3EG-l6u_BKrsea8gqQf1PAyBBoKxDibrzChYISjnMuvTu7Uar2Lnv4P-2Uh-3fi41ayZ3VkF9OJANKrlFBQuyFZX_7a1OGz1k3nWoVw==", screen_width//5, screen_height*2//5)
top_canvas3.create_image(0, 0, anchor=tk.NW, image=picture3)

top_canvas4 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture4 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/9f858faa075510a603fca73b02cb5036/IMG_7542.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ0YdSrRPAK29G9uf2vXdTSiENQjb8SB3-mCbVY7ASDMwVZYAWNtpe4CXZF57PSqfHSIsdVfIE24szNoLiXWDXizqAZjlhBPKlnK3RuQ71Gs_U2YBnWxHhbzRnDV8OpWy7g==", screen_width//5, screen_height*2//5)
top_canvas4.create_image(0, 0, anchor=tk.NW, image=picture4)

top_canvas5 = tk.Canvas(top_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
top_canvas5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture5 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/98a1d721339906fc30b2ab3b23c0d286/IMG_7543.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ0THvUPyBu47TqyvjSjcyH-0ld6uHOGmkylrc9Wcsrv4vSxei-f-LfA-A1M6Jwcq0MZkRieEOH0teoHbrBbqh48vPYr7Pdhyykhanl4pJdz0Inymr15dptdGgGCJIWGJ1g==", screen_width//5, screen_height*2//5)
top_canvas5.create_image(0, 0, anchor=tk.NW, image=picture5)

# Create a frame for the bottom canvases
bottom_frame = tk.Frame(root, bg=MY_YELLOW)
bottom_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Manually create bottom canvases
bottom_canvas1 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture6 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/91fd0b42f97f50cfdd67c9acbfdeb166/IMG_7544.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ8MOI37mOwfUlcNnhSCdjb2EynGrbto-EFlAiI53rxoa_OOIu7tKmuQe7cCkGZSHcCxLKCJ1m-5Lk6z7F7GFtp3n10qiWMI1LJL0H3ESYWU2FQYgQLaexgsgCgiF23uqXA==", screen_width//5, screen_height*2//5)
bottom_canvas1.create_image(0, 0, anchor=tk.NW, image=picture6)

bottom_canvas2 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture7 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/ab22b62da1b47d81b3df83ed4e0ceb00/IMG_7545.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ3i_DK-6c8ExXNkSevK6YM6UmNLXkhjFYbnhsvRuR1cHu8SxfLDlJsBZvRTxRwx6-2hiRJh7dxbpCBozw2zGN_e0eFi2Ifv_LDE8k5LtCU3cIOC-uHwuDI4ggE8WUnLCew==", screen_width//5, screen_height*2//5)
bottom_canvas2.create_image(0, 0, anchor=tk.NW, image=picture7)

bottom_canvas3 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture8 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/40d75e58cb2373c90ffffb4ba1178708/IMG_7546.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ6yDdsb2lZr9c0IVnK-OE4ZLoVFdGDw-gA2Pa_zxk9A_RFRJGPbRIZPnWExiy9RadsNwIn8gD6_6fll5hwxpjzK1EPi8TZKWQiJOfXcxfUiSV-mA1exvccrgpkiHjAoOUw==", screen_width//5, screen_height*2//5)
bottom_canvas3.create_image(0, 0, anchor=tk.NW, image=picture8)

bottom_canvas4 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture9 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/7700645d3167db292bc3fe103be4ec70/IMG_7547.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ62yDmzLKrAi9_cdoIWWHyaQQUa43yfPug4t4ciPVbYaEQVR_BaqdXxIPE9QlmPvj3-ZXgbH0MchNk7-uqqe-89pC7zxHUC8bH3NM3bi5P3CkQzWe0qVH-b_JSk8zzx-tg==", screen_width//5, screen_height*2//5)
bottom_canvas4.create_image(0, 0, anchor=tk.NW, image=picture9)

bottom_canvas5 = tk.Canvas(bottom_frame, bg=MY_YELLOW, width=screen_width//5, height=screen_height*2//5)
bottom_canvas5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
picture10 = get_image("https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c1dece3848e88581b17b76581c5fceac/IMG_7548.jpg?expiry_token=5WaHZRdGG3LkUVQGy3SZ-zdRtq89aJeottSBaF_Hii8EGDVBG-vnLc5ZfL_2GiKosWMOCkHArMcc8LorETHcZ7CG3D7yPd8whmZ8tSgeJijisekf1fHbhxqVkMZ-V4_f1wEvz7cG-BGOSQS39sZTnoLaJQOgPB5iFIlfslhtJ5UDj2mU2y8aP0pCoQhK-IUTMyicJcjbELfLvx68rlXuPQ==", screen_width//5, screen_height*2//5)
bottom_canvas5.create_image(0, 0, anchor=tk.NW, image=picture10)

countdown(time_left)

root.mainloop()