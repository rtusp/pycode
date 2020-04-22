from flask import request, text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from database.users import User

@app.route('hello')
def hello():
    id = request.args.get("id")
    query = SQLAlchemy().session.query("SELECT 1") # Noncompliant
    user = query.one()
    return "Hello %s" % user.username


