import json

# go through each entry in beavertails_results.json and count the amount of times is_harmful is '1'
# with open("./res/prunedbeaverselfcheck.jsonl", "r") as file:
#     harmful_count = 0
#     for line in file:
#         result = json.loads(line)
#         if result['is_harmful'] == '1':
#             harmful_count += 1
#     print(f"Amount of harmful responses: {harmful_count}")

# go through each entry in pruinedbeaverclassification.jsonl and count the amount of times is_harmful is '1', '2', and '3'
with open("./res/multiturn_results.jsonl", "r") as file:
    harmful_count = 0 
    safe_count = 0
    line_count = 1
    for line in file:
        result = json.loads(line)
        if result['gotJailbroken'] == True:
            harmful_count += 1
            print(f"Line {line_count}: Jailbroken")
        elif result['gotJailbroken'] == False:
            safe_count += 1
        line_count += 1
    print(f"Amount of harmful responses: {harmful_count}")
    print(f"Amount of safe responses: {safe_count}")
