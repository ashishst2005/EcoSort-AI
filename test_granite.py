import os

from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

api_key = os.getenv("WATSONX_APIKEY")
project_id = os.getenv("WATSONX_PROJECT_ID")
url = os.getenv("WATSONX_URL")

credentials = Credentials(
    url=url,
    api_key=api_key
)

model = ModelInference(
    model_id="ibm/granite-4-h-small",
    credentials=credentials,
    project_id=project_id
)

print("Testing Granite...")

response = model.generate_text(
    prompt="Classify vegetable peels as a waste category. Give a short answer.",
    params={
        "max_new_tokens": 100,
        "temperature": 0.2
    }
)

print("\n===== GRANITE RESPONSE =====")
print(response)