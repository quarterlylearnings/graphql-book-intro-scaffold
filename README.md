# GraphQL Book App

Welcome to the GraphQL Book App challenge! Follow these steps to build a fully functional GraphQL API from scratch.

## Level 0: Setup & Exploration

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the App**:
    ```bash
    uvicorn main:app --reload --port 8000
    ```
3.  **Verify**: Open [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql). You should see the GraphiQL interface. The schema will be empty or very basic for now.

---

## Level 1: The Schema (Types)

**Goal**: Define the shape of your data.

1.  Open `schema.py`.
2.  Uncomment/Define the `Author` type:
    - Fields: `name` (str).
3.  Complete the `Book` type:
    - It already has `id` and `title`.
    - Add a resolver for `author` that returns an `Author` object.
    - *Hint*: You'll need `author_name` (str) to look it up, but strictly speaking for the type, we want to expose an `Author` object.

---

## Level 2: Reading Data (Queries)

**Goal**: Fetch data from the "database".

1.  In `schema.py`, look at the `Query` class.
2.  Implement `books`:
    - Use `db.get_books()` from `data.py`.
    - Convert the dictionary results into `Book` objects.
3.  **Test**: Open GraphiQL and run:
    ```graphql
    query {
      books {
        title
        author {
          name
        }
      }
    }
    ```

---

## Level 3: Writing Data (Mutations)

**Goal**: Add new books to the system.

1.  In `schema.py`, look at the `Mutation` class.
2.  Add a method `add_book`:
    - Arguments: `title` (str), `author` (str).
    - Return type: `Book`.
    - Implement: Call `db.add_book(...)` and return the new `Book`.
3.  **Test**:
    ```graphql
    mutation {
      addBook(title: "New Book", author: "New Author") {
        id
        title
      }
    }
    ```

---

## Level 4: Real-time Updates (Subscriptions)

**Goal**: Notify clients when a book is added.

1.  Update `add_book` mutation to be `async` (needed for the next step).
2.  Define a `Subscription` class in `schema.py`.
3.  Add `book_added` method:
    - Decorator: `@strawberry.subscription`.
    - Implementation: Iterate over `db.book_events()` (which is an async generator).
    - Yield: `Book` objects.
4.  Add `subscription=Subscription` to `strawberry.Schema(...)` at the bottom.
5.  **Test**: Open two tabs. Run the subscription in one, and the mutation in the other.

---

## Level 5: Optimization (Caching)

**Goal**: Handle "expensive" fields efficiently.

1.  Add a `biography` field to the `Author` type.
2.  This field should resolve using `await db.get_author_bio(self.name)`.
3.  **Observe**: `db.get_author_bio` has an artificial delay (2 seconds).
4.  **Test**: Run a query requesting `biography`. Notice the delay on the first run, and the speed on the second run (the `db` class handles caching internally).

---

## Challenge Complete!

You have built a full-featured GraphQL API with Types, Resolvers, Mutations, Subscriptions, and Caching!
