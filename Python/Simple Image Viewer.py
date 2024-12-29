from PIL import Image

image_path = input("Enter the path to the image: ")
img = Image.open(image_path)
img.show()
