import json

# go through each entry in beavertails_results.json and count the amount of times is_harmful is '1'
with open("./res/beavertails_results.json", "r") as file:
    harmful_count = 0
    for line in file:
        result = json.loads(line)
        if result['is_harmful'] == '1':
            harmful_count += 1
    print(f"Amount of harmful responses: {harmful_count}")
    