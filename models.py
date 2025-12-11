# In this simple example, we might not strictly need Pydantic models 
# if we are just using dicts from the DB and Strawberry types.
# But let's define Strawberry types here or in schema.py.
# Keeping it simple for the teaching example, let's put types in schema.py 
# or keep models if we want to show separation. 
# Let's make a simple class for non-strawberry models if needed, 
# but for now I'll just use a placeholder to show structure.

class BookModel:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author
