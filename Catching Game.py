import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk, UnidentifiedImageError
import requests
from io import BytesIO
import subprocess
import sys
from random import randint, choice

root = tk.Tk()
root.title("Catching Game")
root.geometry("1920x1080")  
root.attributes("-fullscreen", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

def get_image(url, width, height):
    response = requests.get(url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

allurabig = tkFont.Font(family="Allura", size=48, weight="bold")
allurabig2 = tkFont.Font(family="Allura", size=36, weight="bold")

score = 0
finished = 0
myyellow = "#FFD500"
urls = [
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/87a4e8eb3ed8e1406f77470a0ae78ae9/IMG_7015.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfuu-rUBucKMsyHdudQh4mOXomYV21pB6gRi3tbWej733rSnviD6QCjHP_Hc5rqipAyO77fOAAby7f1ThV2l6EG8rDi0hivu2D9c8s5YNzGsVwd5NUkZYl49BvkPiDiUGXjB2OBLHkNtXkdYpeUcMdk",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/2a1c13b3392f7fbdff16a9bac78157f6/IMG_7016.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfTObiilaDsI_hq4KXpaBL-hmxfO5amhAWUnwCGy3Twpyy7tsak3qYDgvQFH-qMYpXqOk5IT8zmruUNSZlHD7vIBPb4_AilyAUolPPbVyvbnIW5-Y5ydGsbHcV42hn12Q1yp4epIMtbyu7HJGuYHKT2",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/498ed8a7b1c939c963501c8821b1689e/IMG_7017.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzenSVTIzXx48zpMtveqC8NmzVtuIBqQ307bIVlYiDGNDhi4DyZcQ3ZpzJF7tWG09bvx4iYVbgHGOgCUKr1flZR937L5lCp9Z6fPS-14-BlTLGvspgjj7T-l6MMN7PJloJmTd5iZjAgSSq8a4Sos7HY0",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/bd62b918e5eebf68ff1f70266928b91b/IMG_7019.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdiduYQEOxhjcxvboQPKgA638BvvUx5ZwLi-YYT4cmuC-vVzgGWOWIHHIBxA7p7sysiumM4R3tt7qsyOE9_IaHbRcwN9HHIR4ZKAnkMSN05XH-_A9_tEwYH4S32xbXcLL8z9nYzrGu40qnd2SJ-WY7i",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/09966410438ce7a7fa4e86484b5fe000/IMG_7020.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvf4RMJNFjjJ7mOcDhehVntXJWW4GIL7tnEaKeQKRqxIvwVhlXHkqgq1d979OiSz28OBqaTiArzDeETD6VzTq_tYpRN4OSUGHd3e4Tn_85mqRFQmrnzDSpARY-3UVxMMio",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/f65e33620772ff82c8ffc94126adfc40/IMG_7022.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdrfw102NKhCFdQ4eCHKtNvhLnk0DUiaRk9jBSRzCb9_-Y04nWLgAEnZun88Zxfb3RLw_QIWcsCR9cDyHr9SgyeODXU_XHnFMXtpKqpVEZtkkBPyhOmYtGQ3_Wrh97rE-RbmwNkIDAR3rlGgZk9ZLeP",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/5527f6afcb8b0ed64cc12312556c6107/IMG_7023.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfhUhZTA5OeWcEGM3iGX6ZoPSfz3P23djMoDQSLv6n31ZAo5VoRMXDqXM3Hl9CW61A18eqAOdYV2F5uY_wigZdA6Mt8AJN7Myd0aX4zn3pVBatYju0fssJ-TBnzGgwtMIDkPrw9PmLqiJqZjoX01ck9",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/8acef3fa4cd1e5d22a287fe0d6a075fa/IMG_7024.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfuu-rUBucKMsyHdudQh4mOVZq8Mc9WddGd7fV5wPAaH5IpOgqJ1CdOWHOn0BIoQI_uE0PIUT3GyX3h2zzWSyO0MQl1LIY0rkx3OF99XNssyLxgVD7yyChEXlRViFVxu8WiiC0Y_GZjs_YNmJl-evZO",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/bc59086160f431e9df980715c338df53/IMG_7025.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdiduYQEOxhjcxvboQPKgA6dpDeXe9Bzycvku_Tfg3-S7QX5Jiy1hykeIA-8Kliy1OjNCICx-_Z8zBSvJoee0VJQn1RMSD8TvllkPEFTLCADb8fqMWYWu8sI7Ckd9FVFjKLh9kM8b-vTHHy_3YzSWAe",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/09dbbc115274d07f1bec31764500893f/IMG_7026.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzf8LLUpYs7srmv2ELi9FrYvnlvEkaAmh98J0pq3eSHuK5YqYqB2n-_IHMGX_n7xTmCd948jeHTN9V-Rcgf_XQCH88pbJQe0mE3QIFpLzgOeKOMqyeO3hyENINw8bm2OMDlfs5RZmsTzEJilzPPGoGah",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/3005facb9a1a5d08ca7cec6ba042520e/IMG_7027.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzeG68HmhjCTPeEAkFH88KonvgnmPgF-ArR-zdQMqcf7KIPS3UaTWe6Uw2K2dLZc09hq4p05J9vuS9YSplBOKglcuLEz4qtKEVWRkZmuAyrs4YXwtRsK-g14kg2XSg6hkIq5qA5n1WD_U3ubbGU2rczX"
    ]
titles = [
    "Choisissez les aliments adaptés pour le petit-déjeuner",
    "Choisissez les plats sucrés",
    "Choisissez les aliments qui sont des liquides",
    "Choisissez les aliments végétariens",
    "Choisissez les plats qui sont chauds"
]

headings_urls = [
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/1723715b0f12b4c623eabd805b3f1296/IMG_7459.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxvy3UQHPwxtzT0ukNhvQD6yLRUwnUPZtTVG3Ph_kd5Ik1RfjlgVVrCXl5vCIS_kiStGKsJ_ENZ3eVsqhMKkk1YvyAGg6p4_qCiKHn11uNhZqxv99cXLPZsa2TGVd7Cs8SPce9R0y0Xsdf1f9YrSWF",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/c1d6e0f25b73d3ed382fbaa1c1de4efd/IMG_7460.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzcDM9glIFgB6UIAKkBUo76RxDuu_PizWRudEHhwFv2jpmq5SXojCrxUYmFS-uNfclF3DUAoJoMMHDKCWqP7xZnqVs2fQFpm6Nw4yv4qarguFdjgr33VfctaUjyteNJRFRzae0aciJGsI9wzuiuDOtK9",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/8bd2a57abaa348cf89f20a216a56f755/IMG_7461.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfuu-rUBucKMsyHdudQh4mO_h0gseYTVhnaDJvYSPHlRb56jN3P5sYqBVJKwDCa6kf95NCjnWWQMrRdLLbHQXmbYLbv3Ulotz6pDA-4faJpGIIO4HesG13JugF6nuGWybTyL7N3tHbvIIvsy1qnt7VG",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/7cc928f83bda17ec4392a1bb4eb95a92/IMG_7462.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzebLajaIv9b92DI7GQgO4RrYuUphu_o4Z5dJ1zf32KAoy_Mb86NAWEPAbwhXeS623LNFxqWvsIk4gKwnx5EZr8p-gDwPFXuMyq6LErWV3m0dGWIIlEBlYHGTebAneV2aXZg0IbJon8y1WVO4uhKQkKi",
    "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/58c0575a2c4c5981c30eb8860549b509/IMG_7463.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfhUhZTA5OeWcEGM3iGX6ZoznnT_jI_VB-wS3Q5gI1NKmU5YlnOht_pHgjErHyifhPeq7yprgOWNP8teKISQGZRsTCA8brcOhUlkNUsowrMlcwxgqaVs2z9qJlKpXwa03L6XbrXqxYY6U8ykOziKql7"
]

keyboard = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/bb88f6bd93ad110478d1b4a760602b85/IMG_7021.jpeg?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzdiduYQEOxhjcxvboQPKgA6u6GGqbug_LJLET_bn8mfsL9rgT7nTXPgUanY3h48U7LaZydZnHzLVnE4Im6nZ9haM3Gr5X_it0-oG3YAAmNC1TOv38YLfgGtX5LoYWLVnYVV8L8aFE0405FJ4jfymV7w"

falling_objects = []
steak = urls[0]
times2 = urls[1]
minus3 = urls[2]
times3 = urls[3]
minus2 = urls[4]
soup = urls[5]
oj = urls[6]
soda = urls[7]
cereal = urls[8]
sandwich = urls[9]
croissant = urls[10]
game_over_flag = False
heading_height = screen_height // 10
randomint = randint(0, 4)
topic = titles[randomint]
print(randomint)

def open_fullscreen_window():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.mainloop()

breakfast = [cereal, oj, croissant]
sweets = [cereal, croissant, soda, oj]
liquids = [oj, soda, soup, cereal]
vegetarian = [cereal, soup, sandwich]
hot = [soup, steak, sandwich, croissant]

if topic == titles[0]:
    answers = breakfast
elif topic == titles[1]:
    answers = sweets
elif topic == titles[2]:
    answers = liquids
elif topic == titles[3]:
    answers = vegetarian
elif topic == titles[4]:
    answers = hot


def check_answer(answer):
    global score, finished
    if answer == catchedObject:
        score += 2
        finished += 1
        if finished == 10:
            game_over()
    else:
        score -= 1

if len(sys.argv) > 1:
    time_left = sys.argv[1]
    print(f"Received variable: {time_left}")
else:
    print("No variable received.")
    time_left = 2700

def open_script():
    try:
        subprocess.Popen([sys.executable, "Break.py", str(remaining)])
        sys.exit()
    except FileNotFoundError:
        messagebox.showerror("Error", "File Break.py not found.")

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
        open_script()

parent_canvas = tk.Canvas(root, bg=myyellow, width=screen_width, height=heading_height, highlightthickness=0)
parent_canvas.pack(fill="x")
child_canvas1 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 5, height=heading_height, highlightthickness=0)
child_canvas1.place(x=0, y=0)
child_canvas1.pack(side="left", fill="both", expand=True)
score_label = tk.Label(child_canvas1, text="Score: 0", font=allurabig, bg=myyellow)
score_label.pack(expand=True)
child_canvas2 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 2, height=heading_height, highlightthickness=0)
child_canvas2.place(x=screen_width // 5, y=0)
child_canvas2.pack(side="left", fill="both", expand=True)
heading1 = get_image(headings_urls[titles.index(topic)], screen_width // 2, heading_height)
child_canvas2.create_image(80, 0, anchor="nw", image=heading1)
child_canvas3 = tk.Canvas(parent_canvas, bg=myyellow, width=screen_width // 5, height=heading_height, highlightthickness=0)
child_canvas3.place(x=(2 * screen_width) // 3, y=0)
child_canvas3.pack(side="left", fill="both", expand=True)
heading2 = get_image(keyboard, screen_width // 5, heading_height//2)
child_canvas3.create_image(50, heading_height // 4, anchor="nw", image=heading2)

game_canvas = tk.Canvas(root, bg=myyellow, width=screen_width, height=screen_height - heading_height, highlightthickness=0)
game_canvas.pack(fill="both", expand=True)

basket_width = screen_width // 5
basket_height = screen_height // 10
basket_x = screen_width // 2
basket_y = screen_height - basket_height - heading_height
object_width = 100
object_height = 100
falling_speed = 5
basket_image = "https://u1.padletusercontent.com/uploads/padlet-uploads/772896347/12989f02d436fe4b641c47e1ffd5d404/IMG_7465.png?token=ovZCJ2DsQTTdlrr926tnqto8AUdkuKZ6x6FAMVy6n7-poSxZhGqP1uYapDZt8Es7IMGYQjFrEytvk7pzxUbF0ZlpwL7yxCdvO6iDm5WlOzfxvy3UQHPwxtzT0ukNhvQDmyJNFzfkOL3uuLgPA0wqXegyPZdq018YA_4BBeu-pAvqJXE2UwtmFOmwrJlwBr7HCKgoaTfr8_5U39kcTjOjDmWRQ078f2QK9y4gyWocu7E="
basket_canvas = tk.Canvas(game_canvas, bg=myyellow, width=basket_width, height=basket_height, highlightthickness=0)
basket = get_image(basket_image, basket_width, basket_height)
basket_canvas.place(x=basket_x, y=basket_y)
basket_canvas.create_image(0, 0, anchor="nw", image=basket)

def move_basket(event):
    global basket_x
    if event.keysym == 'Left' and basket_x > 0:
        basket_x -= 20
    elif event.keysym == 'Right' and basket_x < screen_width - basket_width:
        basket_x += 20
        basket_canvas.place(x=basket_x, y=basket_y)

def create_falling_object():
    global falling_objects
    url = choice(urls)
    obj_image = get_image(url, 100, 100)
    x_position = randint(0, screen_width - 100)
    falling_object = game_canvas.create_image(x_position, 0, anchor="nw", image=obj_image)
    falling_objects.append((falling_object, obj_image))

def update_falling_objects():
    global score, game_over_flag
    if not game_over_flag:
        for obj in falling_objects:
            obj_id, img = obj
            game_canvas.move(obj_id, 0, 5)  
            if game_canvas.coords(obj_id)[1] > screen_height:
                game_canvas.delete(obj_id)
                falling_objects.remove(obj)
                score -= 1
                score_label.config(text=f"Score: {score}")
            elif (game_canvas.coords(obj_id)[0] >= basket_x and
                  game_canvas.coords(obj_id)[0] <= basket_x + basket_width and
                  game_canvas.coords(obj_id)[1] + 100 >= basket_y):
                game_canvas.delete(obj_id)
                falling_objects.remove(obj)
                score += 2
                score_label.config(text=f"Score: {score}")
                if score >= 20:
                    goBack()

        root.after(100, update_falling_objects)

def goBack():
    messagebox.showinfo("Game Over", "Game Over: You have successfully completed this mission")
    try:
        subprocess.Popen([sys.executable, "NextGames.py", str(remaining)])
        sys.exit()  
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {script_name} not found.")



root.bind("<KeyPress>", move_basket)
root.after(1000, create_falling_object)  
root.after(1000, update_falling_objects) 

def continuous_creation():
    create_falling_object()
    root.after(1000, continuous_creation)  

continuous_creation()  
countdown(time_left)  
root.mainloop()
