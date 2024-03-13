from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails
import json 

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "tell me about the history of the united states"
}])
print(response["content"])