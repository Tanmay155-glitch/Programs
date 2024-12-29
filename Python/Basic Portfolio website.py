name = input("Enter your name: ")
bio = input("Enter a short bio: ")

html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{name}'s Portfolio</title>
</head>
<body>
    <h1>Welcome to {name}'s Portfolio</h1>
    <p>{bio}</p>
</body>
</html>
"""

with open("portfolio.html", "w") as file:
    file.write(html_content)

print("Portfolio website created as 'portfolio.html'")
