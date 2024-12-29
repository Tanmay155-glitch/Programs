name = input("Enter your name: ")
email = input("Enter your email: ")
skills = input("Enter your skills (comma-separated): ")

resume = f"""
Resume:
---------
Name: {name}
Email: {email}
Skills: {skills}
"""

with open("resume.txt", "w") as file:
    file.write(resume)

print("Resume saved to 'resume.txt'")
