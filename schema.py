import strawberry
from typing import List, Optional
from data import db

# TODO: Define the Author type
# @strawberry.type
# class Author:
#     ...

# TODO: Define the Book type
@strawberry.type
class Book:
    id: strawberry.ID
    title: str
    author: str 
    # TODO: Add author object resolver

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        # TODO: Implement fetching all books
        return []

    # TODO: Add book(id) query

@strawberry.type
class Mutation:
    # TODO: Add add_book mutation
    @strawberry.mutation
    def _placeholder(self) -> str:
        return "Implement mutations here"

# TODO: Add Subscription type
# @strawberry.type
# class Subscription:
#    ...

schema = strawberry.Schema(query=Query, mutation=Mutation)
