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
with open("./res/prunedbeaverclassification.jsonl", "r") as file:
    harmful_count_0 = 0
    harmful_count_1 = 0
    harmful_count_2 = 0
    harmful_count_3 = 0
    for line in file:
        result = json.loads(line)
        if result['is_harmful'] == '0':
            harmful_count_0 += 1
        elif result['is_harmful'] == '1':
            harmful_count_1 += 1
        elif result['is_harmful'] == '2':
            harmful_count_2 += 1
        elif result['is_harmful'] == '3':
            harmful_count_3 += 1
    print(f"Amount of harmful responses with is_harmful = 0: {harmful_count_0}")
    print(f"Amount of harmful responses with is_harmful = 1: {harmful_count_1}")
    print(f"Amount of harmful responses with is_harmful = 2: {harmful_count_2}")
    print(f"Amount of harmful responses with is_harmful = 3: {harmful_count_3}")