"""
Create a dictionary named book with the following key-value pairs:
"title": "The Great Gatsby"
"author": "F. Scott Fitzgerald"
"year": 1925

Add a new key-value pair to the book dictionary: "genre": "Fiction".

Print the dictionary to display the book's information.

Create a list of dictionaries, each representing a book. Include at least three books with different attributes (title, author, year, genre).

Print the different genres associated with the books

Do the same with list comprehension

"""

dic = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald","year": 1925}

dic.update({"genre": "Fiction"})

print(f"Book's information: {dic}")

list_dic = [
    {"title": "The book", "Author": "C.S Lewis", "Year": "1990", "Genre": "Fiction"},
    {"title": "Confession", "Author": "S. Thomas de Aquino", "Year": "400", "Genre": "Philosophy"},
    {"title": "Uma breve Historia do tempo", "Author": "Stephen Hawking", "Year": "1988", "Genre": "Astrophysical"}
]

for i in range(len(list_dic)):
    print("\n", list_dic[i]["Genre"])

print(list_dic)