from typing import List, Optional, Dict
import random

class Database:
    def __init__(self):
        self.books: Dict[int, dict] = {
            1: {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
            2: {"id": 2, "title": "1984", "author": "George Orwell"},
        }
        self.authors: Dict[str, dict] = {
            "F. Scott Fitzgerald": {"id": 1, "name": "F. Scott Fitzgerald"},
            "George Orwell": {"id": 2, "name": "George Orwell"},
        }
        self._book_id_counter = 3

    def get_books(self) -> List[dict]:
        return list(self.books.values())

    def get_book_by_id(self, book_id: int) -> Optional[dict]:
        return self.books.get(book_id)

    def add_book(self, title: str, author: str) -> dict:
        new_id = self._book_id_counter
        self._book_id_counter += 1
        book = {"id": new_id, "title": title, "author": author}
        self.books[new_id] = book
        
        # Simple author handling
        if author not in self.authors:
            self.authors[author] = {"id": len(self.authors) + 1, "name": author}
            
        return book

    def update_book(self, book_id: int, title: str = None, author: str = None) -> Optional[dict]:
        if book_id not in self.books:
            return None
        
        if title:
            self.books[book_id]["title"] = title
        if author:
            self.books[book_id]["author"] = author
            if author not in self.authors:
                self.authors[author] = {"id": len(self.authors) + 1, "name": author}
                
        return self.books[book_id]

    def delete_book(self, book_id: int) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False

# Global database instance
import asyncio

class request_latency:
    """Context manager to simulate latency."""
    def __init__(self, seconds=2):
        self.seconds = seconds
    
    async def __aenter__(self):
        await asyncio.sleep(self.seconds)
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass

class Database:
    def __init__(self):
        self.books: Dict[int, dict] = {
            1: {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
            2: {"id": 2, "title": "1984", "author": "George Orwell"},
        }
        self.authors: Dict[str, dict] = {
            "F. Scott Fitzgerald": {"id": 1, "name": "F. Scott Fitzgerald"},
            "George Orwell": {"id": 2, "name": "George Orwell"},
        }
        self._book_id_counter = 3
        # Simple PubSub: List of queues
        self._subscribers: List[asyncio.Queue] = []
        # Simple manual cache for expensive operations
        self._bio_cache: Dict[str, str] = {}

    def get_books(self) -> List[dict]:
        return list(self.books.values())

    def get_book_by_id(self, book_id: int) -> Optional[dict]:
        return self.books.get(book_id)

    async def add_book(self, title: str, author: str) -> dict:
        new_id = self._book_id_counter
        self._book_id_counter += 1
        book = {"id": new_id, "title": title, "author": author}
        self.books[new_id] = book
        
        # Simple author handling
        if author not in self.authors:
            self.authors[author] = {"id": len(self.authors) + 1, "name": author}
        
        # Notify subscribers
        for queue in self._subscribers:
            await queue.put(book)
            
        return book

    def update_book(self, book_id: int, title: str = None, author: str = None) -> Optional[dict]:
        if book_id not in self.books:
            return None
        
        if title:
            self.books[book_id]["title"] = title
        if author:
            self.books[book_id]["author"] = author
            if author not in self.authors:
                self.authors[author] = {"id": len(self.authors) + 1, "name": author}
                
        return self.books[book_id]

    def delete_book(self, book_id: int) -> bool:
        if book_id in self.books:
            del self.books[book_id]
            return True
        return False
        
    async def book_events(self):
        """Yields book data as it arrives."""
        queue = asyncio.Queue()
        self._subscribers.append(queue)
        try:
            while True:
                book_data = await queue.get()
                yield book_data
        finally:
            self._subscribers.remove(queue)

    async def get_author_bio(self, author_name: str) -> str:
        """Simulates an expensive API call to get an author's bio."""
        if author_name in self._bio_cache:
            print(f"Cache HIT for {author_name}")
            return self._bio_cache[author_name]
        
        print(f"Cache MISS for {author_name} (fetching...)")
        # Simulate network delay
        async with request_latency(2):
            # Sleep is handled in __aenter__, so we don't strictly need another sleep here 
            # unless we want double delay. The class impl sleeps.
            pass
            
        bio = f"This is the biography of {author_name}. It was fetched from a remote source."
        self._bio_cache[author_name] = bio
        return bio

# Global database instance
db = Database()
