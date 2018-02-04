import random

class Alias:

    def create:
        #TODO add more people and adjectives
        adjectives = ["Obnoxious", "Gruesome", "Abhorrent", "Sleazy", "Stupid", "Awesome", "Lovely", "Lonely",
                      "Bored", "Condescending", "Dorky", "Happy", "Brilliant", "Blunt", "Silly", "Adventurous", "Affectionate", "Ambitious",
                      "Compassionate", "Diligent", "Generous", "Impartial", "Persistent", "Philosophical", "Rational", "Sincere", "Sensible",
                      "Witty", "Cheeky", "Sleepy", "Artistic", "Aggressive", "Anxious", "Charismatic", "Devious", "Egotistic", "Upbeat"]
        people = ["Newton", "Pythagoras", "Turing", "Edison", "Tesla", "Dijkstra", "Lovelace", "Jobs",
                  "Wozniak","Gates", "Gosling", "Hawking", "Einstein", "Pascal", "Schrodinger", "Mendeleev", "Babbage", "Zuckerberg",
                  "Darwin", "Copernicus", "Farnsworth", "Bohr", "Watson", "Kepler", "Brahe", "Planck", "Mozart", "Chopin", "Beethoven",
                  "Lovecraft", "Locke", "Archimedes", "Mendel", "Hubble", "Boyle", "Washington", "Hertz", "Nobel", "Heisenberg", "Hippocrates",
                  "Fleming", "Avogadro", "Aristotle", "Sagan", "Fermi", "Ohm", "Watt"]

        adj = adjectives[random.randint(0, len(adjectives))]
        person = people[random.randint(0, len(people))]
        number = str(random.randint(0, 1000))

        return  adj + person + number
