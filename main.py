from flask import Flask
from data import db_session
from data.users import *
from data.news import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.sqlite")
    session = db_session.create_session()
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Homer'
    user.name = 'Simpson'
    user.age = 42
    user.position = 'sofa guardian'
    user.speciality = 'programmer'
    user.address = 'module_2'
    user.email = 'homer_proger@mars.org'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Bart'
    user.name = 'Simpson'
    user.age = 15
    user.position = 'captain helper'
    user.speciality = 'cleaner'
    user.address = 'module_3'
    user.email = 'bart_the_cleaner@mars.org'
    session.add(user)
    session.commit()
    user = User()
    user.surname = 'Harry'
    user.name = 'Potter'
    user.age = 17
    user.position = 'ex-captain'
    user.speciality = 'space magic driver'
    user.address = 'module_1'
    user.email = 'harry_magic@mars.org'
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()
