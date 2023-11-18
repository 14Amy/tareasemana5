from sqlalchemy.orm import sessionmaker
# se importa la clase(s) del
# archivo crear_entidades
from crear_entidades import Ciudades
from crear_entidades import Estadio
# se importa el engine
from base_datos import engine

# Se crea una clase llamada Sessión,
# desde el generador de clases de SQLAlchemy
# sessionmaker.
Session = sessionmaker(bind=engine) # Se usa el engine
# Importante, se crea un objeto llamado session
# de tipo Session, que permite: permitir guardar, eliminar,
# actualizar y generar consultas a la base de datos.
session = Session()

# se crea un objetos de tipo Autor
ciudad1 = Ciudades(nombreciudad="quito", pais="ecuador", continente="america")
ciudad2 = Ciudades(nombreciudad="riobamba", pais="ecuador", continente="america")
ciudad3 = Ciudades(nombreciudad="pillaro", pais="ecuador", continente="america")
ciudad4 = Ciudades(nombreciudad="bolivar", pais="ecuador", continente="america")

estadio1 = Estadio(nombreestadio="liga", ciudad="quito", direccion="america")
estadio2 = Estadio(nombreestadio="barcelona", ciudad="guayaquil", direccion="america")
estadio3 = Estadio(nombreestadio="olimpico", ciudad="quito", direccion="america")
estadio4 = Estadio(nombreestadio="aucas", ciudad="quito", direccion="america")
# se agrega los objetos de tipo Autor a la sesión
# a la espera de un commit
session.add(ciudad1)
session.add(ciudad2)
session.add(ciudad3)
session.add(ciudad4)

session.add(estadio1)
session.add(estadio2)
session.add(estadio3)
session.add(estadio4)

# se necesita confirmar los cambios que existan en la sessió
# se usar commit
session.commit()
