from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/tevai_vaikai.db')
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    vaikai = relationship("Vaikas", back_populates="tevas")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde})"


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    mokymo_istaiga = Column("mokykla", String, nullable=True)
    # ForeignKey veda i lentelės pavadinimą
    tevas_id = Column("tevas_id", Integer, ForeignKey("tevas.id"))
    # Relationship veda į objekto pavadinimą
    tevas = relationship("Tevas", back_populates="vaikai")

    def __repr__(self):
        return f"({self.id}, {self.vardas}, {self.pavarde}, {self.tevas})"


if __name__ == "__main__":
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
