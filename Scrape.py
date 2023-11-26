import requests
from bs4 import BeautifulSoup
import json
import re
import matplotlib.pyplot as plt

import time

champions = [
    "Aatrox",
    "Ahri",
    "Akali",
    "Akshan",
    "Alistar",
    "Amumu",
    "Anivia",
    "Annie",
    "Aphelios",
    "Ashe",
    "Aurelion Sol",
    "Azir",
    "Bard",
    "Bel'Veth",
    "Blitzcrank",
    "Brand",
    "Braum",
    "Briar",
    "Caitlyn",
    "Camille",
    "Cassiopeia",
    "Cho'Gath",
    "Corki",
    "Darius",
    "Diana",
    "Draven",
    "Dr. Mundo",
    "Ekko",
    "Elise",
    "Evelynn",
    "Ezreal",
    "Fiddlesticks",
    "Fiora",
    "Fizz",
    "Galio",
    "Gangplank",
    "Garen",
    "Gnar",
    "Gragas",
    "Graves",
    "Gwen",
    "Hecarim",
    "Heimerdinger",
    "Illaoi",
    "Irelia",
    "Ivern",
    "Janna",
    "Jarvan IV",
    "Jax",
    "Jayce",
    "Jhin",
    "Jinx",
    "Kai'Sa",
    "Kalista",
    "Karma",
    "Karthus",
    "Kassadin",
    "Katarina",
    "Kayle",
    "Kayn",
    "Kennen",
    "Kha'Zix",
    "Kindred",
    "Kled",
    "Kog'Maw",
    "K'Sante",
    "LeBlanc",
    "Lee Sin",
    "Leona",
    "Lillia",
    "Lissandra",
    "Lucian",
    "Lulu",
    "Lux",
    "Malphite",
    "Malzahar",
    "Maokai",
    "Master Yi",
    "Milio",
    "Miss Fortune",
    "Wukong",
    "Mordekaiser",
    "Morgana",
    "Naafiri",
    "Nami",
    "Nasus",
    "Nautilus",
    "Neeko",
    "Nidalee",
    "Nilah",
    "Nocturne",
    "Nunu & Willump",
    "Olaf",
    "Orianna",
    "Ornn",
    "Pantheon",
    "Poppy",
    "Pyke",
    "Qiyana",
    "Quinn",
    "Rakan",
    "Rammus",
    "Rek'Sai",
    "Rell",
    "Renata Glasc",
    "Renekton",
    "Rengar",
    "Riven",
    "Rumble",
    "Ryze",
    "Samira",
    "Sejuani",
    "Senna",
    "Seraphine",
    "Sett",
    "Shaco",
    "Shen",
    "Shyvana",
    "Singed",
    "Sion",
    "Sivir",
    "Skarner",
    "Sona",
    "Soraka",
    "Swain",
    "Sylas",
    "Syndra",
    "Tahm Kench",
    "Taliyah",
    "Talon",
    "Taric",
    "Teemo",
    "Thresh",
    "Tristana",
    "Trundle",
    "Tryndamere",
    "Twisted Fate",
    "Twitch",
    "Udyr",
    "Urgot",
    "Varus",
    "Vayne",
    "Veigar",
    "Vel'Koz",
    "Vex",
    "Vi",
    "Viego",
    "Viktor",
    "Vladimir",
    "Volibear",
    "Warwick",
    "Xayah",
    "Xerath",
    "Xin Zhao",
    "Yasuo",
    "Yone",
    "Yorick",
    "Yuumi",
    "Zac",
    "Zed",
    "Zeri",
    "Ziggs",
    "Zilean",
    "Zoe",
    "Zyra",
]


champion_numbers = [
    266,
    103,
    84,
    166,
    12,
    32,
    34,
    1,
    523,
    22,
    136,
    268,
    432,
    200,
    53,
    63,
    201,
    233,
    51,
    164,
    69,
    31,
    42,
    122,
    131,
    119,
    36,
    245,
    60,
    28,
    81,
    9,
    114,
    105,
    3,
    41,
    86,
    150,
    79,
    104,
    887,
    120,
    74,
    420,
    39,
    427,
    40,
    59,
    24,
    126,
    202,
    222,
    145,
    429,
    43,
    30,
    38,
    55,
    10,
    141,
    85,
    121,
    203,
    240,
    96,
    897,
    7,
    64,
    89,
    876,
    127,
    236,
    117,
    99,
    54,
    90,
    57,
    11,
    902,
    21,
    62,
    82,
    25,
    950,
    267,
    75,
    111,
    518,
    76,
    895,
    56,
    20,
    2,
    61,
    516,
    80,
    78,
    555,
    246,
    133,
    497,
    33,
    421,
    526,
    888,
    58,
    107,
    92,
    68,
    13,
    360,
    113,
    235,
    147,
    875,
    35,
    98,
    102,
    27,
    14,
    15,
    72,
    37,
    16,
    50,
    517,
    134,
    223,
    163,
    91,
    44,
    17,
    412,
    18,
    48,
    23,
    4,
    29,
    77,
    6,
    110,
    67,
    45,
    161,
    711,
    254,
    234,
    112,
    8,
    106,
    19,
    498,
    101,
    5,
    157,
    777,
    83,
    350,
    154,
    238,
    221,
    115,
    26,
    142,
    143,
]

# print(len(champions), len(champion_numbers))

# exit()


import os


# Function to load existing data
def load_existing_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return {}


# Function to save data
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)


# all_champions_data = load_existing_data('new_champion_data.json')
all_champions_data = {}
cnt = 0

session = requests.Session()
url = f"https://lolalytics.com/lol/{champions[0]}/build/?tier=1trick&patch=30"
session.get(url)


for champion in champions:
    boy = re.sub(r"[^a-zA-Z0-9]", "", champion).lower()

    # print(boy)
    # Create the session on the page
    # session = requests.Session()
    # url = f"https://lolalytics.com/lol/{boy}/build"
    # session.get(url)

    data_url = f"https://ax.lolalytics.com/mega/?ep=champion&p=d&v=1&patch=30&cid={champion_numbers[cnt]}&lane=default&tier=1trick&queue=420&region=all"
    # print(data_url)
    response = session.get(data_url)

    if response.status_code != 200:
        print("Failed to retrieve data. Status code: {response.status_code}: " + boy)
        continue

    print(f"Processing: {champion} + {champion_numbers[cnt]}")

    data = response.json()

    # while 'timeWin' not in data:
    #     print(data)
    #     time.sleep(15)

    # Extract 'timeWin' and 'time' data and calculate winrates
    time_win_data = data["timeWin"]
    time_data = data["time"]

    # asd = {k: time_win_data[k] for k in sorted(time_win_data, key=lambda x: int(x))}
    # asd2 = {k: time_data[k] for k in sorted(time_data, key=lambda x: int(x))}

    # print(asd)
    # print(asd2)

    winrates = {
        int(key): time_win_data[key] / time_data[key] if time_data[key] != 0 else 0
        for key in time_win_data
    }

    # Sort the data by game length
    sorted_data = sorted(winrates.items())
    sorted_game_lengths, sorted_winrates = zip(*sorted_data)

    all_champions_data[champion] = sorted_winrates

    save_data("new_champion_data.json", all_champions_data)

    # Plot
    # plt.figure(figsize=(10, 6))
    # plt.plot(sorted_game_lengths, sorted_winrates, marker='o', linestyle='-', color='b')
    # plt.title("Winrate vs Sorted Game Length")
    # plt.xlabel("Sorted Game Length")
    # plt.ylabel("Winrate")
    # plt.grid(True)
    # plt.show()
    cnt = cnt + 1

# print(all_champions_data)

# filename = "new_champion_data.json"

# # Write the data to a file
# with open(filename, "w") as file:
#     json.dump(all_champions_data, file)

# print(f"Data saved to {filename}")
