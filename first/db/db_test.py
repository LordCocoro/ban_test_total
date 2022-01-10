from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Client(db.Model):
    ClientID = db.Column(db.Integer, primary_key=True)
    NroDocTit = db.Column(db.String(80),nullable=False)
    isComp = db.Column(db.Boolean, default=False)
    NroDocComp = db.Column(db.String(120),default="")

    def __repr__(self):
        return '<Client %r>' % self.ClientID
    def findClient(nroDoc):
        clientid = Client.query.filter_by(NroDocTit=nroDoc).first()
        return 'Client %r' % (clientid.ClientID)

class Product(db.Model):
    ProductID = db.Column(db.String(12), primary_key=True)
    ProdName = db.Column(db.String(80),  nullable=False)
    ProdType = db.Column(db.String(80),  nullable=False)
    
    def __repr__(self):
        return '<Product %r>' % self.ProductID
    def findProduct(productID):
        productType = Product.query.filter_by(ProductID=productID).first()
        return 'Product Type %r' % (productType.ProdType)

class ProductClient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.ClientID'),
        nullable=False)
    Client = db.relationship('Client',
        backref=db.backref('clients', lazy=True))
    
    product_id = db.Column(db.String(12), db.ForeignKey('product.ProductID'),
        nullable=False)
    Product = db.relationship('Product',
        backref=db.backref('products', lazy=True))

    def __repr__(self):
        return '<Client %r and Product %r>' % (self.client_id,self.product_id)
    def findProductID(clientID):
        product = ProductClient.query.filter_by(client_id=clientID).all()
        arrProducts = []
        for p in product:
            arrProducts.append(p.Product)
        return 'Products %r' % (arrProducts)
