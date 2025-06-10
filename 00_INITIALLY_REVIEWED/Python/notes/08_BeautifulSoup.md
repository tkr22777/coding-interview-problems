# Beautiful Soup

```python
from bs4 import BeautifulSoup
import requests

# Example 1: Load HTML content and create a BeautifulSoup object
html_doc = """
<html>
<head>
    <title>The Dormouse's story</title>
</head>
<body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# Example 2: Accessing data in tags
title = soup.title
print("Title tag:", title)
print("Title text:", title.string)

# Example 3: Finding all instances of a tag
all_a_tags = soup.find_all('a')
for link in all_a_tags:
    print("Anchor text:", link.text)
    print("Href:", link['href'])

# Example 4: Finding tags by attributes
first_id_link = soup.find(id="link1")
print("First link with ID 'link1':", first_id_link)

# Example 5: Using CSS selectors
css_selector_links = soup.select('p.story > a.sister')
for link in css_selector_links:
    print("CSS Selector link text:", link.text)

# Example 6: Navigating the parse tree
parent_of_title = title.parent
print("Parent of the title tag:", parent_of_title.name)

# Example 7: Getting data from a real webpage
url = "http://example.com"
response = requests.get(url)
web_soup = BeautifulSoup(response.text, 'html.parser')
print("Web page title:", web_soup.title.string)

# Example 8: Extracting all URLs from a page
urls = [a['href'] for a in web_soup.find_all('a', href=True)]
print("All URLs found:", urls)
``` 