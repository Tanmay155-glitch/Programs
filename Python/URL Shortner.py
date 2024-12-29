urls = {}
original_url = input("Enter original URL: ")
short_url = "short.ly/" + original_url[-6:]
urls[short_url] = original_url

print("Shortened URL:", short_url)
print("Original URL from short link:", urls[short_url])
