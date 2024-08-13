from bs4 import BeautifulSoup

# Read the HTML file
with open('index.html', 'r') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all course divs
courses = soup.find_all('div', class_='course')

# Loop through each course and extract information
for course in courses:
    # Extract course name
    course_name = course.find('h3').text
    
    # Extract course description
    description = course.find('p').text
    
    # Extract course price
    price = course.find('button').text.split()[-1]
    
    # # Print the extracted information
    # print(f"Course: {course_name}")
    # print(f"Description: {description}")
    # print(f"Price: {price}")
    # print("-" * 50)

#extract information using find_all method h3 tag
# course_names = soup.find_all('h3')
# for name in course_names:
#     print(name.text)

#find all course Divs with specific class 
# course_divs = soup.find_all('div', class_='course')
# for course in course_divs:
#     print(course)

#find all button tags no matter where they are
# button_tags = soup.find_all('button')
# for button in button_tags:
#     print(button.text)

#find all courses with specific text in a button
#     specific_courses = soup.find_all('div', class_='course-box')
# for course in specific_courses:
#     if 'Start for 50$' in course.find('button').text:
#         print(course.find('h3').text)

#find all the p tags 
paragraph_tags = soup.find_all('p')
for p in paragraph_tags:
    print(p.text)
