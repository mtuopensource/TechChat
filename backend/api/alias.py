import random

class Alias:

    def create:
        #TODO add more people and adjectives
        adjectives = ["obnoxious", "gruesome", "abhorrent", "sleazy", "stupid", "swesome", "lovely", "lonely",
                      "bored", "condescending", "dorky"]
        people = ["Newton", "Pythagoras", "Turing", "Edison", "Tesla", "Dijkstra", "Lovelace", "Jobs",
                  "Wozniak","Gates", "Gosling", "Hawking", "Einstein", "Pascal", "Schrodinger", "Mendeleev"]

        adj = adjectives[random.randint(0, len(adjectives))]
        person = people[random.randint(0, len(people))]
        rumber = str(random.randint(0, 1000))

        return  adj + person + number
