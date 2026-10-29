"""Demonstrate password hashing with bcrypt (registration and login).

bcrypt generates a random salt and embeds it inside the hash string, so
only one value needs to be stored per user. To verify a login attempt,
use bcrypt.checkpw(), which re-hashes the attempt with the stored salt
and compares the results in constant time.
"""

import bcrypt


def register(password: str) -> bytes:
    """Hash a password for storage (what you would save in a database)."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def login(attempt: str, stored_hash: bytes) -> bool:
    """Return True if the attempted password matches the stored hash."""
    return bcrypt.checkpw(attempt.encode("utf-8"), stored_hash)


def main():
    stored_hash = register("mypassword")
    print(f"Stored hash:    {stored_hash.decode()}")

    # The first 29 characters of a bcrypt hash hold the version, cost, and salt.
    print(f"Embedded salt:  {stored_hash[:29].decode()}")

    for attempt in ("mypassword", "wrongpassword"):
        result = "Password matches!" if login(attempt, stored_hash) else "Invalid password!"
        print(f"Login with {attempt!r}: {result}")


if __name__ == "__main__":
    main()
