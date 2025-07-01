from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
MODEL = None


def _get_model(**kwargs):
    """
    This function returns the ChatOpenAI model object. 
    Checks if the model is already created, and if not then creates it.
    """

    global MODEL, OPENAI_API_KEY, MODEL_NAME

    assert OPENAI_API_KEY is not None, "OPENAI_API_KEY is not set"

    if not MODEL:
        model_name = kwargs.get("model_name") or MODEL_NAME
        MODEL = ChatOpenAI(temperature=1.7, model_name=model_name, openai_api_key=OPENAI_API_KEY)
    return MODEL


def get_response(input_data):
    model = _get_model()
    response = model.invoke(input_data)
    return response.content
