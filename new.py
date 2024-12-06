from flask import Flask, jsonify, render_template
from owlready2 import get_ontology
from owlready2 import default_world

app = Flask(__name__)

# Load the ontology
onto = get_ontology("new.owl").load()
print("Ontology loaded")
print(onto)

# Helper function to extract schema:image if present
def get_image_url(instance):
    from owlready2 import default_world
    q = f"""
    SELECT ?img
    WHERE {{
        <{instance.iri}> <http://schema.org/image> ?img .
    }}
    """
    # Execute the SPARQL query
    for row in default_world.sparql(q):
        return row[0]  # Return the first image URL found
    return None

@app.route("/")
def index():
    # Home page, just links to different sections or could be a dashboard
    return render_template("index.html")

@app.route("/accommodations")
def accommodations_page():
    # Render a page that will fetch JSON data from /accommodations.json
    return render_template("accommodations.html")

@app.route("/accommodations.json")
def get_accommodations_json():
    Accommodation = onto.Accommodation
    print(Accommodation.instances())
    accommodations_data = []
    for accom in Accommodation.instances():
        name = accom.hasName[0] if accom.hasName else None
        rating = accom.hasRating[0] if accom.hasRating else None
        cost = accom.hasCost[0] if accom.hasCost else None
        image_url = get_image_url(accom)
        accommodations_data.append({
            "iri": accom.iri,
            "name": name,
            "rating": rating,
            "cost": cost,
            "image": image_url
        })
    return jsonify(accommodations_data)

@app.route("/destinations")
def destinations_page():
    return render_template("destinations.html")

@app.route("/destinations.json")
def get_destinations_json():
    Destination = onto.Destination
    destinations_data = []
    for dest in Destination.instances():
        name = dest.hasName[0] if dest.hasName else None
        dest_image = get_image_url(dest)

        attractions = []
        # hasAttraction may not always exist, so check before iterating
        if hasattr(dest, 'hasAttraction') and dest.hasAttraction:
            for attr in dest.hasAttraction:
                attr_name = attr.hasName[0] if attr.hasName else None
                attr_image = get_image_url(attr)
                attractions.append({
                    "iri": attr.iri,
                    "name": attr_name,
                    "image": attr_image
                })

        destinations_data.append({
            "iri": dest.iri,
            "name": name,
            "image": dest_image,
            "attractions": attractions
        })
    return jsonify(destinations_data)

@app.route("/tourists")
def tourists_page():
    return render_template("tourists.html")

@app.route("/tourists.json")
def get_tourists_json():
    Tourist = onto.Tourist
    tourists_data = []
    for tourist in Tourist.instances():
        t_name = tourist.hasName[0] if tourist.hasName else None
        t_image = get_image_url(tourist)

        preferred_activities = []
        if hasattr(tourist, 'preferredActivity') and tourist.preferredActivity:
            for act in tourist.preferredActivity:
                act_name = act.hasName[0] if act.hasName else None
                act_image = get_image_url(act)
                preferred_activities.append({
                    "iri": act.iri,
                    "name": act_name,
                    "image": act_image
                })

        tourists_data.append({
            "iri": tourist.iri,
            "name": t_name,
            "image": t_image,
            "preferred_activities": preferred_activities
        })
    return jsonify(tourists_data)

@app.route("/activities")
def activities_page():
    return render_template("activities.html")

@app.route("/activities.json")
def get_activities_json():
    Activity = onto.Activity
    activities_data = []
    for act in Activity.instances():
        a_name = act.hasName[0] if act.hasName else None
        duration = act.hasDuration[0] if act.hasDuration else None
        cost = act.hasCost[0] if act.hasCost else None
        a_image = get_image_url(act)
        activities_data.append({
            "iri": act.iri,
            "name": a_name,
            "duration": duration,
            "cost": cost,
            "image": a_image
        })
    return jsonify(activities_data)

if __name__ == "__main__":
    app.run(debug=True)
