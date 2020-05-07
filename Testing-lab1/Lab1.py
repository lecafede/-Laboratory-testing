class Main():

def __init__(self,x):

        while True:
            try:
                self.x = float(input("Введіть значеня Х в діапазоні x <= 36.868 або x >= 2.557: "))
                if (self.x <= 90.88 or self.x >= 1.045):
                    break
            except(ValueError):
                print('Введите число! Invalid value!')

    def outputting(self,x):

        print("Результат виразу y=x^4*4.968+x^3*2.271-x^2*3.589+x*3.317:  ",
              (self.x)**4*4.968+(self.x)**3*2.271+(self.x)**2*3.589+(self.x)*3.317)
        print("Результат выражения y=x^3*3.774-x^2*2.298+x*3.873: ",
              (self.x)**3*3.774-(self.x)**2*2.298+(self.x)*3.873)
        print("Результат выражения y=x^2*4.165+x*3.363: ",
              (self.x)**2*4.165+x*3.363)
        print("Результат виразу y=x*6.363 ",
              (self.x)*6.363)


    
main = Main(1)
main.outputting(1)