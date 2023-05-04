
GRADES = ['Kindergarten'] + list(str(i) for i in range(1, 13))
NUM_GRADES = len(GRADES)
NUM_FAMILIES = 100
NUM_STUDENTS = NUM_GRADES * 20
STUDENTS_PER_GRADE = NUM_STUDENTS // NUM_GRADES
GENDERS = ['M', 'F']
NUM_TRANSACTIONS = 50_000

ITEMS = [
    {"name": "Pencil", "item_type": "Stationery", "price": 0.5},
    {"name": "Notebook", "item_type": "Stationery", "price": 2.0},
    {"name": "Eraser", "item_type": "Stationery", "price": 0.25},
    {"name": "Textbook", "item_type": "Book", "price": 10.0},
    {"name": "Lunch", "item_type": "Food", "price": 3.5},
    {"name": "Ruler", "item_type": "Stationery", "price": 1.0},
    {"name": "Calculator", "item_type": "Electronics", "price": 15.0},
    {"name": "Crayons", "item_type": "Art Supplies", "price": 3.0},
    {"name": "Backpack", "item_type": "Accessories", "price": 25.0},
    {"name": "Water Bottle", "item_type": "Accessories", "price": 8.0},
    {"name": "Colored Pencils", "item_type": "Art Supplies", "price": 4.0},
    {"name": "Markers", "item_type": "Art Supplies", "price": 5.0},
    {"name": "Scissors", "item_type": "Stationery", "price": 2.5},
    {"name": "Glue Stick", "item_type": "Stationery", "price": 1.5},
    {"name": "Binder", "item_type": "Stationery", "price": 4.0},
    {"name": "Highlighter", "item_type": "Stationery", "price": 0.75},
    {"name": "Lunchbox", "item_type": "Accessories", "price": 15.0},
    {"name": "Pencil Case", "item_type": "Accessories", "price": 6.0},
    {"name": "Graph Paper", "item_type": "Stationery", "price": 3.0},
    {"name": "Loose-Leaf Paper", "item_type": "Stationery", "price": 2.5},
    {"name": "Index Cards", "item_type": "Stationery", "price": 1.0},
    {"name": "USB Flash Drive", "item_type": "Electronics", "price": 10.0},
    {"name": "Stapler", "item_type": "Stationery", "price": 5.0},
    {"name": "Paper Clips", "item_type": "Stationery", "price": 1.5},
    {"name": "Pen", "item_type": "Stationery", "price": 0.75},
    {"name": "Folder", "item_type": "Stationery", "price": 1.5},
    {"name": "Protractor", "item_type": "Stationery", "price": 2.0},
    {"name": "Compass", "item_type": "Stationery", "price": 3.0},
    {"name": "Lined Journal", "item_type": "Stationery", "price": 7.0},
    {"name": "Sketchbook", "item_type": "Art Supplies", "price": 8.0},
]
