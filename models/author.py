class Author:
    def __init__(self,name: str, birth_year: int = None, nationality: str = None ):
        self.name = name
        self.birth_year = birth_year
        self.nationality = nationality
    
    def __repr__(self):
        return f"Author(name={self.name})"
        
