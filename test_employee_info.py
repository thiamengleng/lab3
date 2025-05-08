import employee_info as db

def test_employees_above_30():
    items = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert(db.get_employees_by_age_range(30, 999) == items)

def test_employees_younger_26():
    items = [{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(db.get_employees_by_age_range(0, 26) == items)

def test_average_salary():
    assert(db.calculate_average_salary() == 361000/6)
def test_engineering():
    items = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert(db.get_employees_by_dept('Engineering') == items)

def test_sales_dept():
    items = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000},{"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}]
    assert(db.get_employees_by_dept("Sales") == items)