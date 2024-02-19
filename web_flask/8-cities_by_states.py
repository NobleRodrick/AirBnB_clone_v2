#!/usr/bin/python3
"""simple flask app
- must be listening on 0.0.0.0, port 5000
- must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
    and storage.all(...)
- To load all cities of a State:
    If your storage engine is DBStorage, you must use cities relationship
    Otherwise, use the public getter method cities
- After each request you must remove the current SQLAlchemy Session
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
- Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name>
            </B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
- Import this 7-dump to have some data
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def stop_session(exception=None):
    """
    storage is reloaded after each request
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def sorted_states_cities():
    """
    states and cities are listed, sorted by name
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
