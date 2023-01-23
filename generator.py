import os
import glob

weapons = [
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V1",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V2",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V3",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V4",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V5",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V6",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V7",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V8",
    },
    {
        "base": "WEAPON_POOLCUE",
        "name": "WEAPON_POOLCUE_V9",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V1",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V2",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V3",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V4",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V5",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V6",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V7",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V8",
    },
    {
        "base": "WEAPON_KNIFE",
        "name": "WEAPON_KNIFE_V9",
    },
     {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V1",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V2",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V3",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V4",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V5",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V6",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V7",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V8",
    },
    {
        "base": "WEAPON_KNUCKLE",
        "name": "WEAPON_KNUCKLE_V9",
    },
]

orderNumberStart = 10000

# create output folder if not exists
if not os.path.exists("./output"):
    os.makedirs("./output")

for weapon in weapons:
    orderNumberStart += 1
    base = weapon["base"]
    weaponName = weapon["name"]

    # delete whole folder
    os.system("rmdir .\\output\\{} /S /Q".format(weaponName))

    # copy whole folder
    os.system("xcopy .\\{} .\\output\\{} /E /I /Y".format(base, weaponName))

    files = glob.glob("./output/{}/**".format(weaponName), recursive=True)
    for file in files:
        if os.path.isfile(file):
            with open(file, "r") as f:
                filedata = f.read()
                # Replace the text
                filedata = filedata.replace("NEW_ORDER_NUMBER_HERE", str(orderNumberStart))
                filedata = filedata.replace("WEAPON_IN_GAME_NAME_HERE", str(weaponName))
                filedata = filedata.replace("SLOT_NAME_HERE", str(orderNumberStart))
                filedata = filedata.replace("WEAPON_MODEL_NAME_HERE", str(weaponName))
                
                with open(file, "w") as f:
                    f.write(filedata)