from flask import *
import datetime
from bson.objectid import ObjectId
from database import MongoDBHelper
import hashlib

web_app = Flask("Finance Manager")

@web_app.route("/")
def index():
    return render_template('Indexx.html')

@web_app.route("/register")
def register():
    return render_template('registerr.html')


@web_app.route("/home")
def home():
    return render_template('Home.html', email=session['user_email'])


@web_app.route("/register-user", methods=['POST'])
def register_user():

    user_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
        'income': float(request.form['income']),
        'housing_status': request.form['housing_status'],
        'createdOn': datetime.datetime.today()
    }

    print(user_data)
    db = MongoDBHelper(collection="user")

    result = db.insert(user_data)

    # Test the same
    user_id = result.inserted_id
    session['user_id'] = str(user_id)
    session['user_name'] = user_data['name']
    session['user_email'] = user_data['email']
    session['user_income'] = float(user_data['income'])
    session['user_housing_status'] = user_data['housing_status']
    return render_template('Home.html', email=session['user_email'])


@web_app.route("/login-user", methods=['POST'])
def login_vet():

    user_data = {
        'email': request.form['email'],
        'password': hashlib.sha256(request.form['pswd'].encode('utf-8')).hexdigest(),
    }

    print(user_data)
    db = MongoDBHelper(collection="user")
    documents = db.fetch(user_data)
    print(documents, type(documents))
    if len(documents) == 1:
        session['user_id'] = str(documents[0]['_id'])
        session['user_email'] = documents[0]['email']
        session['user_name'] = documents[0]['name']
        print(vars(session))
        return render_template('home.html', email=session['user_email'], name=session['user_name'])
    else:
        return render_template('error.html')


@web_app.route("/logout")
def logout():
    session['user_id'] = ""
    session['user_email'] = ""
    return redirect("/")



def main():

    web_app.secret_key = 'finanacemanager-key-1'
    web_app.run(port=5084)


if __name__ == "__main__":
    main()






