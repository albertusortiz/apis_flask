from flask import json, jsonify

def bad_request(error='Bad request'):
    return jsonify({
        'success': False,
        'data': {},
        'message': error,
        'code': 400
    }), 400

def not_found():
    return jsonify({
        'success': False,
        'data': {},
        'message': 'Resource not found.',
        'code': 404
    }), 404

def response(data):
    return jsonify({
        'success': True,
        'data': data
    }), 200