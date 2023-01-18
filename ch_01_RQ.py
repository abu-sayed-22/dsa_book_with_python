#for diff purpose wing or something
# text="Happy Birth-day"
# text=text.split("-")
# bDayWish=text.upper()
# print(bDayWish)
# Python Refresher
# exer_dict = {"kent":"Denise" ,"Steve":"Lindy" }
# empty_dict={}
# empty_dict["kent"]="Denise"
# empty_dict["Steve"]="Landy"
# print(empty_dict)
# __lt__
#_________________________________________13_____________________
# input_int=int(input("Please Input A Number : "))
#
# result=0
#
# for i in range(input_int):
#     if i%2 == 0 :
#         result += i
#
#
# print(result)
# import tkinter
#
# root=tkinter.Tk()
#
# root.mainloop()

import xml.etree.ElementTree as ET
with open("hello.xml" , "r") as file :
    elem=file.read()
    xml_tree=ET.fromstring(elem)
    res = xml_tree.findall("style")
    print(res[0].attrib["lang"])













