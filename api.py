import requests

def api(size):
    response = requests.get(
        'http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=1&size=9')

    list = [["x" for columns in range(size)] for row in range(size)]

    for item in response.json()["squares"]:
        list[item["y"]][item["x"]] = str(item["value"])

    return list
