class Rectangle:
    def __init__(self,width,height):
        self._width=width   # _width means private width!
        self._height=height
    @property
    def width(self):
        return f"{self._width:.2f}cm"
    @property
    def height(self):
        return f"{self._height:.2f}cm"
    
    # Setter
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width = new_width
        else:
            print("Width must be positive")
    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height = new_height
        else:
            print("Height must be positive")
    
    # Deleter
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle=Rectangle(3,4)
print(rectangle._width)
print(rectangle._height)
del rectangle.width
del rectangle.height