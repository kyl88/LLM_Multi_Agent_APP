from langflow.load import run_flow_from_json
TWEAKS = {
  "TextInput-nnXnX": {
      "input_value": "question"
  },
  
  "TextInput-03p3z": {
      "input_value": "profile"   
  },
  
}

result = run_flow_from_json(flow = "AskAIV2.json",input_value="message",fallback_to_env_vars=False, tweaks=TWEAKS)
