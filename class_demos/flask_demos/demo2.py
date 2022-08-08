from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create instance of flask class / create flask app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/alx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# flask link to/communicate with the database
# link a db
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'PERSON_ID: {self.id} NAME: {self.name}'


db.create_all()


# create index route
@app.route('/')
# create route handler
def index():
    me = Person.query.first()
    return 'Hello ' + me.name + ' !!!'


# always include this at the bottom of your code
# to let you run a flask app through running a python file
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
