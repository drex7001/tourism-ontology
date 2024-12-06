from owlready2 import *
from flask import Flask, jsonify, request

# Load your ontology
onto = get_ontology("new.owl").load()

app = Flask(__name__)

# Example: Get all destinations and their attractions
@app.route("/destinations", methods=["GET"])
def get_destinations():
    destinations = []
    for dest in onto.Destination.instances():
        attractions = [attraction.hasName[0] for attraction in dest.hasAttraction]
        destinations.append({
            "name": dest.hasName[0],
            "attractions": attractions
        })
    return jsonify(destinations)

# Example: Get tourists and their preferred activities
@app.route("/tourists", methods=["GET"])
def get_tourists():
    tourists = []
    for tourist in onto.Tourist.instances():
        activity = tourist.preferredActivity[0].hasName[0] if tourist.preferredActivity else "None"
        tourists.append({
            "name": tourist.hasName[0],
            "preferredActivity": activity
        })
    return jsonify(tourists)

if __name__ == "__main__":
    app.run(debug=True)
