from People import *
from app import *
# from config import *

@app.route("/")
def index():
    person = People.get(ID=1)
    return render_template('home.html', user=person)
