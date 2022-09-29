from flask import Flask,request
from flask_migrate import Migrate
from models import db, User
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/userlist"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
 
#  POST request-add new user
@app.route('/users',methods=['POST','GET'])
def users():

    if request.method=="POST":
        if request.is_json:
            post_data=request.get_json()
            new_user=User(
                name=post_data['name'],
                email=post_data['email'],
                phone=post_data['phone'],
                city=post_data['city'],
                country=post_data['country'],
                dob=post_data['dob'])
            db.session.add(new_user)
            db.session.commit()
            return {"message":  f"user {new_user.name} has been added successfully."},201
        else:
             return {"error":"Check data format"},403
        
# GET request-fetch all the users
    elif request.method=='GET':
        users=User.query.all()
        results=[{
            "name":user.name,
            "email":user.email,
            "phone":user.phone,
            "city":user.city,
            "country":user.country,
            "dob":user.dob
        } for user in users]
    return {"count":len(results),"users":results},200

@app.route('/users/<user_id>',methods=['GET','PUT',"DELETE"])
def list(user_id):
    user=User.query.get_or_404(user_id)
# GET- fetch individual user data
    if request.method=='GET':
        response={
            "name":user.name,
            "email":user.email,
            "phone":user.phone,
            "city":user.city,
            "country":user.country,
            "dob":user.dob
        }
        return {"message":'SUCCESS',"user":response},200
# PUT-update the data of individual user
    elif request.method=='PUT':
        data=request.get_json()
        user.name=data['name']
        user.email=data['email']
        user.phone=data['phone']
        user.city=data['city']
        user.country=data['country']
        user.dob=data['dob']
        db.session.add(user)
        db.session.commit()
        return {"message": f" user {user.name} successfully updated"},200
# DELETE-remove the user data
    elif request.method=='DELETE':
        db.session.delete(user)
        db.session.commit()
        return{"message": f"user {user.name} deleted successfully."},200
        
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')