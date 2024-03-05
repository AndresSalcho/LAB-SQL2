import threading
from time import sleep
from random import randint
import comprador as com
import sql

s = sql.db()
s.__int__()


class threadpool:

    def __int__(self):
        self.Threads = 5

        self.c1 = com.Comprador()
        self.c2 = com.Comprador()
        self.c3 = com.Comprador()
        self.c4 = com.Comprador()
        self.c5 = com.Comprador()

        self.sem = threading.Semaphore(1)

        self.personaLista = []

    def funcion(self, thread):
        self.sem.acquire()
        self.personaLista[thread].buySeq()
        sleep(2)
        self.sem.release()

    def start(self):
        naux = []
        for i in range(5):
            pas = False
            aux = randint(1, 5)

            while not pas:
                if naux.__contains__(aux):
                    aux = randint(1, 5)
                else:
                    pas = True

            naux.append(aux)

        self.c1.__int__(str(naux[0]))
        self.c2.__int__(str(naux[1]))
        self.c3.__int__(str(naux[2]))
        self.c4.__int__(str(naux[3]))
        self.c5.__int__(str(naux[4]))

        self.personaLista.append(self.c1)
        self.personaLista.append(self.c2)
        self.personaLista.append(self.c3)
        self.personaLista.append(self.c4)
        self.personaLista.append(self.c5)

        while not s.isnull() and not self.cant():
            threadLista = []

            for num_thread in range(self.Threads):
                hiloX = threading.Thread(target=self.funcion(num_thread))
                threadLista.append(hiloX)

            threadLista[0].start()
            threadLista[1].start()
            threadLista[2].start()
            threadLista[3].start()
            threadLista[4].start()

        print("\nYa nadie puede seguir comprando\n")

        sleep(5)

        self.personaLista[0].endSeq()
        sleep(5)
        self.personaLista[1].endSeq()
        sleep(5)
        self.personaLista[2].endSeq()
        sleep(5)
        self.personaLista[3].endSeq()
        sleep(5)
        self.personaLista[4].endSeq()

    def cant(self):
        if not self.personaLista[0].getState() and not self.personaLista[1].getState() and not self.personaLista[2].getState() and not self.personaLista[3].getState() and not self.personaLista[4].getState():
            return False
        else:
            return True
