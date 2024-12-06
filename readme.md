# SPARQL Queries and Expected Outputs for Sri Lanka Travel Ontology

## Query 1: Retrieve All Destinations and Their Attractions
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?destinationName ?attractionName
WHERE {
  ?destination ontology:hasAttraction ?attraction .
  ?destination ontology:hasName ?destinationName .
  ?attraction ontology:hasName ?attractionName .
}
```

### Expected Output:
| Destination Name | Attraction Name       |
|------------------|-----------------------|
| Colombo          | Galle Face Green     |
| Ella             | Nine Arches Bridge   |
| Nuwara Eliya     | Horton Plains        |
| Kandy            | Temple of the Tooth  |

## Query 2: List Tourists and Their Preferred Activities
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?touristName ?activityName
WHERE {
  ?tourist ontology:preferredActivity ?activity .
  ?tourist ontology:hasName ?touristName .
  ?activity ontology:hasName ?activityName .
}
```

### Expected Output:
| Tourist Name | Preferred Activity                 |
|--------------|------------------------------------|
| Amara        | Chariot Path                      |
| Nimal        | SPA Ceylon Ayurvedic Treatment    |

## Query 3: Get All Accommodations, Their Locations, Costs, and Ratings
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?accommodationName ?locationName ?cost ?rating
WHERE {
  ?accommodation a ontology:Accommodation .
  ?accommodation ontology:hasName ?accommodationName .
  ?accommodation ontology:locatedIn ?location .
  ?location ontology:hasName ?locationName .
  ?accommodation ontology:hasCost ?cost .
  OPTIONAL { ?accommodation ontology:hasRating ?rating . }
}
```

### Expected Output:
| Accommodation Name            | Location Name   | Cost  | Rating |
|--------------------------------|-----------------|-------|--------|
| Ella Mountain Guest House      | Ella            | 50.0  | 4.0    |
| Nuwara Eliya Tea Bungalow      | Nuwara Eliya    | 120.0 | 4.8    |
| Sophia Colombo                 | Colombo         | 100.0 | 4.2    |

## Query 4: Find Destinations Offering Specific Activities (e.g., Surfing)
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?destinationName ?activityName
WHERE {
  ?destination ontology:offersActivity ?activity .
  ?destination ontology:hasName ?destinationName .
  ?activity ontology:hasName ?activityName .
  FILTER(CONTAINS(LCASE(?activityName), "surfing"))
}
```

### Expected Output:
| Destination Name | Activity Name         |
|------------------|-----------------------|
| Ahangama         | Ahangama Surfing      |
| Mirissa          | Mirissa Surfing       |

## Query 5: List All Activities with Their Durations and Costs
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?activityName ?duration ?cost
WHERE {
  ?activity a ontology:Activity .
  ?activity ontology:hasName ?activityName .
  ?activity ontology:hasDuration ?duration .
  ?activity ontology:hasCost ?cost .
}
```

### Expected Output:
| Activity Name                      | Duration | Cost   |
|------------------------------------|----------|--------|
| Ahangama Surfing                   | 2.0      | 30.0   |
| SPA Ceylon Ayurvedic Treatment     | 1.5      | 50.0   |
| Chariot Path                       | 4.0      | 15.0   |
| Damro Tea Plantation Tour          | 3.0      | 6000.0 |

## Query 6: Get Transportation Options Provided by Accommodations
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?accommodationName ?transportationName
WHERE {
  ?accommodation ontology:providesTransportation ?transportation .
  ?accommodation ontology:hasName ?accommodationName .
  ?transportation ontology:hasName ?transportationName .
}
```

### Expected Output:
| Accommodation Name      | Transportation Name |
|--------------------------|---------------------|
| Sophia Colombo           | Pick Me             |

## Query 7: List Recommendations for Tourists Based on Their Preferred Activities
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?touristName ?destinationName
WHERE {
  ?tourist ontology:preferredActivity ?activity .
  ?destination ontology:offersActivity ?activity .
  ?tourist ontology:hasName ?touristName .
  ?destination ontology:hasName ?destinationName .
}
```

### Expected Output:
| Tourist Name | Destination Name |
|--------------|------------------|
| Amara        | Ella             |
| Nimal        | Colombo          |

## Query 8: Find All Cultural Sites and Their Locations
```sparql
PREFIX ontology: <http://www.semanticweb.org/srilanka/travel/ontology#>

SELECT ?siteName ?locationName
WHERE {
  ?site a ontology:CulturalSite .
  ?site ontology:hasName ?siteName .
  ?site ontology:locatedIn ?location .
  ?location ontology:hasName ?locationName .
}
```

### Expected Output:
| Site Name          | Location Name   |
|--------------------|-----------------|
| Galle Face Green   | Colombo         |
| Temple of the Tooth| Kandy           |
| Nine Arches Bridge | Ella            |

