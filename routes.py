from flask import Flask, render_template, request, session, redirect, url_for
from models import  Place
from forms import AddressForm

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = # add your Heroku Postgres database URL here
#db.init_app(app)

app.secret_key = "development-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")


@app.route("/home", methods=["GET", "POST"])
def home():
 # if 'email' not in session:
  #  return redirect(url_for('login'))

  form = AddressForm()

  places = []
  my_coordinates = (37.4221, -122.0844)

  if request.method == 'POST':
    if form.validate() == False:
      return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)
    else:
      # get the address
      address = form.address.data

      # query for places around it
      p = Place()
      my_coordinates = p.address_to_latlng(address)
      places = p.query(address)

      # return those results
      return render_template('home.html', form=form, my_coordinates=my_coordinates, places=places)

  elif request.method == 'GET':
    return render_template("home.html", form=form, my_coordinates=my_coordinates, places=places)

if __name__ == "__main__":
  app.run(debug=True)
