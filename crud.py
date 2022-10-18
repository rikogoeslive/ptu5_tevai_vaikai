from sqlalchemy.orm import sessionmaker
from models import engine, Tevas, Vaikas


session = sessionmaker(bind=engine)()

# CRUD
def create_tevas(vardas, pavarde):
    tevas = Tevas(vardas=vardas, pavarde=pavarde)
    session.add(tevas)
    session.commit()
    return tevas

def read_tevai():
    tevai = session.query(Tevas).all()
    return tevai

def create_vaikas(vardas, pavarde, tevas, mokymo_istaiga=None):
    vaikas = Vaikas(
        vardas=vardas, 
        pavarde=pavarde, 
        tevas=tevas, 
        mokymo_istaiga=mokymo_istaiga
    )
    session.add(vaikas)
    session.commit()
    return vaikas

def read_vaikai():
    return session.query(Vaikas).all()

def delete_object(object_class, object_id):
    obj = session.query(object_class).get(object_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    else:
        print(f"Klaida: {object_class.__name__} su ID:{object_id} neegzistuoja")

def update_object(object_class, object_id, **kwargs):
    obj = session.query(object_class).get(object_id)
    if obj and kwargs:
        for column_name, value in kwargs.items():
            if hasattr(obj, column_name):
                setattr(obj, column_name, value)
            else:
                print(f"Klaida: {obj} neturi {column_name} atributo")
        else:
            session.commit()
            return obj
    else:
        print(f"Klaida: {object_class.__name__} su ID:{object_id} neegzistuoja")

# Testuojam
if __name__ == "__main__":
    # --- Ivaikinimo scenarijus
    vaikas = session.query(Vaikas).filter(Vaikas.pavarde.ilike("Super%")).first()
    tevas = session.query(Tevas).filter(Tevas.pavarde.ilike("Jan%")).first()
    ivaikintas = update_object(Vaikas, vaikas.id, tevas=tevas, vardas="Ivaikintas")
    print("Python objektas `ivaikintas`:\n", vaikas)
    print("Perkraunam is DB:\n", read_vaikai())

    # --- Sukuriam superine seima, ir nutrinam teva
    # naujas_tevas = create_tevas("Tevas", "Superinis")
    # naujas_vaikas = create_vaikas("Vaikas", "Superinis", naujas_tevas)
    # print(read_vaikai())
    # delete_object(Tevas, naujas_tevas.id)
    # print(read_vaikai())
