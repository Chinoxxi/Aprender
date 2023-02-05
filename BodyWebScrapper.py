import requests
import re
from bs4 import BeautifulSoup

# List of URLs to scrape
urls = [
    "https://blog.hubspot.com/sales/linkedin-summary-examples",
    "https://www.tanda.co/features/rosters/",
    
]

# Iterate through the list of URLs
for url in urls:
    # Make a request to the webpage
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.8",
    }
    response = requests.get(url, headers=headers)

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
                # Encode the heading to ASCII and write it to the file
                file.write(element.text.encode("ascii", "ignore").decode() + "\n")
            elif element.name == "p":
                # Encode the paragraph to ASCII and write it to the file
                file.write(element.text.encode("ascii", "ignore").decode() + "\n")

