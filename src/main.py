import os
from dotenv import load_dotenv
from flask import Flask
from apps.user_app.views import user_app
from apps.bank_app.views import bank_app


# load evn variable
load_dotenv()

# create app
app = Flask(__name__)
# configure SECRET KEY
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# register user app
app.register_blueprint(user_app)

# register bank_app
app.register_blueprint(bank_app)


# run app
if __name__ == '__main__':
    # now building
    app.run(port=os.environ.get('PORT'), debug=os.environ.get('DEBUG'))
