#!/usr/bin/python3
"""simple flask app
 -will be listening on 0.0.0.0, port 5000
 -must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
    and storage.all(...)
-After each request we must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()
    
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
        
we Import this 7-dump to have some data
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def stop_session(exception=None):
    """
    To reload storage after each request
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def sorted_states():
    """
    states are listed sorted by name
    """
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
