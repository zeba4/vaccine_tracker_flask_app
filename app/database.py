"""Defines all the functions related to the database"""

import sys
from app import db

def fetch_todo(city_id: int, date: str, type_param: str) -> dict:
    """Reads all tasks listed in the table
    Returns:
        A list of dictionaries
    """
    conn = db.connect()
    todo_list = []
    print(city_id)
    if city_id == 0 and date == '':
        query_results = conn.execute("Select * FROM Distributions LIMIT 15;").fetchall()
        # conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "type": result[2],
                "num_delivered" : result[3]
            }
            todo_list.append(item)

    elif city_id == -1 and date == 'query':
        query_results = conn.execute("Select Distinct c.city_name, del.num_delivered, d.num_deaths From Distributions del Natural Join City c Join Deaths d on d.city_id = c.city_id Where d.num_deaths > (Select avg(num_deaths) From Deaths) and d.date Like '1/1/2021' and del.date Like '1/1/2021' and type = 'Moderna' Order By d.num_deaths desc Limit 15;").fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_name": result[0],
                "num_delivered": result[1],
                "num_deaths" : result[2]
               
               
            }
            todo_list.append(item)
        print(result[2])

    else:
        query_results = conn.execute('SELECT * FROM Distributions WHERE city_id = {} AND date = "{}" AND type = "{}";'.format(city_id, date, type_param)).fetchall()
        conn.close()
        for result in query_results:
            item = {
                "city_id": result[0],
                "date": result[1],
                "type": result[2],
                "num_delivered" : result[3]
            }
            todo_list.append(item)

        # print(result[3])
        print("got here")

    return todo_list


def update_distribution_entry(city_id: int, date: str, num_delivered: int, type_param:str) -> None:
    """Updates distribution description based on given `city_id` and `date`
    Args:
        city_id (int): Targeted city_id
        date (str): Targeted date
        num_delivered (str): Updated number of delivered doses
        type_param (str) : Targeted type
    Returns:
        None
    """
    print("hi")
    conn = db.connect()
    query = 'Update Distributions set num_delivered = {} where city_id = {} and date = "{}" and type = "{}";'.format(num_delivered, city_id, date, type_param)
    conn.execute(query)
    conn.close()


def insert_new_distribution(city_id: int, date: str, num_delivered: int, type_param: str):
    """Insert new distribution to Distributions table.
    Args:
        city_id (int): city id
        date (str): month 
        num_delivered (int): number of vaccines delivered for that month
        type_param (str): type of dose
    """

    conn = db.connect()
    query = 'Insert Into Distributions (city_id, date, type, num_delivered) VALUES ({}, "{}", "{}", {});'.format(
        city_id, date, type_param, num_delivered)
    conn.execute(query)
    conn.close()



def remove_distribution(city_id: int, date: str, type_param:str) -> None:
    """ remove entries based on city ID and date """
    print(city_id)
    print(date)
    print(type_param)
    conn = db.connect()
    query = 'Delete From Distributions where city_id={} and date="{}" and type ="{}";'.format(city_id, date, type_param)
    conn.execute(query)
    conn.close()
