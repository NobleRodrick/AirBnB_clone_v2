#!/usr/bin/python3
"""simple flask app that:
- must be listening on 0.0.0.0, port 5000
- must use storage for fetching data from the storage engine 
    (FileStorage or DBStorage) => from models import storage
    and storage.all(...)
- To load all cities of a state:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
Routes:
Routes:
    /states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
            H1 tag: “State: ”
            H3 tag: “Cities:”
            UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
        Otherwise:
            H1 tag: “Not found!”
"""
from flask import Flask, render_template
from models import storage
from os import environ as env
app = Flask(__name__)


@app.teardown_appcontext
def stop_session(exception=None):
    """
    storage is reloaded after each request
    """
    storage.close()


@app.route("/states/<id>", strict_slashes=False)
@app.route("/states", strict_slashes=False)
def sorted_states_cities(id=None):
    """
    show state and cities in the case where ID is given
    otherwise list all states
    """
    states = storage.all("State")
    if id:
        state = states.get('State.{}'.format(id))
        states = [state] if state else []
    else:
        states = list(states.values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template(
        '9-states.html',
        states=states,
        len=len(states),
        id=id
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
