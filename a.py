a = input()
b = ""
for i in a:
    if i == " " or i == ":" or i == ",":
        b += "_"
    else:
        b += i
        
print("\\movie\\"+b+ ".mp4" )