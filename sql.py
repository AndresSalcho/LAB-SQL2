import pyodbc as sql


class db:
    def __int__(self):
        self.server = "localhost"
        self.db = "GALERIA_ARTE"
        self.user = "adminSubasta"
        self.password = "muyseguro123"

        try:
            self.con = sql.connect("DRIVER={ODBC Driver 17 for SQL server}; Server=" + self.server + ";DATABASE="
                                   + self.db + ";UID=" + self.user + ";PWD=" + self.password)
            self.crs = self.con.cursor()
        except():
            print("Ocurrió un error, no se ha podido conectar")

    # Realiza un select para obtener el nombre del usuario
    def getMyName(self, number):
        self.crs.execute("select Nombre, Apellidos from dbo.Usuarios "
                         "where ID_usuario = " + number)
        res = self.crs.fetchone()
        return res[0] + " " + res[1]

    # Realiza un select para obtener el dinero del usuario
    def getMyMoney(self, number):
        self.crs.execute("select Dinero from dbo.Usuarios "
                         "where ID_usuario = " + number)
        res = self.crs.fetchval()
        return float(res)

    # Le da al usuario un cuadro aleatorio sin dueño
    def getRand(self):
        self.crs.execute("exec getRandom")
        res = self.crs.fetchone()
        try:
            if res is not None:
                return res
            else:
                self.crs.execute("exec auxRandom")
                res = self.crs.fetchone()
                return res
        except:
            self.crs.execute("exec auxRandom")
            res = self.crs.fetchone()
            return res

    # Le da al usuario un cuadro que ya haya comprado
    def getOwned(self, identifyer):
        self.crs.execute("exec getOwned " + identifyer)
        res = self.crs.fetchone()
        try:
            if res is not None:
                return res
            else:
                return 0
        except:
            return 0

    # Ejecuta un procedure que actualiza las tablas para hacer la compra
    def buy(self, selection, identifyer, amount):
        self.crs.execute("exec dbo.buyTransac " + str(selection) + "," + identifyer + "," + str(amount))
        self.crs.commit()

    # Ejecuta un procedure que actualiza las tablas para hacer la venta
    def sell(self, selection, identifyer, amount):
        self.crs.execute("exec dbo.sellTransac " + str(selection) + "," + identifyer + "," + str(amount))
        self.crs.commit()

    # Reinicia las tablas para empezar desde 0
    def restart(self):
        self.crs.execute("exec resetseq")
        self.crs.commit()

    # Reinicia las tablas con una cantidad de dinero custom
    def restartCustom(self, amount):
        self.crs.execute("exec resetcustom " + amount)
        self.crs.commit()

    # Hace un select para ver si aun quedan cuadros sin dueño
    def isnull(self):
        self.crs.execute("select COUNT(*) From dbo.Cuadros "
                         "Where Propietario is NULL")
        res = self.crs.fetchval()

        if res != 0:
            return False
        else:
            return True
