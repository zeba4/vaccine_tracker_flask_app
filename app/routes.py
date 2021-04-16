# """ Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper
from urllib.parse import unquote
import sys

city_id_global = -1
date_global = ''
type_global = ''

@app.route("/delete/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def delete(city_id, date, type_param):
    """ recieved post requests for entry delete """

    try:
        db_helper.remove_distribution(city_id, unquote(date), unquote(type_param))
        result = {'success': True, 'response': 'Removed city distribution record for that date and type'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    # print(result)
    # print(city_id)
    # print(date)
    # print(type_param)
    return jsonify(result)


@app.route("/edit/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def update(city_id, date, type_param):
    """ recieved post requests for entry updates """

    date = unquote(date)
    type_param = unquote(type_param)
    data = request.get_json()
    # print(city_id)
    # print(date)
    # print(type_param)
    try:
        if "num_delivered" in data:
            db_helper.update_distribution_entry(city_id, date, data["num_delivered"], type_param)
            result = {'success': True, 'response': 'Number of Distributions Updated'}
            print(data["num_delivered"])
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    print(result)
    
    return jsonify(result)


@app.route("/create/<int:city_id>/<path:date>/<int:num_delivered>/<string:type_param>", methods=['POST'])
def create(city_id, date, num_delivered, type_param):
    """ recieves post requests to add new distribution """
    print("City id is " + str(city_id), file=sys.stdout) 
    print("Date is " + date, file=sys.stdout) 
    print("Num delivered is " + str(num_delivered), file=sys.stdout) 
    print("Type is " + type_param, file=sys.stdout) 
    date = unquote(date)
    type_param = unquote(type_param)
    print("City id is " + str(city_id), file=sys.stdout) 
    print("Date is " + date, file=sys.stdout) 
    print("Num delivered is " + str(num_delivered), file=sys.stdout) 
    print("Type is " + type_param, file=sys.stdout) 
    db_helper.insert_new_distribution(city_id, date, num_delivered, type_param)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

# @app.route("/create/<int:city_id>/<path:date>/<int:num_delivered>/<path:type_param>", methods=['POST'])
# def create(city_id, date, num_delivered, type_param):
#     """ recieves post requests to add new case """
#     date = unquote(date)
#     db_helper.insert_new_distribution(city_id, date, num_delivered, type_param)
#     result = {'success': True, 'response': 'Done'}
#     return jsonify(result)

# @app.route("/create/<int:city_id>/<path:date>/<int:num_delivered>", methods=['POST'])
# def create(city_id, date, num_delivered):
#     """ recieves post requests to add new case """
#     date = unquote(date)
#     db_helper.insert_new_distribution(city_id, date, num_delivered, "testing")
#     result = {'success': True, 'response': 'Done'}
#     return jsonify(result)   

@app.route("/search/<int:city_id>/<path:date>/<string:type_param>", methods=['POST'])
def search(city_id, date, type_param):
    """ recieves post requests to search distribution """
    global city_id_global
    global date_global
    global type_global
    date = unquote(date)
    city_id_global = 2
    type_global = unquote(type_param)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/query", methods=['POST'])
def query():
    """ recieves post requests to add new distribution """
    global city_id_global
    global date_global
    city_id_global = -1
    date_global = "query"
    type_global = ''
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    global city_id_global
    global date_global
    global type_global
    # global type_global
    items = []

    if city_id_global != -1 and date_global != '':
        items = db_helper.fetch_todo(city_id_global, date_global, type_global)
    elif city_id_global == -1 and date_global == 'query':
        items = db_helper.fetch_todo(city_id_global, date_global, type_global)
    # elif city_id_global == 2:
    #     items = db_helper.fetch_todo(city_id_global, date_global, type_global)
    else:
        items = db_helper.fetch_todo(0, '', type_global)

    city_id_global = -1
    date_global = ''
    # type_global = ''

    return render_template("index.html", items=items)