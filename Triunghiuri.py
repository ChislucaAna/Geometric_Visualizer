import math
from Points import Punct
import matplotlib.pyplot as plt

class Triunghi:
    def __init__(self, p1,p2,p3):
        if isinstance(p1, Punct) and isinstance(p2, Punct) and isinstance(p3,Punct):
            self.p1 = p1
            self.p2 = p2
            self.p3 = p3 
        else:
            raise TypeError("P1 si P2 TREBUIE SA FIE PUNCTE")

    def lungime_laturi(self):
        diff_x = self.p2.x - self.p1.x
        diff_y = self.p2.y - self.p1.y
        p1p2= (abs(diff_x)**2 + abs(diff_y)**2)**0.5

        diff_x = self.p3.x - self.p1.x
        diff_y = self.p3.y - self.p1.y
        p1p3= (abs(diff_x)**2 + abs(diff_y)**2)**0.5

        diff_x = self.p3.x - self.p2.x
        diff_y = self.p3.y - self.p2.y
        p2p3= (abs(diff_x)**2 + abs(diff_y)**2)**0.5

        return p1p2,p1p3,p2p3
    
    def perimetru(self):
        a,b,c = self.lungime_laturi()
        return a+b+c

    def arie(self): #folosind formula lui Heron
        a,b,c = self.lungime_laturi()
        p = self.perimetru() /2
        return (p*(p-a)*(p-b)*(p-c))**0.5
    
    def este_valid(self):
        a, b, c = self.lungime_laturi()
        return a + b > c and a + c > b and b + c > a

    def este_dreptunghic(self):
        a, b, c = sorted(self.lungime_laturi())  # Sort
        return math.isclose(a**2 + b**2, c**2) #functie de comparare a numerelor de tip float

    def tip_triunghi(self):
        a, b, c = self.lungime_laturi()
        if a == b == c:
            return "echilateral"
        elif a == b or b == c or a == c:
            return "isoscel"
        elif self.este_dreptunghic():
            return "dreptunghic"
        else:
            return "scalen"
    
    def plot(self):
        x_coords = [self.p1.x, self.p2.x, self.p3.x, self.p1.x] 
        y_coords = [self.p1.y, self.p2.y, self.p3.y, self.p1.y]
        
        plt.figure()
        plt.plot(x_coords, y_coords, marker='o')  # Draw the triangle
        
        plt.text(self.p1.x, self.p1.y, 'P1', fontsize=12, ha='right')
        plt.text(self.p2.x, self.p2.y, 'P2', fontsize=12, ha='right')
        plt.text(self.p3.x, self.p3.y, 'P3', fontsize=12, ha='right')
        
        #pentru scalabilitatea reprezentarii
        plt.xlim(min(x_coords) - 1, max(x_coords) + 1)
        plt.ylim(min(y_coords) - 1, max(y_coords) + 1)
        
        plt.gca().set_aspect('equal', adjustable='box')  # Unitatea sa fie const pe axe
        plt.grid(True)
        plt.show()




