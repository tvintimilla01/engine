
from flask import Blueprint, request, jsonify
#import generate_recommendations
from .recommendation_model import generate_recommendations

main = Blueprint('main', __name__)

@main.route('/recommendations', methods=['POST'])
def get_recommendations():
    data = request.json
    input_data = int(data.get('input', ''))

    try:
        recommendations = generate_recommendations(input_data)
    except:
        return jsonify({'error': "User not Found"}), 400

    return jsonify({
        'recommendations': recommendations
    })