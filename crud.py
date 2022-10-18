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

def update_tevas(tevas_id, **kwargs):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        if "vardas" in kwargs:
            tevas.vardas = kwargs["vardas"]
        if "pavarde" in kwargs:
            tevas.pavarde = kwargs["pavarde"]
        session.commit()
    else:
        print(f"Klaida: Tevas su ID:{tevas_id} neegzistuoja")

def delete_tevas(tevas_id):
    tevas = session.query(Tevas).get(tevas_id)
    if tevas:
        session.delete(tevas)
        session.commit()
        return True
    else:
        print(f"Klaida: Tevas su ID:{tevas_id} neegzistuoja")

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

# Testuojam
if __name__ == "__main__":
    # - Naujas Vaikas
    # tevas = session.query(Tevas).get(1)
    # naujas_vaikas = create_vaikas(
    #     "Emilija", "Januskeviciute", 
    #     tevas, "Scuola di Staggia Sienese"
    # )
    # print(read_tevai())
    print(read_vaikai())
    # - Naujas Tevas
    # naujas_tevas = create_tevas("Kestutis", "Januskevicius")
    # print(naujas_tevas.id, naujas_tevas.vardas, naujas_tevas.pavarde)
    # - Atnaujintas Tevas
    # update_tevas(1, vardas="Geras", pavarde="Programuotojas")
    # update_tevas(1, vardas="Neblogas")
    # - Trinamas Tevas
    # print(delete_tevas(1))
