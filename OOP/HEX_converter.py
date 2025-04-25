class Colour:
    def __init__(self, hex_code):
        self.hex_code = hex_code
        self.red = int(self.hex_code[1:3],16)
        self.green = int(self.hex_code[3:5],16)
        self.blue = int(self.hex_code[5:7],16)

colour = Colour("#ff0000")
print(colour.red)
print(colour.green)
print(colour.blue)

colour2 = Colour("#00ff2d")
print(colour2.red)
print(colour2.green)
print(colour2.blue)

colour3 = Colour("#aacce4")
print(colour3.red)
print(colour3.green)
print(colour3.blue)
