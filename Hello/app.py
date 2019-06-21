import sys
import requests

# print (sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get(
    "https://www.youtube.com/watch?v=-nh9rCzPJ20&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=112&t=0s"
)
print(r.status_code)
print(greet("word"))
print(greet("Corey"))
