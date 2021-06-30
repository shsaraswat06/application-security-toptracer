from flask import Flask, abort, jsonify, request
from worktestauthproblem.request_verification import verify_request

app = Flask(__name__)
APPLICATION_NAME = "application-service-1"

@app.errorhandler(401)
def request_unauthorized(e):
    return jsonify(error=str(e)), 401


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/protected_endpoint", methods=["GET"])
@verify_request
def authenticate(service):
    access = service.get_application_access(app_name=APPLICATION_NAME)
    if not access.get('can-access-data'):
        abort(401, description='Service doesn\'t have access to this application data')
    return jsonify({"secret-data": "very very secret"})


@app.route("/add_service", methods=["POST"])
@verify_request
def add_service(service):
    access = service.get_application_access(app_name=APPLICATION_NAME)
    if not access.get('can-create-service'):
        abort(401, description='Service doesn\'t have access to add service')
    body = request.json
    service_name = body.get('name')
    applications = body.get('applications')
    if service.add_service(service_name=service_name, applications=applications):
        return jsonify({"response": "Service added"})
    else:
        return jsonify({"response": "Service already added"})

if __name__ == '__main__':
    # Example application is run on port 5001. If this is changed, make sure that this is reflected
    # in `mocked_client.py`
    app.run(port=5001, debug=True)
