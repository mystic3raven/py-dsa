import json
import yaml

# Define complex nested data structures
nested_data_examples = [
    # Example 1
    {
        "name": "Alice",
        "details": {
            "age": 30,
            "hobbies": ["reading", "hiking", "coding"],
            "contact": {
                "email": "alice@example.com",
                "phones": {"home": "555-5555", "mobile": "555-5556"}
            }
        },
        "projects": [{"name": "Project1", "status": "completed"}, {"name": "Project2", "status": "ongoing"}]
    },
    # Example 2
    (
        {"type": "Fruit", "items": {"apples": 10, "bananas": 5, "citrus": {"oranges": 7, "lemons": 3}}},
        {"type": "Vegetable", "items": {"carrots": 7, "broccoli": 3, "greens": {"spinach": 4, "lettuce": 5}}}
    ),
    # Example 3
    [
        {"cities": {"New York": "NY", "Los Angeles": "CA", "Chicago": "IL"}},
        {"states": {"California": "CA", "Texas": "TX", "Florida": "FL"}},
        {"countries": {"USA": ["New York", "California"], "Canada": ["Ontario", "Quebec"]}}
    ],
    # Example 4
    {
        "sets_example": {
            "fruits": {"apple", "banana", "cherry"},
            "colors": {"red", "blue", "green"},
            "combinations": [("red", "apple"), ("blue", "banana")]
        },
        "tuple_example": (1, 2, (3, 4, {"key": "value"})),
        "data_matrix": [[1, 2], [3, 4], [5, 6]]
    },
    # Example 5
    [
        {
            "id": 101,
            "grades": {"math": "A", "science": "B", "history": "C"},
            "schedule": [
                {"day": "Monday", "subjects": ["Math", "History"]},
                {"day": "Tuesday", "subjects": ["Science", "Math"]},
                {"day": "Wednesday", "subjects": ["History", "PE"]}
            ]
        },
        {
            "id": 102,
            "grades": {"math": "B", "science": "A", "history": "B"},
            "schedule": [
                {"day": "Thursday", "subjects": ["Math", "Art"]},
                {"day": "Friday", "subjects": ["Science", "Music"]},
                {"day": "Monday", "subjects": ["History", "Science"]}
            ]
        }
    ],
    # Example 6
    {
        "employees": [
            {"name": "John", "role": "Manager", "team": {"members": 5, "location": "HQ"}},
            {"name": "Jane", "role": "Developer", "languages": ["Python", "JavaScript"]},
            {"name": "Doe", "role": "Analyst", "tools": {"spreadsheets": "Excel", "databases": ["SQL", "NoSQL"]}}
        ],
        "departments": {"IT": 20, "HR": 10, "Finance": 15},
        "locations": {"HQ": "New York", "Branch": ["California", "Texas"]}
    },
    # Example 7
    [
        {
            "title": "Book Title",
            "author": ("First Name", "Last Name"),
            "details": {"ISBN": "123-456-789", "published": 2020, "genres": ["Fiction", "Mystery"]}
        },
        {
            "title": "Another Book",
            "author": ("Different", "Author"),
            "details": {"ISBN": "987-654-321", "published": 2018, "genres": ["Non-Fiction", "Biography"]}
        },
        {
            "title": "Third Book",
            "author": ("Third", "Author"),
            "details": {"ISBN": "111-222-333", "published": 2022, "genres": ["Science Fiction", "Adventure"]}
        }
    ],
    # Example 8
    {
        "coords": [
            {"x": 1, "y": 2, "z": 3},
            {"x": 4, "y": 5, "z": 6},
            {"x": 7, "y": 8, "z": 9}
        ],
        "data": {"type": "PointCloud", "size": 1000, "dimensions": 3},
        "metadata": {"source": "Sensor", "accuracy": 0.98}
    },
    # Example 9
    {
        "weather": {
            "temperature": 72,
            "humidity": 55,
            "conditions": "Sunny",
            "forecast": [
                {"day": "Monday", "high": 75, "low": 60},
                {"day": "Tuesday", "high": 78, "low": 62},
                {"day": "Wednesday", "high": 80, "low": 65}
            ]
        },
        "location": {"city": "Springfield", "state": "Illinois", "country": "USA"}
    },
    # Example 10
    {
        "family": {
            "parents": ("Mother", "Father"),
            "children": [
                {"name": "Child1", "age": 10, "hobbies": ["soccer", "chess"]},
                {"name": "Child2", "age": 7, "hobbies": ["drawing", "cycling"]}
            ]
        },
        "pets": {"dog": "Rover", "cat": "Whiskers"},
        "house": {"rooms": ["kitchen", "living room", "bedroom"], "address": "123 Main St"}
    },
    # Example 11
    {
        "university": {
            "name": "XYZ University",
            "departments": {
                "Engineering": {"students": 500, "faculties": ["Mechanical", "Electrical", "Civil"]},
                "Arts": {"students": 300, "faculties": ["History", "Literature", "Philosophy"]},
                "Science": {"students": 400, "faculties": ["Physics", "Chemistry", "Biology"]}
            }
        }
    },
    # Example 12
    [
        {
            "sports_team": "Team A",
            "players": [{"name": "Player1", "position": "Forward"}, {"name": "Player2", "position": "Goalkeeper"}],
            "coach": "Coach A",
            "home_city": "City A"
        },
        {
            "sports_team": "Team B",
            "players": [{"name": "Player3", "position": "Midfielder"}, {"name": "Player4", "position": "Defender"}],
            "coach": "Coach B",
            "home_city": "City B"
        }
    ],
    # Example 13
    {
        "gaming": {
            "genres": ["RPG", "FPS", "Strategy"],
            "titles": {
                "RPG": ["Game1", "Game2"],
                "FPS": ["Game3", "Game4"],
                "Strategy": ["Game5", "Game6"]
            },
            "platforms": {"PC": 4, "Console": 3, "Mobile": 2}
        }
    },
    # Example 14
    {
        "science": {
            "experiments": [
                {"name": "Experiment1", "field": "Physics", "duration": "2 weeks"},
                {"name": "Experiment2", "field": "Chemistry", "duration": "3 weeks"}
            ],
            "equipment": ["microscope", "test tubes", "beaker"],
            "lab_location": "Building B"
        }
    },
    # Example 15
    [
        {
            "concert": {
                "performer": "Band A",
                "venue": "Stadium A",
                "date": "2022-09-01",
                "tickets": {"available": 100, "sold": 50}
            }
        },
        {
            "concert": {
                "performer": "Band B",
                "venue": "Arena B",
                "date": "2022-10-15",
                "tickets": {"available": 200, "sold": 150}
            }
        }
    ],
    # Example 16
    {
        "transport": {
            "vehicles": {
                "cars": {"sedan": 5, "SUV": 10},
                "bikes": {"mountain": 7, "road": 4}
            },
            "routes": [
                {"origin": "City A", "destination": "City B", "distance": 100},
                {"origin": "City C", "destination": "City D", "distance": 200}
            ],
            "tickets": {"bus": 50, "train": 30}
        }
    },
    # Example 17
    {
        "movies": [
            {
                "title": "Movie A",
                "genre": "Action",
                "cast": [{"actor": "Actor1", "role": "Hero"}, {"actor": "Actor2", "role": "Villain"}],
                "release_year": 2020
            },
            {
                "title": "Movie B",
                "genre": "Drama",
                "cast": [{"actor": "Actor3", "role": "Protagonist"}, {"actor": "Actor4", "role": "Antagonist"}],
                "release_year": 2019
            }
        ]
    },
    # Example 18
    {
        "library": {
            "sections": {
                "Fiction": ["Book1", "Book2"],
                "Non-Fiction": ["Book3", "Book4"],
                "Science": ["Book5", "Book6"]
            },
            "staff": ["Librarian1", "Assistant1", "Assistant2"],
            "location": "Downtown"
        }
    },
    # Example 19
    {
        "technology": {
            "companies": [
                {"name": "Tech A", "employees": 1000, "products": ["Product1", "Product2"]},
                {"name": "Tech B", "employees": 500, "products": ["Product3", "Product4"]}
            ],
            "startups": [
                {"name": "Startup A", "founded": 2018, "funding": "Series A"},
                {"name": "Startup B", "founded": 2020, "funding": "Seed"}
            ]
        }
    },
    # Example 20
    {
        "restaurants": [
            {
                "name": "Restaurant A",
                "cuisine": "Italian",
                "menu": {"pasta": 12, "pizza": 15},
                "location": "City Center"
            },
            {
                "name": "Restaurant B",
                "cuisine": "Mexican",
                "menu": {"tacos": 10, "burritos": 8},
                "location": "Old Town"
            }
        ]
    },
    # Example 21
    {
        "education": {
            "schools": [
                {"name": "School A", "students": 500, "programs": ["Arts", "Sciences"]},
                {"name": "School B", "students": 300, "programs": ["Technology", "Business"]}
            ],
            "universities": [
                {"name": "University A", "students": 1000, "courses": ["Engineering", "Medicine"]},
                {"name": "University B", "students": 2000, "courses": ["Law", "Arts"]}
            ]
        }
    },
    # Example 22
    {
        "nature": {
            "national_parks": [
                {"name": "Park A", "location": "Region A", "size": "500 acres"},
                {"name": "Park B", "location": "Region B", "size": "800 acres"}
            ],
            "wildlife": ["bears", "deer", "eagles"]
        }
    },
    # Example 23
    {
        "real_estate": {
            "properties": [
                {"type": "house", "price": 300000, "location": "Suburb A"},
                {"type": "apartment", "price": 200000, "location": "City B"}
            ],
            "agents": [{"name": "Agent A", "sales": 50}, {"name": "Agent B", "sales": 75}]
        }
    },
    # Example 24
    {
        "music": {
            "bands": [
                {"name": "Band A", "albums": ["Album1", "Album2"]},
                {"name": "Band B", "albums": ["Album3", "Album4"]}
            ],
            "solo_artists": [
                {"name": "Artist A", "hits": ["Hit1", "Hit2"]},
                {"name": "Artist B", "hits": ["Hit3", "Hit4"]}
            ]
        }
    },
    # Example 25
    {
        "finance": {
            "accounts": [
                {"type": "savings", "balance": 1000, "transactions": [{"amount": 100, "type": "deposit"}]},
                {"type": "checking", "balance": 500, "transactions": [{"amount": 50, "type": "withdrawal"}]}
            ],
            "investments": [
                {"type": "stocks", "portfolio": {"AAPL": 50, "GOOGL": 30}},
                {"type": "bonds", "portfolio": {"US Treasury": 1000, "Corporate": 500}}
            ]
        }
    },
    # Example 26
    {
        "adventures": {
            "travel": [
                {"destination": "Country A", "activities": ["hiking", "sightseeing"], "duration": "2 weeks"},
                {"destination": "Country B", "activities": ["skiing", "shopping"], "duration": "1 week"}
            ],
            "local_trips": [
                {"destination": "City A", "activities": ["museum", "park"], "duration": "3 days"},
                {"destination": "City B", "activities": ["beach", "restaurant"], "duration": "2 days"}
            ]
        }
    },
    # Example 27
    {
        "pets": {
            "dogs": [
                {"name": "Fido", "breed": "Labrador", "age": 3},
                {"name": "Buddy", "breed": "Golden Retriever", "age": 5}
            ],
            "cats": [
                {"name": "Whiskers", "breed": "Siamese", "age": 2},
                {"name": "Mittens", "breed": "Persian", "age": 4}
            ]
        }
    },
    # Example 28
    {
        "fashion": {
            "brands": [
                {"name": "Brand A", "products": ["jeans", "t-shirts"]},
                {"name": "Brand B", "products": ["shoes", "jackets"]}
            ],
            "trends": [
                {"year": 2020, "style": "casual"},
                {"year": 2021, "style": "formal"}
            ]
        }
    },
    # Example 29
    {
        "food": {
            "recipes": [
                {"name": "Pasta", "ingredients": ["noodles", "sauce"], "time": "30 minutes"},
                {"name": "Salad", "ingredients": ["lettuce", "tomatoes"], "time": "15 minutes"}
            ],
            "chefs": [
                {"name": "Chef A", "specialty": "Italian"},
                {"name": "Chef B", "specialty": "French"}
            ]
        }
    },
    # Example 30
    {
        "history": {
            "events": [
                {"name": "Event A", "year": 2000, "location": "City A"},
                {"name": "Event B", "year": 1999, "location": "City B"}
            ],
            "figures": [
                {"name": "Figure A", "contribution": "Science"},
                {"name": "Figure B", "contribution": "Arts"}
            ]
        }
    },
    # Example 31
    {
        "art": {
            "styles": ["impressionism", "cubism", "realism"],
            "galleries": [
                {"name": "Gallery A", "location": "City A"},
                {"name": "Gallery B", "location": "City B"}
            ],
            "artists": [
                {"name": "Artist A", "movement": "Modern"},
                {"name": "Artist B", "movement": "Renaissance"}
            ]
        }
    },
    # Example 32
    {
        "health": {
            "doctors": [
                {"name": "Doctor A", "specialty": "Cardiology", "patients": 50},
                {"name": "Doctor B", "specialty": "Pediatrics", "patients": 30}
            ],
            "hospitals": [
                {"name": "Hospital A", "location": "City A"},
                {"name": "Hospital B", "location": "City B"}
            ]
        }
    },
    # Example 33
    {
        "fitness": {
            "gyms": [
                {"name": "Gym A", "memberships": 200},
                {"name": "Gym B", "memberships": 150}
            ],
            "programs": [
                {"name": "Program A", "duration": "1 month"},
                {"name": "Program B", "duration": "3 months"}
            ]
        }
    },
    # Example 34
    {
        "languages": {
            "spoken": ["English", "Spanish", "French"],
            "programming": ["Python", "Java", "C++"],
            "ancient": ["Latin", "Greek"]
        }
    },
    # Example 35
    {
        "space": {
            "planets": [
                {"name": "Earth", "type": "Terrestrial", "moons": 1},
                {"name": "Jupiter", "type": "Gas Giant", "moons": 79}
            ],
            "missions": [
                {"name": "Mission A", "year": 2020},
                {"name": "Mission B", "year": 2021}
            ]
        }
    },
    # Example 36
    {
        "architecture": {
            "styles": ["Gothic", "Modern", "Classical"],
            "buildings": [
                {"name": "Building A", "height": 100, "style": "Modern"},
                {"name": "Building B", "height": 200, "style": "Classical"}
            ]
        }
    },
    # Example 37
    {
        "media": {
            "films": [
                {"title": "Film A", "genre": "Action"},
                {"title": "Film B", "genre": "Drama"}
            ],
            "tv_shows": [
                {"title": "Show A", "season": 1},
                {"title": "Show B", "season": 2}
            ]
        }
    },
    # Example 38
    {
        "technology": {
            "devices": [
                {"type": "Laptop", "brands": ["Brand A", "Brand B"]},
                {"type": "Smartphone", "brands": ["Brand C", "Brand D"]}
            ],
            "software": [
                {"name": "Software A", "type": "OS"},
                {"name": "Software B", "type": "Application"}
            ]
        }
    },
    # Example 39
    {
        "business": {
            "companies": [
                {"name": "Company A", "industry": "Tech"},
                {"name": "Company B", "industry": "Finance"}
            ],
            "markets": ["US", "EU", "APAC"]
        }
    },
    # Example 40
    {
        "politics": {
            "parties": ["Party A", "Party B", "Party C"],
            "elections": [
                {"year": 2020, "winner": "Party A"},
                {"year": 2016, "winner": "Party B"}
            ]
        }
    },
    # Example 41
    {
        "science": {
            "fields": ["Physics", "Chemistry", "Biology"],
            "discoveries": [
                {"name": "Discovery A", "field": "Physics"},
                {"name": "Discovery B", "field": "Chemistry"}
            ]
        }
    },
    # Example 42
    {
        "travel": {
            "destinations": [
                {"country": "Country A", "attractions": ["Attraction A", "Attraction B"]},
                {"country": "Country B", "attractions": ["Attraction C", "Attraction D"]}
            ],
            "agencies": [
                {"name": "Agency A", "packages": ["Package A", "Package B"]},
                {"name": "Agency B", "packages": ["Package C", "Package D"]}
            ]
        }
    },
    # Example 43
    {
        "environment": {
            "issues": ["Climate Change", "Pollution", "Deforestation"],
            "organizations": [
                {"name": "Organization A", "focus": "Climate Change"},
                {"name": "Organization B", "focus": "Pollution"}
            ]
        }
    },
    # Example 44
    {
        "sports": {
            "teams": [
                {"name": "Team A", "players": ["Player A", "Player B"]},
                {"name": "Team B", "players": ["Player C", "Player D"]}
            ],
            "leagues": [
                {"name": "League A", "country": "Country A"},
                {"name": "League B", "country": "Country B"}
            ]
        }
    },
    # Example 45
    {
        "law": {
            "cases": [
                {"name": "Case A", "year": 2020},
                {"name": "Case B", "year": 2019}
            ],
            "lawyers": [
                {"name": "Lawyer A", "specialty": "Criminal"},
                {"name": "Lawyer B", "specialty": "Civil"}
            ]
        }
    },
    # Example 46
    {
        "history": {
            "periods": ["Renaissance", "Industrial", "Modern"],
            "events": [
                {"name": "Event A", "year": 1800},
                {"name": "Event B", "year": 1900}
            ]
        }
    },
    # Example 47
    {
        "religion": {
            "beliefs": ["Belief A", "Belief B", "Belief C"],
            "practices": [
                {"name": "Practice A", "region": "Region A"},
                {"name": "Practice B", "region": "Region B"}
            ]
        }
    },
    # Example 48
    {
        "geography": {
            "continents": ["Africa", "Asia", "Europe"],
            "countries": [
                {"name": "Country A", "capital": "Capital A"},
                {"name": "Country B", "capital": "Capital B"}
            ]
        }
    },
    # Example 49
    {
        "economy": {
            "industries": ["Manufacturing", "Service", "Agriculture"],
            "companies": [
                {"name": "Company A", "sector": "Manufacturing"},
                {"name": "Company B", "sector": "Service"}
            ]
        }
    },
    # Example 50
    {
        "security": {
            "issues": ["Cybersecurity", "Data Protection", "National Security"],
            "organizations": [
                {"name": "Organization A", "focus": "Cybersecurity"},
                {"name": "Organization B", "focus": "National Security"}
            ]
        }
    }
]

# Write data structures to JSON file
with open('nested_data.json', 'w') as json_file:
    json.dump(nested_data_examples, json_file, indent=2, default=str)

# Write data structures to YAML file
with open('nested_data.yaml', 'w') as yaml_file:
    yaml.dump(nested_data_examples, yaml_file, default_flow_style=False)

# Read data structures from JSON file
with open('nested_data.json', 'r') as json_file:
    loaded_json_data = json.load(json_file)
    print("Loaded JSON Data:")
    for i, example in enumerate(loaded_json_data):
        print(f"Example {i + 1}:", example)

# Read data structures from YAML file
with open('nested_data.yaml', 'r') as yaml_file:
    loaded_yaml_data = yaml.safe_load(yaml_file)
    print("\nLoaded YAML Data:")
    for i, example in enumerate(loaded_yaml_data):
        print(f"Example {i + 1}:", example)
