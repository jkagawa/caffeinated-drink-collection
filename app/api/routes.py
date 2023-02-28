from flask import Blueprint, request, jsonify, render_template
from helpers import token_required
from models import db, User, Drink, drink_schema, drink_multi_schema, user_schema

api = Blueprint('ap', __name__, url_prefix='/api')

# Add new drink endpoint
@api.route('/drink', methods = ['POST'])
@token_required
def add_drink(current_user_token):
    name = request.json['name']
    caffeine_per_oz = request.json['caffeine_per_oz']
    color = request.json['color']
    description = request.json['description']
    image_url = request.json['image_url']
    user_token = current_user_token.token

    print(f'User\'s token: {current_user_token.token}')

    try:
        drink = Drink(name, caffeine_per_oz, color, description, image_url, user_token)
        db.session.add(drink)
        db.session.commit()

        response = drink_schema.dump(drink)
        return jsonify(response)
    except:
        return jsonify({'message' : 'Failed to add item'}), 500

# Get all drinks added by user
@api.route('/drink', methods = ['GET'])
@token_required
def get_drink(current_user_token):
    user_token = current_user_token.token
    drink = Drink.query.filter_by(user_token=user_token).all()
    if drink:
        response = drink_multi_schema.dump(drink)
        return jsonify(response)
    return jsonify({'message' : 'Item not found'}), 404

# Get single drink added by user
@api.route('/drink/<id>', methods = ['GET'])
@token_required
def get_single_drink(current_user_token, id):
    user_token = current_user_token.token
    drink = Drink.query.filter_by(user_token=user_token, id=id).all()
    if drink:
        response = drink_schema.dump(drink)
        return jsonify(response)
    return jsonify({'message' : 'Item not found'}), 404
    
# Update drink endpoint
@api.route('/drink/<id>', methods = ['POST','PUT'])
@token_required
def update_drink(current_user_token, id):
    user_token = current_user_token.token
    drink = Drink.query.filter_by(user_token=user_token, id=id).all()
    if drink:
        drink.name = request.json['name']
        drink.caffeine_per_oz = request.json['caffeine_per_oz']
        drink.color = request.json['color']
        drink.description = request.json['description']
        drink.image_url = request.json['image_url']
        drink.user_token = current_user_token.token

        db.session.commit()
        response = drink_schema.dump(drink)
        return jsonify(response)
    return jsonify({'message' : 'Item not found'}), 404

# Delete drink endpoint
@api.route('/drink/<id>', methods = ['DELETE'])
@token_required
def delete_drink(current_user_token, id):
    user_token = current_user_token.token
    drink = Drink.query.get(id)
    if drink and drink.user_token == user_token:
        db.session.delete(drink)
        db.session.commit()
        response = drink_schema.dump(drink)
        return jsonify(response)
    return jsonify({'message' : 'Item not found'}), 404

# Delete user endpoint
@api.route('/user/<id>', methods = ['DELETE'])
@token_required
def delete_user(current_user_token, id):
    user_token = current_user_token.token
    user = User.query.get(id)
    if user and user.token == user_token:
        db.session.delete(user)
        db.session.commit()
        response = user_schema.dump(user)
        return jsonify(response)
    return jsonify({'message' : 'User not found'}), 404