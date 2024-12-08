from rdflib import Graph, Literal, RDF, Namespace
from rdflib.namespace import RDFS, OWL, XSD

# Define Namespaces
NAMESPACE = Namespace("http://example.org/tourplanner#")

# Create the RDF graph
g = Graph()

# Add Classes
classes = ["Place", "TourPackage", "Activity"]
for cls in classes:
    g.add((NAMESPACE[cls], RDF.type, OWL.Class))

# Add Object Properties
object_properties = {
    "includesPlace": ("TourPackage", "Place"),
    "hasActivity": ("Place", "Activity")
}

for prop, (domain, range_) in object_properties.items():
    g.add((NAMESPACE[prop], RDF.type, OWL.ObjectProperty))
    g.add((NAMESPACE[prop], RDFS.domain, NAMESPACE[domain]))
    g.add((NAMESPACE[prop], RDFS.range, NAMESPACE[range_]))

# Add Data Properties
data_properties = {
    "placeName": ("Place", XSD.string),
    "location": ("Place", XSD.string),
    "category": ("Place", XSD.string),
    "packageName": ("TourPackage", XSD.string),
    "price": ("TourPackage", XSD.decimal),
    "duration": ("TourPackage", XSD.integer),
    "activityName": ("Activity", XSD.string)
}

for prop, (domain, range_) in data_properties.items():
    g.add((NAMESPACE[prop], RDF.type, OWL.DatatypeProperty))
    g.add((NAMESPACE[prop], RDFS.domain, NAMESPACE[domain]))
    g.add((NAMESPACE[prop], RDFS.range, range_))

# Sample Dataset
places = [
    {"id": "SriLankaBeach", "name": "Unawatuna Beach", "location": "Southern Province", "category": "Beach"},
    {"id": "SigiriyaRock", "name": "Sigiriya Rock", "location": "Central Province", "category": "Historical"},
]

packages = [
    {"id": "HeritageTour", "name": "Heritage Tour", "price": 25000.00, "duration": 5, "places": ["SriLankaBeach", "SigiriyaRock"]},
]

activities = [
    {"id": "Snorkeling", "name": "Snorkeling", "place": "SriLankaBeach"},
    {"id": "RockClimbing", "name": "Rock Climbing", "place": "SigiriyaRock"},
]

# Add Instances to Ontology
# Places
for place in places:
    place_uri = NAMESPACE[place["id"]]
    g.add((place_uri, RDF.type, NAMESPACE.Place))
    g.add((place_uri, NAMESPACE.placeName, Literal(place["name"], datatype=XSD.string)))
    g.add((place_uri, NAMESPACE.location, Literal(place["location"], datatype=XSD.string)))
    g.add((place_uri, NAMESPACE.category, Literal(place["category"], datatype=XSD.string)))

# Tour Packages
for package in packages:
    package_uri = NAMESPACE[package["id"]]
    g.add((package_uri, RDF.type, NAMESPACE.TourPackage))
    g.add((package_uri, NAMESPACE.packageName, Literal(package["name"], datatype=XSD.string)))
    g.add((package_uri, NAMESPACE.price, Literal(package["price"], datatype=XSD.decimal)))
    g.add((package_uri, NAMESPACE.duration, Literal(package["duration"], datatype=XSD.integer)))
    for place_id in package["places"]:
        g.add((package_uri, NAMESPACE.includesPlace, NAMESPACE[place_id]))

# Activities
for activity in activities:
    activity_uri = NAMESPACE[activity["id"]]
    g.add((activity_uri, RDF.type, NAMESPACE.Activity))
    g.add((activity_uri, NAMESPACE.activityName, Literal(activity["name"], datatype=XSD.string)))
    g.add((NAMESPACE[activity["place"]], NAMESPACE.hasActivity, activity_uri))

# Save the Ontology to an OWL File
output_file = "tourplanner.owl"
with open(output_file, "wb") as f:
    f.write(g.serialize(format="xml").encode("utf-8"))  # Encode to bytes

