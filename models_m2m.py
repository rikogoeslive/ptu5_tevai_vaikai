from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/tevai_vaikai_m2m.db')
Base = declarative_base()


tevai_vaikai_table = Table('tevai_vaikai', Base.metadata, 
    Column('tevas_id', Integer, ForeignKey("tevas.id")),
    Column('vaikas_id', Integer, ForeignKey("vaikas.id")),
)


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    vaikai = relationship(
        "Vaikas", 
        secondary=tevai_vaikai_table, 
        back_populates="tevai",
    )

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymo_istaiga = Column("mokykla", String, nullable=True)
    tevai = relationship(
        "Tevas",
        secondary=tevai_vaikai_table,
        back_populates="vaikai",
    )

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
