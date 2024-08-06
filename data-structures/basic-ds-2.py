import json
import yaml

# Define complex nested data structures
nested_data_examples = [
    # Example 1
    {
        "name": "Alice",
        "age": 30,
        "hobbies": ["reading", "hiking", "coding"],
        "contact": {
            "email": "alice@example.com",
            "phones": {"home": "555-5555", "mobile": "555-5556"}
        }
    },
    # Example 2
    (
        {"type": "Fruit", "items": {"apples": 10, "bananas": 5}},
        {"type": "Vegetable", "items": {"carrots": 7, "broccoli": 3}}
    ),
    # Example 3
    [
        {"cities": {"New York": "NY", "Los Angeles": "CA", "Chicago": "IL"}},
        {"states": {"California": "CA", "Texas": "TX", "Florida": "FL"}}
    ],
    # Example 4
    {
        "sets_example": {"fruits": {"apple", "banana"}, "colors": {"red", "blue"}},
        "tuple_example": (1, 2, (3, 4, {"key": "value"}))
    },
    # Example 5
    [
        {
            "id": 101,
            "grades": {"math": "A", "science": "B"},
            "schedule": [{"day": "Monday", "subject": "Math"}, {"day": "Tuesday", "subject": "Science"}]
        },
        {
            "id": 102,
            "grades": {"math": "B", "science": "A"},
            "schedule": [{"day": "Wednesday", "subject": "Math"}, {"day": "Thursday", "subject": "Science"}]
        }
    ],
    # Example 6
    {
        "employees": [
            {"name": "John", "role": "Manager", "team": {"members": 5, "location": "HQ"}},
            {"name": "Jane", "role": "Developer", "languages": ["Python", "JavaScript"]}
        ],
        "departments": {"IT": 20, "HR": 10}
    },
    # Example 7
    [
        {
            "title": "Book Title",
            "author": ("First Name", "Last Name"),
            "details": {"ISBN": "123-456-789", "published": 2020}
        },
        {
            "title": "Another Book",
            "author": ("Different", "Author"),
            "details": {"ISBN": "987-654-321", "published": 2018}
        }
    ],
    # Example 8
    {
        "coords": [
            {"x": 1, "y": 2, "z": 3},
            {"x": 4, "y": 5, "z": 6}
        ],
        "data": {"type": "PointCloud", "size": 1000}
    },
    # Example 9
    {
        "weather": {"temperature": 72, "humidity": 55, "conditions": "Sunny"},
        "forecast": [
            {"day": "Monday", "high": 75, "low": 60},
            {"day": "Tuesday", "high": 78, "low": 62}
        ]
    },
    # Example 10
    {
        "family": {
            "parents": ("Mother", "Father"),
            "children": [{"name": "Child1", "age": 10}, {"name": "Child2", "age": 7}]
        },
        "pets": {"dog": "Rover", "cat": "Whiskers"}
    },
    # More examples can be added similarly...
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
    print(loaded_json_data)

# Read data structures from YAML file
with open('nested_data.yaml', 'r') as yaml_file:
    loaded_yaml_data = yaml.safe_load(yaml_file)
    print("\nLoaded YAML Data:")
    print(loaded_yaml_data)
