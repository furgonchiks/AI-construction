import json
def task() -> float:
    filename = "input.json"
    with open(filename) as f:
        inf = json.load(f)
    summ = sum([item["score"] * item["weight"] for item in inf])
    return round(summ, 3)
print(task())
