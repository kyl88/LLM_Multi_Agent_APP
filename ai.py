from textwrap import indent
from langflow.load import run_flow_from_json
# .env
from dotenv import load_dotenv
import requests
from typing import Optional
import os

load_dotenv()

BASE_API_URL = "https://api.aiv2.dev/v1/ask"
LANGFLOW_ID = "AskAIV2"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN") 

def ask_aiv2(question, profile):
 TWEAKS = {
   "TextInput-nnXnX": {
      "input_value": question
  },
  
  "TextInput-03p3z": {
      "input_value":dict_to_string(profile)  
  },
  
}

result = run_flow_from_json(flow = "AskAIV2.json",input_value="message",fallback_to_env_vars=False, tweaks=TWEAKS)

   
def get_macros(goals, profile):
 TWEAKS = {
   "TextInput-nnXnX": {
      "input_value": ",".join(goals) 
  },
  
   "TextInput-03p3z": {
       "input_value": dict_to_string(profile) 
    },
  }
 
 return run_flow_from_json("", tweaks=TWEAKS)
 
def run_flow_from_json(message : str,
                       output_type: str = "chat",
                       input_type: str = "chat",
                       tweaks: Optional[dict] = None,
                       application_token: Optional[str] = None)-> dict:
                       api_url = f"{BASE_API_URL}/{output_type}"
                      
                       payload = {
                          "input_value": message,
                          "output_type": output_type,
                          "input_type": input_type,  

                       }
                       headers = None

                       if tweaks:
                           payload["tweaks"] = tweaks

                       if application_token:
                           headers = {"Authorization": f"Bearer {application_token}"}
                       
                       response = requests.request("POST", api_url, headers=headers, data=payload)
                       return response.json() 
result = get_macros("name: Kyle, age: 37","weight: 71kg, 1.72cm","muscle gain")
print(result)