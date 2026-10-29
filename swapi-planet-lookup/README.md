# SWAPI Planet Lookup

Fetches every planet from the [Star Wars API](https://swapi.py4e.com/), lists them, and shows details for the one you pick.

- Follows the API's pagination (`next` links).
- Validates input and handles network errors and timeouts.
- Formats large numbers with thousands separators and handles `unknown` values.

```bash
pip install requests
python swapi_planets.py
```
