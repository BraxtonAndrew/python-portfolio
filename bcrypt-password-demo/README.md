# bcrypt Password Demo

Shows the register and login flow for password storage:

- `register()` hashes a password with a random salt via `bcrypt.hashpw`.
- `login()` verifies an attempt with `bcrypt.checkpw`, which is constant-time.
- The demo prints the hash and the salt embedded in its first 29 characters.

```bash
pip install bcrypt
python password_hashing.py
```
