#herencias
from clase_constructor import operaciones

class calculo(operaciones):
    #metodo __init__ constructor clase heredado mas un atributo nuevo
    def __init__(self,a,b, c):
        super().__init__(a,b)
        self.numero3 =c

    def total(self):

        if self.numero3==1:
            super().sumar()
        if self.numero3==2:
            super().restar()
        if self.numero3==3:
            super().multiplicar()

cal= calculo(3,5,3)

cal.total()
