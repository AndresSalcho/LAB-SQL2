import sql
import time
from decimal import Decimal


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
        self.cuadrosAmount2 = 0
        self.cuadroList = []
        self.cuadroList2 = []
        self.end = False

    def buySeq(self):
        data = self.s.getRand()
        try:
            amount = round(data[1] + (data[1] * 0.10), 2)
            print(self.name + " quiere comprar el cuadro " + data[2])
            time.sleep(1)
            if amount <= self.money:
                print(self.name + " compró el cuadro \"" + data[2] + "\" por " + str(amount) + " dólares")
                self.money = round(self.money - amount, 2)
                self.s.buy(data[0], self.number, amount)
                print("A " + self.name + " le quedan " + str(self.money) + " dólares\n")
                self.cuadroList.append(data[2] + " - Costo: " + str(amount))
                self.cuadrosAmount += 1
            if data[1] > self.money:
                print(self.name + " No tiene suficiente dinero para comprarlo!!!\n")
                self.end = True
        except:
            print()

    def sellSeq(self):

        data = self.s.getOwned(self.number)

        if data != 0:
            self.end = False
            print(self.name + " quiere vender el cuadro " + data[2])
            time.sleep(1)
            print(self.name + " vendió el cuadro \"" + data[2] + "\" por " + str(data[1]) + " dólares")
            self.money = round(self.money + data[1], 2)
            self.s.sell(data[0], self.number, self.money)
            print(self.name + " tiene " + str(self.money) + " dólares\n")
            self.cuadrosAmount2 += 1
            self.cuadroList2.append(data[2] + " - Costo: " + str(data[1]))
        else:
            return 0

    def endSeq(self):
        print("\n-------------------------------------------\n" + self.name + " ha comprado " + str(
            self.cuadrosAmount) + " cuadros: \n")
        for i in self.cuadroList:
            print(i)
        print("\n Y ha vendido " + str(
            self.cuadrosAmount2) + " cuadros")
        for i in self.cuadroList2:
            print(i)

    def getState(self):
        return self.end
