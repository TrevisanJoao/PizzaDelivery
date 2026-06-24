from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

# create databse connection
db = create_engine("sqlite:///database.db")
# create database base
Base = declarative_base()
# create classes/tables of the database
# User
class User(Base):
    __tablename__="Users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String, nullable=False)
    password = Column("password", String)
    active = Column("active", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, name, email, password, active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.active = active
        self.admin = admin



# Orders
class order(Base):
    __tablename__ ="orders"

#    STATUS_ORDERS = (
#        ("PENDING", "PENDING"),
#        ("CANCELD", "CANCELED"),
#        ("FINISHED", "FINISHED")
#    )

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #pending, canceled, finishED
    user = Column("user", ForeignKey("Users.id"))
    price = Column("price", Float)
    # itens

    def __init__(self, user, status="pending", price=0):
        self.user = user
        self.status = status
        self.price = price
        # OrderItens

class OrdersItem(Base):
    __tablename__ ="OrdersItem"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantity = Column("quantity", Integer)
    flavor = Column("flavor", String)
    size = Column("size", String)
    unity_price = Column("unity_price", Float)
    order = Column("order", ForeignKey("orders.id"))

    def __init__(self, quantity, flavor, size, unity_price, order):
        self.quantity = quantity
        self.flavor = flavor
        self.size = size
        self.unity_price = unity_price
        self.order = order

# execute the creation of the metadata of the database

Base.metadata.create_all(db)