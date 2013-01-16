import random

descriptor_list = ["exciting", "boring", "calm", "relaxing", "happy", "sad",
                  "mournful", "thoughtful", "cerebral", "silly", "raunchy",
                  "upsetting", "terrifying", "scary", "joyful", "child-like",
                  "youthful", "disturbing", "inspiring", "wacky", "weird",
                  "bizarre", "abstract", "beautiful", "artful", "enchanting",
                  "spellbinding", "engrossing", "confusing", "mind-bending",
                  "visual", "auditory", "tangible", "slapstick", "noire",
                  "historical", "documentary", "non-fiction", "romantic",
                  "fanciful", "fantasy", "magical", "wonderful", "intense",
                  "action packed", "surgical", "divisive", "aggressive",
                  "gory", "ugly", "dark", "black & white"]

genre_list = ["RPG", "FPS", "sim game", "adventure game", "shooter",
             "racing game", "hack n slash", "platformer", "puzzle game",
             "board game", "sports game", "kids game", "virtual pet game",
             "music game", "rhythm game", "trivia game", "abstract game",
             "art game"]

setting_list = ["at night", "in a city", "on a farm", "underwater", "in space",
               "on the moon", "on another planet", "underground",
               "in the clouds", "inside a computer", "inside the human body",
               "in a back yard", "in the kitchen", "in the future",
               "in the past", "in an alternate universe", "in a book",
               "in someone's imagination", "just before the apocalypse",
               "in the country", "in Europe", "in Africa", "in South America",
               "in Asia", "in Australia", "in North America", "in Antarctica",
               "in the afterlife", "in a cemetery", "in a supermarket",
               "in a mall", "in someone's memories", "in the 4th dimension",
               "in time", "in a casino", "in an office building",
               "in a factory", "in the internet", "during a war",
               "just before a war", "just after a war", "in a dungeon",
               "in a forest", "in a painting", "in a photograph", "in a slum",
               "in jail", "in government", "in a zoo", "at a race track",
               "in a traffic jam"]

def generate_game_idea():
    descriptor_one = random.choice(descriptor_list)
    chance_of_two_descriptors = 50
    roll = random.randint(0, 100)
    genre = random.choice(genre_list)
    setting = random.choice(setting_list)

    if roll > chance_of_two_descriptors:
        while 1:
            descriptor_two = random.choice(descriptor_list)
            if descriptor_two != descriptor_one:
                break
        return "{}, {}, {} set {}.".format(descriptor_one.title(),
                                           descriptor_two, genre, setting)
    else:
        return "{}, {} set {}.".format(descriptor_one.title(), genre, setting)