# Utilities

<details>
<summary><strong>Functions & Random</strong></summary>

```python
# Range function
range(9)                                        # 0 - 8
range(0, 9)                                     # 0 - 8

# Random operations
import random

random.random()                                 # Random float between 0 and 1
random.randint(1, 100)                          # Random int between two numbers (inclusive)
random.choice(['apple', 'banana', 'cherry'])   # Random element from list
random.shuffle(sample_list)                     # Shuffles a list in place

# Reproducible randomness
random.seed(42)                                 # Set seed for reproducibility
seeded_random = random.random()                 # Deterministic result with seed
```

</details>

<details>
<summary><strong>Regular Expressions</strong></summary>

```python
import re

# Basic patterns
re.findall(r'\d+', "There are 24 hours in 1 day.")                    # ['24', '1']
re.split(r'\W+', "Words, separated, by, non-alpha characters!")       # Split by non-word chars
re.sub("Spain", "Italy", "The rain in Spain stays mainly.")           # Replace
re.search(r'^\w+', "Starts early, ends late.").group()               # 'Starts'

# Common patterns
re.findall(r'\b[Ss]\w+', "Sun shines after storm.")                   # Words starting with S/s
re.fullmatch(r'\d+', "12345")                                         # Exact match
re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
           "Contact info@example.com or support@sample.org.")         # Email addresses
re.fullmatch(r'\d{3}-\d{3}-\d{4}', "123-456-7890")                   # Phone format
re.findall(r'\#\w+', "Loving #sunny weather! #funinthesun")           # Hashtags
re.fullmatch(r'#[A-Fa-f0-9]{6}', "#1A2B3C")                          # Hex colors

# Split patterns
re.split(r'\s+', "Hello world! Welcome to coding.")                   # Split by whitespace
re.split(r'[,.!?]+', "Hello, world! How are you?")                    # Split by punctuation
re.split(r'\n', "Line one\nLine two\nLine three")                     # Split by newlines
re.split(r'\t', "Column1\tColumn2\tColumn3")                          # Split by tabs
re.split(r'[;,\s]+', "Apple; Banana, Orange Blueberry")               # Multiple delimiters
re.split(r'(?=[A-Z])', "OneTwoThree")                                 # Split at uppercase
```

</details>

<details>
<summary><strong>Datetime</strong></summary>

```python
import datetime

# Current date and time
now = datetime.datetime.now()
today = datetime.date.today()
current_year = now.year
current_month = now.month
current_day = now.day

# Create specific dates
specific_date = datetime.date(2024, 4, 26)
specific_time = datetime.datetime(2024, 4, 26, 12, 30)

# Date arithmetic
future_date = now + datetime.timedelta(days=100)
five_days_ago = now - datetime.timedelta(days=5)
time_difference = datetime.date(2024, 12, 31) - datetime.date(2024, 1, 1)
print(time_difference.days)                                           # Days between dates

# Comparisons
date1 = datetime.datetime(2024, 4, 26)
date2 = datetime.datetime(2024, 5, 1)
print(date1 < date2)                                                  # True
same_day = date1.date() == now.date()

# Formatting and parsing
formatted = now.strftime("%A, %B %d, %Y %H:%M:%S")
parsed = datetime.datetime.strptime("2024-04-26 12:00", "%Y-%m-%d %H:%M")

# Utilities
day_of_week = now.weekday()                                           # 0=Monday, 6=Sunday
beginning_of_day = datetime.datetime.combine(today, datetime.time())

# Calculate age
birthdate = datetime.date(1990, 4, 26)
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
```

</details> 