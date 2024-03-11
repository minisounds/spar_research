from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails

config = RailsConfig.from_path("./config")
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "Hello!"
}])
print(response["content"])

# next steps - cycle thru dataset and generate responses, then have moderator api rate the responses