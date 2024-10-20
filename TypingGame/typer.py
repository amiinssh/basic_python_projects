import random
import time
import word_bank

def get_level_parameters(level):
    if level == 1:
        return {"difficulty": "easy", "num_words": 3, "time_limit": 10}
    elif level == 2:
        return {"difficulty": "easy", "num_words": 5, "time_limit": 10}
    elif level == 3:
        return {"difficulty": "medium", "num_words": 5, "time_limit": 8}
    elif level == 4:
        return {"difficulty": "medium", "num_words": 7, "time_limit": 8}
    elif level == 5:
        return {"difficulty": "hard", "num_words": 7, "time_limit": 6}
    else:
        raise ValueError("Invalid level")

def play_round(words, time_limit):
    start_time = time.time()
    for word in words:
        typed_word = input(f"Type the word: {word}\n")
        if typed_word != word or time.time() - start_time > time_limit:
            return False
    return True

def take_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words.""" 
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def pick_random_words(level, difficulty):
    words = {
        "easy": ["bat",
    "dog",
    "toy",
    "cat",
    "rat",
    "law",
    "mud",
    "boy",
    "the",
    "she",
    "red",
    "pop",
    "lie",
    "bay",
    "hay",
    "can",
    "sad",
    "mad",
    "cap",
    "rap",
    "met",
    "fad",
    "hop",
    "top",
    "tap",
    "lap",
    "lie",
    "bag",
    "ham",
    "ray",
    "say",
    "tie",
    "bit",
    "hit",
    "hat",
    "bet",
    "bid",
    "lid",
    "pad",
    "and",
    "tan",
    "tar",
    "eat",
    "ate",
    "lag",
    "rag",
    "tag",
    "kid",
    "dip",
    "rip",
    "lip",
    "pod",
    "rod",
    "nod",
    "his",
    "sis",
    "gem",
    "ant",
    "wad",
    "win",
    "nap",
    "way",
    "pay",
    "day",
    "van",
    "mom",
    "dad",
    "dot",
    "rot",
    "tip",
    "hen",
    "tin",
    "fee",
    "pee",
    "tee",
    "tea",
    "pea",
    "bee",
    "sea",
    "see",
    "men",
    "man",
    "did",
    "sim",
    "pin",
    "fib",
    "yay",
    "may",
    "pot",
    "pan",
    "run",
    "ran",
    "ton",
    "put",
    "hut",
    "but",
    "cut",
    "pit",
    "vat",],
        "medium": ["lemon",
    "cheese",
    "happy",
    "angry",
    "tomato",
    "carve",
    "tattoo",
    "water",
    "walks",
    "visit",
    "liver",
    "flight",
    "height",
    "skirts",
    "house",
    "train",
    "spoon",
    "tiger",
    "zebra",
    "doctor",
    "teach",
    "study",
    "juice",
    "bottle",
    "never",
    "peace",
    "donor",
    "python",
    "coding",
    "uncle",
    "sleeps",
    "table",
    "wonder",
    "growth",
    "forest",
    "river",
    "yellow",
    "purple",
    "cycle",
    "pillow",
    "school",
    "queen",
    "yogurt",
    "bouncy",
    "flavor",
    "guitar",
    "piano",
    "breeze",
    "sunny",
    "window",
    "marvel",
    "gloves",
    "framed",
    "sweet",
    "dirty",
    "clean",
    "apple",
    "coffee",
    "button",
    "refer",
    "climb",
    "minute",
    "light",
    "shelf",
    "wobble",
    "tired",
    "party",
    "brain",
    "vault",
    "tennis",
    "winter",
    "cover",
    "paper",
    "pencil",
    "hello",],
        "hard": ["congratulations",
    "absolutely",
    "photosynthesis",
    "monstrosity",
    "university",
    "cheeseburger",
    "accommodate",
    "suburban",
    "pizazz",
    "assuming",
    "stewardess",
    "xylophone",
    "overzealous",
    "withdrawal",
    "wednesday",
    "vulnerable",
    "visualization",
    "versatile",
    "veterinary",
    "vaccination",
    "vegetarian",
    "unanimous",
    "transmission",
    "trajectory",
    "temporary",
    "tournament",
    "temperature",
    "surveillance",
    "psychology",
    "responsibility",
    "recommendation",
    "pronunciation",
    "practicioner",
    "plagiarism",
    "pilgrimage",
    "philosophy",
    "participation",
    "nutritious",
    "necessarily",
    "miscellaneous",
    "marshmallows",
    "mayonnaise",
    "leprechaun",
    "limousine",
    "kindergarten",
    "knowledgeable",
    "interference",
    "inflammation",
    "handkerchief",
    "fluorescent",
    "extraordinary",
    "pharmaceutical",
    "exhiliration",
    "environmental",
    "disappointment",
    "choreography",
    "circumstantial",
    "cauliflower",
    "cantaloupe",
    "auditorium",
    "apostrophe",
    "amphitheater",
    "advantageous",
    "acknowledgement",
    "abbreviation",
    "abundant",
    "accommodation",
    "adjustment",
    "ambidextrous",
    "asymmetrical",
    "auxiliary",
    "bachelorette",
    "bureaucracy",
    "behavioral",
    "boulevard",
    "camouflage",
    "determination",
    "differentiation",
    "description",
    "dysfunctional",
    "impressionable",
    "enthusiastic",
    "entrepreneur",
    "eavesdropping",
    "exaggerated",
    "fascinating",
    "governmental",
    "hygienic",
    "immediately",
    "individuality",
    "interpretation",
    "laboratory",
    "labyrinth",
    "lieutenant",
    "lightning",
    "legitimate",
    "likelihood",
    "maintenance",
    "masquerade",
    "medicinal",
    "mezzanine",
    "medieval",
    "mischievious",
    "misunderstood",
    "pneumonia",
    "noticeable",
    "opportunity",
    "overwhelming",
    "picturesque",
    "pilgrimage",
    "prohibitive",
    "quadruple",
    "ridiculous",
    "sacrilegious",
    "rudimentary",
    "chandelier",
    "sophomore",
    "superfluous",
    "susceptible",
    "suspicious",
    "synonymous",
    "tomorrow",
    "zucchini",]
    }
    return random.sample(words[difficulty], level)

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)
