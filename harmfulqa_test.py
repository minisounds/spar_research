from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails
import json 

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

# nemoguardrails response function
def generate_response(human_query):
  response = rails.generate(messages=[{
      "role": "user",
      "content": human_query
  }])
  return response["content"]

# Load your dataset
with open("./data/HarmfulQA_data.json", "r") as f:
    dataset = json.load(f)

# Function to process each turn in the conversation
def process_conversation(conversation):
  # Skip "from: 'gpt'" parts
  print(conversation)
  for i in range(len(conversation)):
    if conversation[i]["from"] == "human":
      # Generate response with NemoGuardrails
      response = generate_response(conversation[i]["value"])
      # Moderate response with OpenAI moderation API
      #is_safe = moderate_response(response)
      # Do something with the response (print, store, etc.)
      print(f"Human: {conversation[i]['value']}")
      print(f"GPT: {response}")
      #print(f"GPT: {response} (Safe: {is_safe})")

# Loop through each conversation in the dataset

for i in range(len(dataset)):
    for convo in dataset[i]["blue_conversations"]:
        process_conversation(dataset[0]["blue_conversations"][convo])
    for convo in dataset[i]["red_conversations"]:
        process_conversation(dataset[0]["red_conversations"][convo])
  


# OpenAI moderation API function
def moderate_response(text):
  # Replace this with your OpenAI moderation API call
  # This is a placeholder and won't work without your specific implementation
  is_safe = True  # Assuming success for simplicity
  return is_safe