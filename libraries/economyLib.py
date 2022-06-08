from datetime import datetime
import json
import random
import time

from captcha.image import ImageCaptcha

confirmations = [
        "yes",
        "yep",
        "yup",
        "y",
        "correct",
        "ys",
        "ye",
        "oui",
        "sure",
        "i do",
        "i am",
        "beaver",
        "🦫",
]



async def progress_bar(current, total, witdh = 20):
    percent = int(witdh * current / total)
    bar = "█" * percent + "░" * (witdh - percent)

    return bar


async def get_ring_emoji(ring):
    ring = ring.lower()
    if ring == "common":
            return "<:commoner_ring:970309052053733396>"
    elif ring == "uncommon":
            return "<:uncommon_ring:970309091249516555>"
    elif ring == "rare":
            return "<:rare_ring:970309099134803978>"
    elif ring == "epic":
            return "<:epic_ring:970309107489849435>"
    elif ring == "mythical":
            return "<:mythical_ring:970309114955702372>"
    else:
            return "none"


async def get_items_data():
    with open("storage/items.json", "r") as f:
        items = json.load(f)

    return items


async def get_shop_data():

    with open("storage/shop.json", "r") as f:
        shop = json.load(f)

    return shop


async def open_account(user):
    users = await get_bank_data()

    
    if str(user.id) in users:
        try:
            users[str(user.id)]["inventory"]
        except:
            #if users[str(user.id)]["version"] < 1.00:
            users[str(user.id)]["inventory"] = {}
            
            users[str(user.id)]["quote"] = "I'm not a bot, I'm a human"
            
            users[str(user.id)]["scavenge_cooldown"] = time.time() - 450
            users[str(user.id)]["inventory"]["logs"] = 0
            
            users[str(user.id)]["daily"] = {}
            users[str(user.id)]["daily"]["day"] = 0
            users[str(user.id)]["daily"]["streak"] = 0

            ###############################################################################
            
            users[str(user.id)]["spoke_day"] = (datetime.utcnow() - datetime(1970, 1, 1)).days - 1
            users[str(user.id)]["spoken_today"] = 0
            
            users[str(user.id)]["dam"] = {}
            users[str(user.id)]["dam"]["spent"] = {}
            users[str(user.id)]["dam"]["spent"]["logs"] = 0
            users[str(user.id)]["dam"]["level"] = 0
            
            users[str(user.id)]["lodge"] = {}
            users[str(user.id)]["lodge"]["spent"] = {}
            users[str(user.id)]["lodge"]["spent"]["logs"] = 0
            users[str(user.id)]["lodge"]["level"] = 0

            ###############################################################################
            
            users[str(user.id)]["inventory"]["insurance"] = 0
            
            users[str(user.id)]["stats"] = {}
            
            a = random.randint(1, 5)
            b = random.randint(1, 5)
            c = random.randint(1, 5)
            d = random.randint(1, 5)
            e = random.randint(1, 5)
            f = random.randint(1, 5)
            
            users[str(user.id)]["stats"]["strength"] = a
            users[str(user.id)]["stats"]["dexterity"] = b
            users[str(user.id)]["stats"]["intelligence"] = c
            users[str(user.id)]["stats"]["wisdom"] = d
            users[str(user.id)]["stats"]["charisma"] = e
            users[str(user.id)]["stats"]["perception"] = f

            users[str(user.id)]["stats"]["points"] = 30 - (a + b + c + d + e + f)
            
        try:
            users[str(user.id)]["data"]
        except: 
        #if users[str(user.id)]["version"] < 1.01:
            users[str(user.id)]["data"] = {} 
            
            users[str(user.id)]["dailyvote"] = {}
            users[str(user.id)]["dailyvote"]["streak"] = 0
            users[str(user.id)]["dailyvote"]["last_vote"] = 0
            users[str(user.id)]["dailyvote"]["total_votes"] = 0

                    
            with open("storage/playerInfo/bank.json", "w") as f:
                json.dump(users, f)

            users = await get_bank_data()
        
    
    
    
    if str(user.id) in users:
        users[str(user.id)]["version"] = 1.02
        
        with open("storage/playerInfo/bank.json", "w") as f:
                    json.dump(users, f)

        users = await get_bank_data()
    
    
    
    if str(user.id) in users:
        return

    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 10.0
    users[str(user.id)]["xp"] = 0
    users[str(user.id)]["quote"] = "I'm not a bot, I'm a human"
    
    ###############################################################################

    users[str(user.id)]["scavenge_cooldown"] = time.time()
    users[str(user.id)]["speak_cooldown"] = time.time() + 300
    
    ###############################################################################
    
    users[str(user.id)]["spoke_day"] = (datetime.utcnow() - datetime(1970, 1, 1)).days - 1
    users[str(user.id)]["spoken_today"] = 0

    ###############################################################################
    
    users[str(user.id)]["marriage"] = {}

    ###############################################################################
    
    users[str(user.id)]["inventory"] = {}
    users[str(user.id)]["inventory"]["logs"] = 0
    users[str(user.id)]["inventory"]["insurance"] = 0

    ###############################################################################
    
    users[str(user.id)]["daily"] = {}
    users[str(user.id)]["daily"]["day"] = 0
    users[str(user.id)]["daily"]["streak"] = 0
    
    ###############################################################################
    
    users[str(user.id)]["dam"] = {}
    users[str(user.id)]["dam"]["spent"] = {}
    users[str(user.id)]["dam"]["spent"]["logs"] = 0
    users[str(user.id)]["dam"]["level"] = 0
    
    ###############################################################################
    
    users[str(user.id)]["lodge"] = {}
    users[str(user.id)]["lodge"]["spent"] = {}
    users[str(user.id)]["lodge"]["spent"]["logs"] = 0
    users[str(user.id)]["lodge"]["level"] = 0

    ###############################################################################
    
    users[str(user.id)]["stats"] = {}
    
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    d = random.randint(1, 5)
    e = random.randint(1, 5)
    f = random.randint(1, 5)
    
    users[str(user.id)]["stats"]["strength"] = a
    users[str(user.id)]["stats"]["dexterity"] = b
    users[str(user.id)]["stats"]["intelligence"] = c
    users[str(user.id)]["stats"]["wisdom"] = d
    users[str(user.id)]["stats"]["charisma"] = e
    users[str(user.id)]["stats"]["perception"] = f

    users[str(user.id)]["stats"]["points"] = 30 - (a + b + c + d + e + f)
    
    ###############################################################################
    
    users[str(user.id)]["version"] = 1.01 
    
    users[str(user.id)]["data"] = {} 
    
    users[str(user.id)]["dailyvote"] = {}
    users[str(user.id)]["dailyvote"]["streak"] = 0
    users[str(user.id)]["dailyvote"]["last_vote"] = 0
    users[str(user.id)]["dailyvote"]["total_votes"] = 0

    

    with open("storage/playerInfo/bank.json", "w") as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("storage/playerInfo/bank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank_data(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("storage/playerInfo/bank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)][mode]]
    return bal


async def generate_user_capcha(user):
    # Create an image instance of the given size
    sizes = []
    for i in range(1, 10):
        sizes.append(random.randint(110, 170))

    image = ImageCaptcha(fonts = ["./font.ttf"], font_sizes = sizes, width = 500, height = 300)
    
    possibleLetters = "ABCEFGHJKLMNOPRSTUVWXYZ"

    captchaStr = " "
    for i in range(0, 5):
        captchaStr += random.choice(possibleLetters)
        captchaStr += " " * random.randint(1, 4)

    
    # generate the image of the given text
    data = image.generate(captchaStr)
    #image.create_noise_dots(image, color = (0, 0, 0), width = 1, number = 100)
    print(captchaStr)
    
    # write the image on the given file and save it
    image.write(captchaStr, f"./temp/captcha{user.id}.png")