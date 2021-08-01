from flask import json, jsonify

def response(data):
    return jsonify(
        {
            'success': True,
            'data': data
        }
    ), 200