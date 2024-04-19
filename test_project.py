import httpx
import pytest
from respx import MockRouter
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage
from openai.types.chat.chat_completion import ChatCompletion, Choice
from datetime import datetime
from dotenv import load_dotenv
from project import get_choice, check_keyword, builtin_translator, use_openai, questionnaire

load_dotenv
client = OpenAI(api_key="YOUR-API-KEY")

def test_get_choice():
    assert get_choice() == None

@pytest.mark.respx()
def test_use_openai(respx_mock: MockRouter) -> None:
    # setup mock response
    completion = ChatCompletion(
        id="bar",
        model="gpt-3.5-turbo",
        object="chat.completion",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                message=ChatCompletionMessage(
                    content="Nice meeting you!",
                    role="assistant",
                ),
            )
        ],
        created=int(datetime.now().timestamp()),
    )
    respx_mock.post("/v1/chat/completions").mock(
        return_value=httpx.Response(200, json=completion.model_dump(mode="python"))
    )

    # send mocked request
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "assistant", "content": "Respond with 'Nice meeting you!'"}
        ]
    )
    assert completion.choices[0].message.content == "Nice meeting you!"

def test_use_openai_chatbot():
    assert use_openai("Respond only with 'Hello World!'") == "\nChatbot: Hello World!\n"

def test_use_openai_calculator():
    assert use_openai("Calculate 500*500 showing answer only with format like 'Answer = ' without new line") == "\nAnswer = 250000\n"

def test_questionnaire():
    assert questionnaire("Question: What is the value of 2 + 2? \n\nA) 3 \nB) 4 \nC) 5 \nD) 6 \n\nAnswer: B") == "Question: What is the value of 2 + 2? \n A) 3 \n B) 4 \n C) 5 \n D) 6"

def test_check_keyword():
    assert check_keyword("Capital of Paris? A) Paris B) Canberra C) New York D) Madrid Answer: A") == "A"
    assert check_keyword("Capital of Paris? A) Canberra B) Paris C) New York D) Madrid Answer: B") == "B"
    assert check_keyword("Capital of Paris? A) New York B) Canberra C) Paris D) Madrid Answer: C") == "C"
    assert check_keyword("Capital of Paris? A) Madrid B) Canberra C) New York D) Paris Answer: D") == "D"

def test_builtin_translator():
    assert builtin_translator("Handsome", "Filipino") == "makisig" or "gwapo"
    assert builtin_translator("How are you doing?", "French") == "Comment tu vas ?"
    assert builtin_translator("Always give your best shot, because you only live once.", "Latin") == "omni tempore comitem"
    assert builtin_translator("What is life?", "Arabic") == "-ما هي الحياة؟"

def test_builtin_translator_error():
    with pytest.raises(RuntimeError):
        assert (builtin_translator("Meric", "English")) == "Word does not exist!"
