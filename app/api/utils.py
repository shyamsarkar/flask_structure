from flask import jsonify


def unauthorized_error():
    response = jsonify({'message': 'Unauthorized'})
    response.status_code = 401
    return response


def bad_request_error(message):
    response = jsonify({'message': message})
    response.status_code = 400
    return response


def not_found_error(message):
    response = jsonify({'message': message})
    response.status_code = 404
    return response


def internal_server_error(message):
    response = jsonify({'message': message})
    response.status_code = 500
    return response
