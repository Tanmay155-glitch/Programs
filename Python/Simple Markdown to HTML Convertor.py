markdown = input("Enter markdown text: ")
html = markdown.replace("#", "<h1>").replace("**", "<b>").replace("*", "<i>")
html = html.replace("<h1>", "</h1>").replace("<b>", "</b>").replace("<i>", "</i>")
print("Converted HTML:", html)
