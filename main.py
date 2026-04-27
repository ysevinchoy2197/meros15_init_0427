#15-misol
class Dars:
    def __init__(self, nomi):
        self.nomi = nomi

    def uchish(self):
        print("Uchmoqda")

class Ingliztili(Dars):

    def uchish(self):
        print("Dars o‘tilmoqda")


d1 = Dars("Ingliz tili darsi")
i1 = Ingliztili

d1.uchish()
