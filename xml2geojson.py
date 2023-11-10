# convert the xml files to geojson

import xml.etree.ElementTree as ET
import geojson

features = []
brokenFeatures = []

# Marker tags
#  <marker dealercode="41051909" outletname="MSHSD HIRALAL AGARWAL" lat="19.682900000000"
#         lng="78.542090000000" distance="0" ADD1="HP DEALER" ADD2="ADILABAD TO NAGPUR ROAD"
#         ADD3="ADILABAD" STATECD="TS" TOWNCD="S4502" CITY="ADILABAD" CLUBHP="No" ATM="" LOANSHOP=""
#         C_STORE="" RESTAURANT="" BOOKSHOP="" INSURANCE="" KVK="" DHABA="" VS_PUC="" AUTO_ACCESS=""
#         BATTERIES="" TYRES="" AUTOLPG="No" CNGOUTLET="No" DTPLUS="Yes" MSRATE="111.88"
#         HSDRATE="99.88" ADDNL_FACILIY="Y" ICON_NAME="null"
#         div_data="&lt;div id='41051909_secTabs'  class='tabs'&gt;&lt;span id='mytab_1' class='activeTab'&gt;Dealer Details&lt;/span&gt;&lt;span id='mytab_2' class='passiveTab'&gt;Mini Map&lt;/span&gt;&lt;span id='mytab_3' class='passiveTab'&gt;Facilities&lt;/span&gt;&lt;span id='mytab_4'   class='passiveTab'&gt;Petrol/Diesel Rate&lt;/span&gt;&lt;/div&gt;&lt;div id='41051909_secCard1'  class='cardContent' style='display: block; '&gt; &lt;table style='border-width:4px; z-index:999; border-color:red;border-style: solid;'&gt;&lt;tbody&gt;&lt;tr &gt;&lt;td&gt; Outlet Name:&lt;/td&gt;&lt;td&gt;MSHSD HIRALAL AGARWAL&lt;/td&gt;&lt;/tr&gt;&lt;tr  class='alt'&gt;&lt;td&gt;ADD1:&lt;/td&gt;&lt;td&gt;HP DEALER&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;ADD2:&lt;/td&gt;&lt;td&gt;ADILABAD TO NAGPUR ROAD&lt;/td&gt;&lt;/tr&gt;&lt;tr class='alt'&gt;&lt;td&gt;ADD3:&lt;/td&gt;&lt;td&gt;ADILABAD&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Town Code:&lt;/td&gt;&lt;td&gt;S4502&lt;/td&gt;&lt;/tr&gt;&lt;tr class='alt'&gt;&lt;td&gt;City:&lt;/td&gt;&lt;td&gt;ADILABAD&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;State Code:&lt;/td&gt;&lt;td&gt;TS&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div id='41051909_secCard2' class='cardContent'&gt; &lt;b&gt;Tabbed Info Window - Marker 2&lt;/b&gt;&lt;/div&gt;&lt;div id='41051909_secCard3' class='cardContent'&gt;&lt;table style='border-width: 3px; border-color:red;border-style: solid;'&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th colspan='2'&gt;Facilities&lt;/th&gt;&lt;th&gt;Availability&lt;/th&gt;&lt;/tr&gt;&lt;tr class='alt'&gt;&lt;td&gt;DTPLUS&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_DTPLUS.svg'&lt;/td&gt;&lt;td&gt;Yes&lt;/td&gt;&lt;/tr&gt;&lt;tr &gt;&lt;td&gt;CLUB HP&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_CLUB_HP.svg'&lt;/td&gt;&lt;td&gt;No&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' class='alt'  &gt;&lt;td&gt;ATM&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_ATM.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr style='display:none' &gt;&lt;td style='display:none' &gt;Dhaba&lt;/td&gt;&lt;td style='display:none' &gt;&lt;IMG style='display:none' width='40px' height='40px' SRC = 'images/svg/icon_Dhaba.svg'&lt;/td&gt;&lt;td style='display:none' &gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' class='alt' &gt;&lt;td&gt;VS PUC &lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Vehicle_Service-PUC.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' &gt;&lt;td&gt;INSURANCE&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Insurance.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' class='alt'&gt;&lt;td&gt;RESTAURANT&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Restaurant.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' &gt;&lt;td&gt;Battery&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Batteries.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr  style='display:none' class='alt'&gt;&lt;td&gt;Tyres&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Tyres.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' &gt;&lt;td&gt;Auto Accessories&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Auto_Accessories.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' class='alt' &gt;&lt;td&gt;C_STORE&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_C-Store.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr style='display:none' &gt;&lt;td&gt;KVK&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_KVK.svg'&lt;/td&gt;&lt;td&gt;&lt;/td&gt;&lt;/tr&gt;&lt;tr class='alt'&gt;&lt;tr class='alt'&gt;&lt;td&gt;CNG Outlet&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_CNG.svg'&lt;/td&gt;&lt;td&gt;No&lt;/td&gt;&lt;/tr&gt;&lt;tr &gt;&lt;td&gt;Auto LPG&lt;/td&gt;&lt;td&gt;&lt;IMG width='40px' height='40px' SRC = 'images/svg/icon_Auto_LPG.svg'&lt;/td&gt;&lt;td&gt;No&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;&lt;div id='41051909_secCard4' class='cardContent'&gt;&lt;table border='0' style='border-width: 2px; border-color:red;border-style: solid'&gt;&lt;tbody&gt;&lt;tr&gt;&lt;th style='color:blue' &gt;Product&lt;/th&gt;&lt;th style='color:blue' &gt;Rate in (Rs.)&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;Petrol&lt;/td&gt;&lt;td&gt;111.88&lt;/td&gt;&lt;/tr&gt;&lt;tr class='alt'&gt;&lt;td&gt;Diesel&lt;/td&gt;&lt;td&gt;99.88&lt;/td&gt;&lt;/tr&gt;&lt;/tbody&gt;&lt;/table&gt;&lt;/div&gt;">
#     </marker>

for i in range(1, 806):
    fileName = "data/" + str(i).zfill(4) + ".xml"
    tree = ET.parse(fileName)
    root = tree.getroot()
    for child in root:
        if child.tag == "marker":
            feature: geojson.Feature = geojson.Feature(
                geometry=geojson.Point(
                    (
                        float(child.attrib["lng"]),
                        float(child.attrib["lat"]),
                    )
                ),
                properties={
                    "name": child.attrib["outletname"] or None,
                    "dealerCode": child.attrib["dealercode"] or None,
                    "address": (
                        child.attrib["ADD1"]
                        + " "
                        + child.attrib["ADD2"]
                        + " "
                        + child.attrib["ADD3"]
                    )
                    or None,
                    "city": child.attrib["CITY"] or None,
                    "stateCode": child.attrib["STATECD"] or None,
                    "townCode": child.attrib["TOWNCD"] or None,
                    "clubHP": child.attrib["CLUBHP"] or None,
                    "ATM": child.attrib["ATM"] or None,
                    "loanShop": child.attrib["LOANSHOP"] or None,
                    "cStore": child.attrib["C_STORE"] or None,
                    "restaurant": child.attrib["RESTAURANT"] or None,
                    "bookShop": child.attrib["BOOKSHOP"] or None,
                    "insurance": child.attrib["INSURANCE"] or None,
                    "kvk": child.attrib["KVK"] or None,
                    "dhaba": child.attrib["DHABA"] or None,
                    "vsPUC": child.attrib["VS_PUC"] or None,
                    "autoAccess": child.attrib["AUTO_ACCESS"] or None,
                    "batteries": child.attrib["BATTERIES"] or None,
                    "tyres": child.attrib["TYRES"] or None,
                    "autoLPG": child.attrib["AUTOLPG"] or None,
                    "cngOutlet": child.attrib["CNGOUTLET"] or None,
                    "dtPlus": child.attrib["DTPLUS"] or None,
                    "msRate": child.attrib["MSRATE"] or None,
                    "hsdRate": child.attrib["HSDRATE"] or None,
                    "addnlFacility": child.attrib["ADDNL_FACILIY"] or None,
                    "iconName": child.attrib["ICON_NAME"] or None,
                },
            )

            # check if coordinates are non 0 0
            if (
                feature.geometry.coordinates[0] != 0
                and feature.geometry.coordinates[1] != 0
            ):
                features.append(feature)
            else:
                brokenFeatures.append(feature)

with open("hp_fuel_full.geojson", "w") as file:
    geojson.dump(geojson.FeatureCollection(features), file)

with open("hp_fuel_broken.geojson", "w") as file:
    geojson.dump(geojson.FeatureCollection(brokenFeatures), file)
