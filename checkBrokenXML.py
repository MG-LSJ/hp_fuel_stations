import xml.etree.ElementTree as ET

clean = True

for i in range(1, 806):
    fileName = "data/" + str(i).zfill(4) + ".xml"
    try:
        tree = ET.parse(fileName)
    except:
        print("File error: " + fileName)
        clean = False

if clean:
    print("All files are clean.")
