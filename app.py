"""Flask app for Cupcakes"""
from flask import Flask,render_template,request
from flask.json import jsonify

from models import connect_db,db,Cupcake,serialize_cupcake


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)






@app.route('/')
def get_page():
    return render_template('index.html')



@app.route('/api/cupcakes')
def get_all_cupcakes():
    cupcakes = [serialize_cupcake(c) for c in Cupcake.query.all()]
    print(cupcakes)
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_a_cupcake(id):
    cupcake = serialize_cupcake(Cupcake.query.get(id))
    
    return jsonify(cupcake=cupcake)


@app.route('/api/cupcakes',methods=["POST"])
def create_cupcake():
    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image'] or None
    new_cupcake = Cupcake(flavor=flavor,size=size,rating=rating,image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    serialized = serialize_cupcake(new_cupcake)
    return jsonify(cupcake=serialized)



@app.route('/api/cupcakes/<int:id>',methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get(id)
    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating= request.json['rating']
    db.session.commit()
    serialized = serialize_cupcake(cupcake)
    return jsonify(update=serialized)

@app.route('/api/cupcakes/<int:id>',methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')