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

    def getMyName(self, number):
        self.crs.execute("select Nombre, Apellidos from dbo.Usuarios "
                         "where ID_usuario = " + number)
        res = self.crs.fetchone()
        return res[0] + " " + res[1]

    def getMyMoney(self, number):
        self.crs.execute("select Dinero from dbo.Usuarios "
                         "where ID_usuario = " + number)
        res = self.crs.fetchval()
        return float(res)

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

    def buy(self, selection, identifyer, amount):
        self.crs.execute("exec dbo.buyTransac " + str(selection) + "," + identifyer + "," + str(amount))
        self.crs.commit()

    def restart(self):
        self.crs.execute("exec resetseq")
        self.crs.commit()

    def restartCustom(self, amount):
        self.crs.execute("exec resetcustom " + amount)
        self.crs.commit()

    def isnull(self):
        self.crs.execute("select COUNT(*) From dbo.Cuadros "
                         "Where Propietario is NULL")
        res = self.crs.fetchval()

        if res != 0:
            return False
        else:
            return True
