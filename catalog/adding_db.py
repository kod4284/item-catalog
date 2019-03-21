from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, User, Catalog, Item

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Daewoong Ko", email="kodw0402@gmail.com")
session.add(User1)
session.commit()

User2 = User(name="Dongsuk Lim", email="dlim0305@gmail.com")
session.add(User2)
session.commit()

# Create dummy catalogs
Catalog1 = Catalog(name="Soccer")
session.add(Catalog1)
session.commit()

Catalog2 = Catalog(name="Basketball")
session.add(Catalog2)
session.commit()

# Create items
Item1 = Item(user_id=1, name="Soccer ball", description="This is a Soccer ball", catalog=Catalog1)
session.add(Item1)
session.commit()

Item2 = Item(user_id=2, name="Soccer uniform", description="This is a Soccer uniform", catalog=Catalog1)
session.add(Item2)
session.commit()

Item3 = Item(user_id=1, name="Basketball ball", description="This is a Basketball ball", catalog=Catalog2)
session.add(Item3)
session.commit()

Item4 = Item(user_id=1, name="Basketball uniform", description="This is a Basketball uniform", catalog=Catalog2)
session.add(Item4)
session.commit()

print "added catalogs and items!"
