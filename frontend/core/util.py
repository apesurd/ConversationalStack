from langchain_openai.chat_models import ChatOpenAI

# import from dotenv

from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
MODEL = None


def _get_model(**kwargs):

    global MODEL, OPENAI_API_KEY, MODEL_NAME

    assert OPENAI_API_KEY is not None, "OPENAI_API_KEY is not set"

    model_name = kwargs.get("model_name") or MODEL_NAME
    if not MODEL:
        MODEL = ChatOpenAI(temperature=1.7, model_name="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)
    return MODEL


def get_response(input_data):
    model = _get_model()
    response = model.invoke(input_data)
    return response.content
