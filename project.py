from translate import Translator
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key="YOUR-API-KEY")

def main():
    while True:
        choice = get_choice()
        if choice:
            print(f"\nGreat! You selected {choice}.\n")
        if choice in ("1 - Chatbot", "3 - Calculator", "4 - Quiz"):
            print(openai_prompt(choice))
        elif choice == "2 - Translator":
            try:
                type = get_type()
                if type == "2 - Built-in Translator":
                    words, language = get_words_language()
                    print(f"Translation: {builtin_translator(words, language)}\n")
                elif type == "2 - OpenAI Translator":
                    print(openai_prompt(type))
            except RuntimeError:
                print("\nWord does not exist!")
        else:
            continue
        prompt = input("[Press any key to Continue | N to Exit] ").lower()
        if prompt in ("no", "n"):
            print("Thank you!\n")
            return True

def get_choice():
    try:
        choices = int(input(
            "\nSelect a number to continue OR press CTRL+C to exit\n"
            "1 for Chatbot\n"
            "2 for Translator\n"
            "3 for Calculator\n"
            "4 for Quiz Generator\n"
            "Which tool would you like to use? "
        ))
        if choices == 1:
            return "1 - Chatbot"
        elif choices == 2:
            return "2 - Translator"
        elif choices == 3:
            return "3 - Calculator"
        elif choices == 4:
            return "4 - Quiz"
        else:
            raise Exception
    except (ValueError, Exception):
        print("\nPlease Enter a Valid Value Between 1 to 4")

def get_type():
    while True:
        try:
            type = int(input("\n1 for Use Built-in \n2 for Use OpenAI \nSelect Type: "))
            if type == 1:
                return "2 - Built-in Translator"
            elif type == 2:
                return "2 - OpenAI Translator"
            else:
                raise Exception
        except (ValueError, Exception):
            print("\nINVALID INPUT!")

def openai_prompt(option):
    if option == "1 - Chatbot":
        return use_openai(input("Question: "))
    elif option == "2 - OpenAI Translator":
        words = input("\nTranslate: ")
        language = input("To [Language]: ")
        return use_openai(f"Translate {words} to {language} with format preprended with 'Translation: ' followed by the translated words only and remove original input")
    elif option == "3 - Calculator":
        math_expression = input("Calculate: ")
        return use_openai(f"Calculate the Math expression {math_expression}, showing answer only with format like 'Answer = '")
    elif option == "4 - Quiz":
        topic = input("Topic: ")
        return use_openai(
            f"Generate a one item - multiple choice quiz on {topic} with an answer formatted like 'Answer: ',"
            f"showing only the correct letter and don't include ')' in the correct answer")

def use_openai(question):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful assistant"},
            {"role": "user", "content": question}
        ]
    )
    response = completion.choices[0].message.content
    check_response = check_keyword(response)
    if check_response in ("A", "B", "C", "D"):
        print(questionnaire(response))
        result = check_answer(check_response)
        return result
    elif check_response == "Answer = ":
        return f"\n{response}\n"
    elif check_response == "Translation: ":
        return f"\n{response}\n"
    else:
        return f"\nChatbot: {response}\n"

def check_keyword(keyword):
    response = keyword.lower()
    if "answer: a" in response:
        return "A"
    elif "answer: b" in response:
        return "B"
    elif "answer: c" in response:
        return "C"
    elif "answer: d" in response:
        return "D"
    elif "answer =" in response:
        return "Answer = "
    elif "translation: " in response:
        return "Translation: "
    else:
        pass

def questionnaire(question):
    questions = question.split()
    new_question = []
    index = 0
    for i in questions:
        if i not in ("Answer:", "A", "a", "B", "b", "C", "c", "D", "d"):
            new_question.append(i)
        if i in ("A)", "A.", "a)", "a.", "B)", "B.", "b)", "b.", "C)", "C.", "c)", "c.", "D)", "D.", "d)", "d."):
            index = new_question.index(i)
            new_question.insert(index, "\n")
        final_question = ' '.join(new_question)
    return final_question

def check_answer(correct_answer):
    answer = input("[LETTER ONLY] Answer: ").upper()
    if answer == correct_answer:
        return "\nCorrect!\n"
    else:
        return f"\n{correct_answer} is the correct answer.\n"

def builtin_translator(word, language):
    if translator := Translator(to_lang=language):
        translations = translator.translate(word)
        return translations

def get_words_language():
    words = input("\nTranslate: ").lower()
    language = input("To (Language): ").lower()
    return (words, language)

if __name__ == "__main__":
    main()
