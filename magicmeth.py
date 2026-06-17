# Dunder methods are basically magic methods
class Book:
    def __init__(self,title,num_pages,author):
        self.title = title
        self.num_pages = num_pages
        self.author = author

    # __str__ : We can give the string representation of the format when we print it directly to the console
    def __str__(self):
        return f"'{self.title} by {self.author}"
    
    #__eq__ : We can compare if two objects are the same or not!
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author

    #__lt__ : Bascially the lower than operator for objects!
    def __lt__(self,other):
        return self.num_pages < other.num_pages

    #__gt__ : Bascially the greater than operator for objects!
    def __gt__(self,other):
        return self.num_pages > other.num_pages

    #__add__ : To add two objects!
    def __add__(self,other):
        return self.num_pages + other.num_pages

    #__contains__ : To check if a certain keyword is in the object or not!
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    #__getitem__ : Basically indexing for objects!
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} was not found"

book1 = Book("SussyBaka",420,"Red_sPaCe_cReW")
book2 = Book("Anime Wars",69,"Mr.Baka")

print(book1)
print(book1 == book2)
print(book1 < book2)
print(book1 > book2)
print(book1 + book2)
print("Anime" in book2)
print(book1['title'])
print(book2['author'])
print(book2['num_pages'])
print(book1['audio'])