from langchain_openai.chat_models import ChatOpenAI

MODEL = None


def _get_model():
    global MODEL
    if not MODEL:
        MODEL = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
    return MODEL


def get_response(input_data):
    model = _get_model()
    response = model.invoke(input_data)
    return response.content
