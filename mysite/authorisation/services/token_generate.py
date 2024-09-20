from datetime import datetime
import hashlib

class TokenGenerator:
    @staticmethod
    def generate(email, username):
        first_chapter = hashlib.sha256(f"{email}{username}".encode()).hexdigest()
        second_chapter = hashlib.sha256(f"{datetime.now()}".encode()).hexdigest()
        token = f"{first_chapter}.{second_chapter}"
        return token
