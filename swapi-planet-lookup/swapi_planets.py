"""Browse Star Wars planets using the SWAPI REST API.

Fetches every planet (following the API's pagination), lists them by
number, then shows details for the one you choose.
"""

import sys

import requests

BASE_URL = "https://swapi.py4e.com/api/planets/"
TIMEOUT_SECONDS = 10


def get_planets():
    """Return a list of all planet dicts, following 'next' page links."""
    planets = []
    url = BASE_URL
    while url:
        response = requests.get(url, timeout=TIMEOUT_SECONDS)
        response.raise_for_status()
        data = response.json()
        planets.extend(data["results"])
        url = data["next"]
    return planets


def format_number(value):
    """Add thousands separators to numeric strings; pass 'unknown' through."""
    if value and value.lower() != "unknown":
        try:
            return f"{int(value):,}"
        except ValueError:
            pass
    return "unknown"


def show_planet(planet):
    print(
        f"Name: {planet.get('name')}\n"
        f"Hours per Day: {planet.get('rotation_period')}\n"
        f"Days per Year: {planet.get('orbital_period')}\n"
        f"Diameter: {format_number(planet.get('diameter'))} km\n"
        f"Gravity: {planet.get('gravity')}\n"
        f"Climate: {planet.get('climate')}\n"
        f"Terrain: {planet.get('terrain')}\n"
        f"Population: {format_number(planet.get('population'))}\n"
    )


def ask_for_choice(count):
    """Prompt until the user enters a number from 1 to count."""
    while True:
        answer = input(f"Choose a number between 1 and {count}: ")
        if answer.isdigit() and 1 <= int(answer) <= count:
            return int(answer)
        print("That wasn't a valid choice, try again.")


def main():
    try:
        planets = get_planets()
    except requests.RequestException as error:
        sys.exit(f"Could not reach the API: {error}")

    print("Here is a list of all available planets:")
    for index, planet in enumerate(planets, start=1):
        print(f"{index}. {planet['name']}")

    choice = ask_for_choice(len(planets))
    show_planet(planets[choice - 1])


if __name__ == "__main__":
    main()
