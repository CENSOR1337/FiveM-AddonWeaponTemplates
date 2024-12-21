import os
import glob

weapons = [
    {"base": "WEAPON_POOLCUE", "name": "WEAPON_POOLCUE_V1", "model": "w_melee_poolcue"}
]

orderNumberStart = 10000

# create output folder if not exists
if not os.path.exists("./output"):
    os.makedirs("./output")

for weapon in weapons:
    orderNumberStart += 1
    base = weapon["base"]
    weaponName = weapon["name"]
    model = weapon["model"] if "model" in weapon else weapon

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
                filedata = filedata.replace("WEAPON_MODEL_NAME_HERE", str(model))
                with open(file, "w") as f:
                    f.write(filedata)