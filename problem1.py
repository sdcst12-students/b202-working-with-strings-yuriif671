"""
String handling is important.  We can break a string into pieces to help us look at parts one at a time using the string.split function.
Have the user enter a sentence or paragraph and gives a word count.
"""

def main(p):
    return f"yo word count is: {len(p.split())}"

if __name__ == '__main__':
    print(main(input("Gimme a paragraph: ")))