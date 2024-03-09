from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails

config = RailsConfig.from_path("config.yml")
rails = LLMRails(config)

response = rails.generate(messages=[{
    "role": "user",
    "content": "Hello!"
}])
print(response["content"])