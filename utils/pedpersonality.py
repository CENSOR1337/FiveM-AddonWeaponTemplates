import xml.etree.ElementTree as ET
mytree = ET.parse("pedpersonality.meta")
myroot = mytree.getroot()

weaponname = "WEAPON_WRENCH"

for x in myroot:
    if x.tag == "MovementModeUnholsterData":
        for y in x:
            for z in y:
                if (z.tag == "UnholsterClips"):
                    toBeRemoved = []
                    for w in z:
                        for q in w:
                            if (q.tag == "Weapons"):
                                found = False
                                weaponsTobeRemoved = []
                                for weapon in q:
                                    if (weapon.text == weaponname):
                                        found = True
                                    else:
                                        weaponsTobeRemoved.append(weapon)
                                for weapon in weaponsTobeRemoved:
                                    q.remove(weapon)
                                if not(found):
                                    toBeRemoved.append(w)
                    for w in toBeRemoved:
                        z.remove(w)


for x in myroot:
    if x.tag == "MovementModes":
        for y in x:
            for z in y:
                if (z.tag == "MovementModes"):
                    for w in z:
                        toBeRemoved = []
                        for q in w:
                            for r in q:
                                if (r.tag == "Weapons"):
                                    found = False
                                    weaponsTobeRemoved = []
                                    for weapon in r:
                                        if (weapon.text == weaponname):
                                            found = True
                                        else:
                                            weaponsTobeRemoved.append(weapon)
                                    for weapon in weaponsTobeRemoved:
                                        r.remove(weapon)
                                    if not(found):
                                        toBeRemoved.append(q)
                        for q in toBeRemoved:
                            w.remove(q)

mytree.write("result.meta", encoding="utf-8", xml_declaration=True, default_namespace=None, method="xml")