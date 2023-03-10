"""Blogly application."""

from flask import Flask,redirect,render_template,request,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, User ,connect_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

app.config['SECRET_KEY'] ="azertyqwerty"
app.config['DEBUG_TB_INTERCEPT_REDIRECT'] = False
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.errorhandler(404)

def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    """Home page."""
    return redirect('/users')

@app.route("/users")
def users():
    """Users page."""
    users = User.get_users()
    users.order_by(User.last_name,User.first_name)
    return render_template("users.html",users=users.all(),count=users.count())

@app.route("/users/new")
def users_new():
    """Add user page."""
    return render_template("add-users.html")

@app.route("/users/new",methods=["POST"])
def users_new_add():
    """Send user data page."""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    imageurl = request.form.get("imageurl")

    if firstname == "":
      flash(f"Fill the field First name")
      return redirect('/users/new')
    if lastname == "":
      flash(f"Fill the field Last name")
      return redirect('/users/new')
    else:
      ok = User.add_users(firstname, lastname, imageurl)
      if ok:
         flash(f"User added Successfully")
         return redirect('/users')
      else:
          return
      
@app.route("/users/<int:id>")
def users_details(id):
    """Details user page."""
    user = User.get_user_by_id(id)
    return render_template("users-details.html",user=user)

@app.route("/users/<int:id>/edit")
def users_edit(id):
    """Edit user page."""
    user = User.get_user_by_id(id)
    return render_template("edit-users.html",user=user)

@app.route("/users/<int:id>/edit",methods=["POST"])
def users_edit_save(id):
    """update user data page."""
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    imageurl = request.form.get("imageurl")

    if firstname == "":
      flash(f"Fill the field First name")
      return redirect(f"/users/{id}/edit")
    if lastname == "":
      flash(f"Fill the field Last name")
      return redirect(f"/users/{id}/edit")
    else:
      ok = User.update_users(id,firstname, lastname, imageurl)
      if ok:
         flash(f"User up to date Successfully")
         return redirect('/users')
      else:
          return

@app.route("/users/<int:id>/delete")
def delete_users(id):
    """delete user."""
    ok = User.delete_users(id)
    if ok:
         flash(f"User deleted successfully")
    return redirect('/users')
   