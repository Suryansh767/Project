from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "0.0.2"
input_data = {
    "style": "",
    "topic": ""
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@sasmit/rap-song-generator/{version}"
else:
    flow_name = "@sasmit/rap-song-generator"

result = client.flow.execute(flow_name, input_data)
print(result)