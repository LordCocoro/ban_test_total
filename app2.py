from db.db_test import Client,Product,ProductClient
from db.db_test import db

resp = Client.query.all()
resp1 = Product.query.all()
resp2 = ProductClient.query.all()

client1 = Client(ClientID=1,NroDocTit="47133933")
client2 = Client(ClientID=2,NroDocTit="71253247",isComp=True,NroDocComp="47133933")

#db.session.add(client1)
#db.session.add(client2)
#db.session.commit()

product1 = Product(ProductID="CA12",ProdName="Cuenta Ahorros Personales",ProdType="1")
product2 = Product(ProductID="PR14",ProdName="Prestamos Hipotecarios",ProdType="2")
product3 = Product(ProductID="CA13",ProdName="Cuenta Ahorros Premium",ProdType="1")
product4 = Product(ProductID="PR16",ProdName="Prestamo Personal",ProdType="2")
product5 = Product(ProductID="CA34",ProdName="Cuenta de ahorros Preferencial",ProdType="1")

#db.session.add(product1)
#db.session.add(product2)
#db.session.add(product3)
#db.session.add(product4)
#db.session.add(product5)


relation1=ProductClient(Client=client1,Product=product1)
relation2=ProductClient(Client=client1,Product=product2)
relation3=ProductClient(Client=client1,Product=product3)
relation4=ProductClient(Client=client2,Product=product4)
relation5=ProductClient(Client=client2,Product=product5)

#db.session.add(relation1)
#db.session.add(relation2)
#db.session.add(relation3)
#db.session.add(relation4)
#db.session.add(relation5)

#db.session.commit()


print(Client.findClient(nroDoc="47133933"))
print(ProductClient.findProductID(clientID=1))
print(Product.findProduct(productID="CA12"))