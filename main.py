import sql
import hilos

s = sql.db()
s.__int__()

# Reinicia los valores de las TABLAS en SQL
s.restart()

# Iniciar con una cantidad custom de dinero
# s.restartCustom("100000")

# Inicio
h = hilos.threadpool()
h.__int__()
h.start()
