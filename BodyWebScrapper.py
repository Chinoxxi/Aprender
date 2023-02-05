import re
import requests
from bs4 import BeautifulSoup

# Set the user agent string
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Make a request to the webpage
response = requests.get("https://www.tanda.co/features/shift-swapping/", headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the title of the webpage
title = soup.title.text

# Create the name of the file using the title of the webpage
filename = re.sub(r"[^\w\s]", "", title) + ".txt"

# Open a new text file in write mode
with open(filename, "w") as file:
    # Find all of the heading and paragraph elements on the webpage
    elements = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p"])

    # Write the title to the file
    file.write(title + "\n")
    # Iterate through the elements and extract the text
    for element in elements:
        if element.name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            # Write the heading to the file
            file.write(element.text + "\n")
        elif element.name == "p":
            # Write the paragraph to the file
            file.write(element.text + "\n")
