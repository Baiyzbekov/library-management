class Employee:
    def __init__(self,employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def __repr__(self):
        return f"Employee(name={self.name}, position={self.position})"
