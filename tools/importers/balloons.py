"""Balloon importer from Bismuths Spreadsheet."""


with open("import.csv", newline="") as csvfile:
    dataset = []
    balloon = None
    name = None
    map = None
    speed = None
    kongs = {}
    for row in csvfile:
        rowdata = row.replace("\r\n", "").split(",")
        newentry = {}
        if rowdata[15] != "" and rowdata[15] != balloon:
            balloon = rowdata[15]
            name = rowdata[16]
            speed = rowdata[17]
            map = rowdata[18]
            kongs = {
                "dk": bool(int(rowdata[23])),
                "diddy": bool(int(rowdata[24])),
                "lanky": bool(int(rowdata[25])),
                "tiny": bool(int(rowdata[26])),
                "chunky": bool(int(rowdata[27])),
            }
            dataset.append({"balloon": int(balloon), "map": map, "name": name, "speed": int(speed), "kongs": kongs, "path": []})
        if rowdata[19] != "":
            newentry["order"] = int(rowdata[19])
            newentry["x"] = int(float(rowdata[20]))
            newentry["y"] = int(float(rowdata[21]))
            newentry["z"] = int(float(rowdata[22]))
            dict_index = next((index for (index, d) in enumerate(dataset) if d["balloon"] == int(balloon)), None)
            dataset[dict_index]["path"].append(newentry)

with open("balloons.txt", "w") as outputfile:
    outputfile.write(str(dataset))
