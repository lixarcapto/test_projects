


from ..cultural_group_depot.CulturalGroupDepot import CulturalGroupDepot

FEMALE_AGE_RANGE_K_TUPLE:tuple[str] = (
    "little girl", 
    "girl", 
    "woman", 
    "old woman", 
    "very old woman"
)

GENDER_KEY_TUPLE:tuple[str] = (
    "female",
    "male"
)

CULTURE_GROUP_DEPOT = CulturalGroupDepot()

CULTURE_KEY_LIST:list[str] = CULTURE_GROUP_DEPOT\
    .get_key_list()

PERSONAL_PRONOUN_TUPLE:tuple[str] = (
    "she",
    "he"
)

POSSESSIVE_PRONOUN_TUPLE:tuple[str] = (
    "her",
    "his"
)

PROFESSIONS_KEY_TUPLE:tuple[str] = (
    "TRAINEE",
    "CHEF",
    "PEASANT",
    "WOODSMAN",
    "SOLDIER",
    "BUILDER",
    "WORKER",
    "TEACHER",
    "SAILOR",
    "ARTIST",
    "TAILOR",
    "DOCTOR",
    "CHEMICAL",
    "MECHANIC",
    "BOSS",
    "CLERK",
    "LAWYER",
    "CRIMINAL",
    "DRIVING",
    "TRADER",
    "PRIEST",
    "ASSISTANT",
    "PILOT",
    "ELECTRICIAN"
)

CARRIED_OBJECT_BY_PROFESSION:dict = {
    "TRAINEE":"beggars hat",
    "CHEF":"wooden spoon",
    "PEASANT":"reaping hook",
    "WOODSMAN":"lumberjack axe",
    "SOLDIER": "rifle",
    "BUILDER": "hammer",
    "WORKER" : "shovel",
    "TEACHER": "measuring ruler",
    "SAILOR": "sailors spyglass",
    "ARTIST": "paint brush",
    "TAILOR" : "needle and thread",
    "DOCTOR" : "stethoscope",
    "CHEMICAL" : "glass flask",
    "MECHANIC" : "wrench",
    "BOSS" : "bosss notebook",
    "CLERK" : "calculator",
    "LAWYER" : "briefcase",
    "CRIMINAL" : "dagger",
    "DRIVING" : "old horn",
    "TRADER" : "wad of bills",
    "PRIEST" : "incense burner",
    "ASSISTANT" : "baby bottle",
    "PILOT": "pilot glasses",
    "ELECTRICIAN": "gloves" 
}

MALE_AGE_RANGE_K_TUPLE:tuple[str] = (
    "little boy", 
    "boy", 
    "man", 
    "old man", 
    "very old man"
)

CAUSE_DEATH_KEY_TUPLE:tuple[str] = (
    "natural_causes",
    "work_accident",
    "domestic_accident",
    "disease",
    "murder",
    "unknown",
    "starvation",
    "dehydration"
)

CLOTHING_STYLE_K_TUPLE:tuple[str] = (
    "nude",
    "rags", 
    "dress", 
    "pants_shirt", 
    "suit", 
    "tunic_hooded"
)

BEARD_STYLE_TUPLE:tuple[str] = (
    "invisible",
    "shaved",
    "short",
    "long",
    "goat"
)

HAIR_COLOR_DETAIL_TUPLE:tuple[str] = (
    "dark",
    "shining", 
    "golden", 
    "like blood", 
    "like chocolate",
    "like mandarins"
)

EYE_COLOR_DETAIL_TUPLE:tuple[str] = (
    "warm",
    "mysterious",
    "wild",
    "crystal clear",
    "like the sun",
    "like fire"
)

HAIRSTYLE_K_TUPLE:tuple[str] = (
    "long",
    "bald",
    "shaved", 
    "short", 
    "pigtails", 
    "princess", 
    "mohawk", 
    "military",
    "pompadour",
    "castaway",
    "cossack"
)

HEIGHT_KEY_TUPLE:tuple[str] = (
    "dwarf", 
    "short", 
    "medium", 
    "tall", 
    "giant"
)

AGE_RANGE_KEY_TUPLE:tuple[str] = (
    "child", 
    "teenager", 
    "adult", 
    "elderly", 
    "dying"
)

IDEOLOGY_KEY_TUPLE:tuple[str] = (
    "conservative",
    "liberal",
    "militarist",
    "collectivist",
    "agrarian",
    "industrialist",
    "separatist",
    "populist",
    "realistic"
)

MAKEUP_KEY_TUPLE:tuple[str] = (
    "invisible",
    "white",
    "maori",
    "doll",
    "egyptian",
    "american"
)

GREETING_TUPLE:tuple[str] = (
    "zdravstvuyte",
    "piali",
    "hello",
    "assalamualaikum",
    "bonjour",
    "sawubona",
    "hei",
    "namaste",
    "hola",
    "merhaba",
    "ni hao",
    "konnichiwa",
    "maeva manava",
    "buongiorno",
    "zdravo",
    "shalom"
)

HEIGHT_MAXIMUM = 5
AGE_MAXIMUM = 5

AGE_RANGE_DICT:dict[list[int]] = {
    "child":[0, 7], 
    "teenager":[8, 18], 
    "adult":[19, 45], 
    "elderly":[46, 65], 
    "dying":[66, 100]
}

FERTILITY_BY_AGE_DICT:dict[int] = {
    "child" : 0, 
    "teenager" : 40, 
    "adult" : 70, 
    "elderly" : 30, 
    "dying" : 2
}

AGE_RANGE_KEY_TUPLE:tuple[str] = (
    "child", 
    "teenager", 
    "adult", 
    "elderly", 
    "dying"
)

GRAY_HAIR_AGE = 4
GRAY_HAIR_DEFINITIVE_AGE = 5
GRAY_HAIR_PROBABILITY = 50
BALDNESS_AGE = 3

MAX_AGE = AGE_RANGE_DICT["dying"][1]

NATURAL_CAUSE_DEATH:list = [
    "heart attack",
    "severe flu",
    "serious infection",
    "respiratory failure"
]

PERSONALITY_KEY_TUPLE:tuple[str] = (
    "egocentric",
    "solidary",
    "evil",
    "adventurer",
    "depressant",
    "shy",
    "casanova",
    "intellectual",
    "consumerist",
    "bully",
    "fanatic",
    "natural",
    "dependent",
    "snooty"
)

PERSONALITY_KEY_TUPLE:tuple[str] = (
    "egocentric",
    "solidary",
    "evil",
    "adventurer",
    "depressant",
    "shy",
    "casanova",
    "intellectual",
    "consumerist",
    "bully",
    "fanatic",
    "natural",
    "dependent",
    "snooty"
)

MOOD_VALUE_KEY:tuple[str] = (
    "SAD",
    "SERIOUS",
    "HAPPY"
)

MOOD_DICT_RANGE:dict = {
    "SAD": [0,30],
    "SERIOUS" : [31, 60],
    "HAPPY": [61, 100]
}

DESCRIPTION_ARCHETYPE_DICT:dict[list] = {
    "egocentric":[
        "was very focused on her goals"
    ],
    "solidary":[
        "thought about how to help his family"
    ],
    "evil":[
        "thought about how to take revenge on his enemies"
    ],
    "adventurer":[
        "thought that another exciting experience awaited his future."
    ],
    "depressant":[
        "felt no interest in what he was doing and wondered why he should continue."
    ],
    "shy":[
        "looked nervous and no one knew what he was thinking."
    ],
    "casanova":[
        "thought about what other incredible people I could meet tomorrow."
    ],
    "intellectual":[
        "thought I could study and learn tomorrow"
    ],
    "consumerist":[
        "thought about what he could buy tomorrow and what to spend his money on."
    ],
    "bully":[
        "thought about how to get others to obey his orders."
    ],
    "fanatic":[
        "was thinking about how to convince others to think the same way."
    ],
    "natural":[
        "was very calm and not worried about what he would do tomorrow."
    ],
    "dependent":[
        "thought about how kind others were to help him"
    ],
    "snooty":[
        "thought about how I could attract more attention to show off."
    ]
}

SPECIFIC_CAUSE_DEATH:dict = {
    "TRAINEE": [
        "fire in the classroom",
        "accident in sports class",
        "school fight with a bully"
    ],
    "CHEF": [
        "gas_barrel_explosion",
        "accidentally_stabbed",
        "burning grease fire"
    ],
    "PEASANT": [
        "kick_from_a_horse",
        "crushed_by_a_tractor",
        "suffocated_in_the_silo"
    ],
    "WOODSMAN": [
        "crushed by a tree",
        "devoured by a bear",
        "fall from the top of a tree"
    ],
    "SOLDIER": [
        "fatal shot",
        "accident with an armored vehicle",
        "missing in action"
    ],
    "BUILDER": [
        "a brick falling from the roof",
        "collapse of a wall",
        "fall from scaffolding"
    ],
    "WORKER": [
        "trapped in industrial machinery",
        "fire at the factory",
        "hit by a truck"
    ],
    "TEACHER": [
        "fight with problem student",
        "slipped on the stairs",
        "suffocated by chalk"
    ],
    "SAILOR": [
        "lost in the ocean",
        "injured by a marlin",
        "devoured by sharks",
        "crushed by the mast"
    ],
    "ARTIST": [
        "suffocated with aerosols",
        "due to depression",
        "poisoned by lead paint"
    ],
    "TAILOR": [
        "crushed by rolls of cloth",
        "trapped by textile machine",
        "poisoned by fumes from the dye"
    ],
    "DOCTOR": [
        "dangerous deadly virus"
    ],
    "CHEMICAL": [
        "suffocated by toxic fumes"
    ],
    "MECHANIC": [
        "crushed by a car"
    ],
    "BOSS": [
        "fall from an office tower"
    ],
    "CLERK": [
        "fire in the church"
    ],
    "LAWYER": [
        "a client's revenge"
    ],
    "CRIMINAL": [
        "failed assault"
    ],
    "DRIVING": [
        "car accident"
    ],
    "TRADER": [
        "run over by a cart",
        "attacked by bandits",
        "drowned crossing a river"
    ],
    "PRIEST": [
        "fire in the church",
        "collapse in the church",
        "crushed by a statue"
    ],
    "ASSISTANT": [
        "office fire"
    ],
    "PILOT": [
        "plane crash",
        "accident with the blades",
        "hit by a plane"
    ],
    "ELECTRICIAN": [
        "electrocuted",
        "explosion at the power plant"
    ]
}

TERRAIN_TYPE_ACTIVITIES_DICT = {
    "jungle":[
        "JG_1", 
        "JG_2"
    ], 
    "cold_forest":[
        "CF_1",
        "CF_2"
    ], 
    "temperate_forest":[
        "TF_1",
        "TF_2"
    ],
    "desert":[
        "DT_1",
        "DT_2"
    ], 
    "dunes":[
        "DN_1",
        "DN_2"
    ], 
    "swamp":[
        "SP_1",
        "SP_2"
    ], 
    "grassland":[
        "GL_1",
        "GL_2"
    ], 
    "rocks":[
        "RK_1",
        "RK_2"
    ], 
    "volcano":[
        "VC_1",
        "VC_2"
    ], 
    "salt_flat":[
        "SF_1",
        "SF_2"
    ], 
    "sea":[
        "TF_1",
        "TF_2"
    ],
    "deep_sea":[
        "DS_1",
        "DS_2"
    ]
}

CHILDRENS_ACTIVITIES_DICT = {
    # JUNGLE
    "JG_1":"playing with his pet monkey",
    "JG_2":"collecting exotic insects like butterflies and spiders",
    # COLD FOREST
    "CF_1":"enduring the cold of the forest in winter",
    "CF_2":"reating sculptures with pine nuts from the forest and glue",
    # TEMPERATURE FOREST
    "TF_1":"collecting flowers in the forest",
    "TF_2":"feeding squirrels and deer in the forest with berries",
    # DESERT
    "DT_1":"by digging water wells and collecting water from puddles",
    "DT_2":"watching the sand lizards and scorpions fighting",
    # DUNES
    "DN_1":"playing sand sledding",
    "DN_2":"exploring ancient ruins under the dunes",
    # SWAMP
    "SP_1":"",
    "SP_2":"",
    # GRASSLAND
    "GL_1":"",
    "GL_2":"",
    # ROCKS
    "RK_1":"",
    "RK_2":"",
    # VOLCANO
    "VC_1":"",
    "VC_2":"",
    # SALT FLAT
    "SF_1":"",
    "SF_2":"",
    # SEA
    "SA_1":"",
    "SA_2":"",
    # DEEP SEA
    "DS_1":"",
    "DS_2":"",
    # MEGACITY
    "MC_1":"",
    "MC_2":""
}