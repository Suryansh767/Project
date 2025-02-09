from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "YOUR_API_KEY"})

version = "1.0.0"
input_data = {"key": "value"}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"author/your-flow-name/{version}"
else:
    flow_name = "author/your-flow-name"

result = client.flow.execute(flow_name, input_data)
print(result)
from mira_sdk import MiraClient, Flow

# Get a flow
flow = client.flow.get("author/flow_name")

# Get flows by author
flows = client.flow.get_by_author("author")

# Get flows by tag
flows = client.flow.get_by_tag("tag")

# Search for flow
flows = client.flow.search("abcd")
curl --request POST \
  --url https://console-bff.stg.arohalabs.dev/v1/flows/flows/{author}/{flow_name} \
  --header 'MiraAuthorization: YOUR_API_KEY' \
  --data '{
    "input_param": "value"
}'
{
  "result": "LLM output"
}
