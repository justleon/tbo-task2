from project import db, app
from project.utils.masking_util import mask_str


# Customer model
class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    city = db.Column(db.String(64))
    age = db.Column(db.Integer)
    pesel = db.Column(db.String(64))
    street = db.Column(db.String(128))
    appNo = db.Column(db.String(10))

    def __init__(self, name, city, age, pesel, street, appNo):
        self.name = name
        self.city = city
        self.age = age
        self.pesel = pesel
        self.street = street
        self.appNo = appNo
        print("Getting: " + str(self), flush=True)

    def __repr__(self):
        return (f"Customer(ID: {self.id}, Name: {self.name}, City: {self.city}, Age: {self.age}, "
                f"Pesel: {mask_str(self.pesel)}, Street: {mask_str(self.street)}, AppNo: {mask_str(self.appNo)})")


with app.app_context():
    db.create_all()
