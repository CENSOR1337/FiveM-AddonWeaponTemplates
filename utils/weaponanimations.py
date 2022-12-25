import xml.etree.ElementTree as ET

weaponname = "WEAPON_ACIDPACKAGE"

tree = ET.parse("weaponanimations.meta")

root = tree.getroot()

for weapon_animations in root.findall(".//WeaponAnimations"):
    for item in weapon_animations.findall("./Item"):
        key = item.get("key")
        if key != weaponname:
            weapon_animations.remove(item)

tree.write("output.xml")