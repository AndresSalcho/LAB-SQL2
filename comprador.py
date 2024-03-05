import sql


class Comprador:
    def __init__(self):
        self.end = None

    def __int__(self, number):
        self.s = sql.db()
        self.s.__int__()
        self.number = number
        self.name = self.s.getMyName(number)
        self.money = self.s.getMyMoney(number)
        self.cuadrosAmount = 0
        self.cuadroList = []
        self.end = False

    def buySeq(self):

        data = self.s.getRand()
        try:
            if not self.end:

                print(self.name + " quiere comprar el cuadro " + data[2])

                if data[1] <= self.money:
                    print(self.name + " compró el cuadro \"" + data[2] + "\" por " + str(data[1]) + " dólares")
                    self.money -= float(data[1])
                    self.s.buy(data[0], self.number, self.money)
                    print("A " + self.name + " le quedan " + str(self.money) + " dólares\n")
                    self.cuadroList.append(data[2] + " - Costo: " + str(data[1]))
                    self.cuadrosAmount += 1
                if data[1] > self.money:
                    print(self.name + " No tiene suficiente dinero para comprarlo!!!\n")
                    self.end = True
        except:
            print("ERROR")

    def endSeq(self):
        print("\n-------------------------------------------\n" + self.name + " ha comprado " + str(self.cuadrosAmount) + " cuadros: \n")
        for i in self.cuadroList:
            print(i)

    def getState(self):
        return self.end
