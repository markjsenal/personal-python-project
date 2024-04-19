# CTCQ System with OpenAI
#### __Video Demo:__
#### __Description:__
 This contains my final project for CS50's Introduction to Programming with Python providing users with dynamic system powered by OpenAI including Chatbot, Translator, Calculator and Quiz generator, CTCQ in short, maximazing the benefits of Generative AI to optimize productivity though there are limitations to take into consideration. Basically, a user can ask questions for any topic of interest and ChatGPT will generate a varying response, translate words or sentences from one language to another using built-in (for simple translation) or OpenAI Translator (for complex translation), and compute Mathematics expression using Calculator, and take a one-item multiple choice quiz using Quiz generator with predefined prompt design in place to control the desired output and reconstruct the same using Python codes for a better system landscape.

 DISCLAIMER: As per OpenAI's Terms of Use, under Content Section:
  * Accuracy. Artificial intelligence and machine learning are rapidly evolving fields of study. We are
  constantly working to improve our Services to make them more accurate, reliable, safe, and beneficial. Given the probabilistic nature of machine learning, use of our Services may, in some situations, result in Output that does not accurately reflect real people, places, or facts...[(Readmore)](https://openai.com/policies/terms-of-use)

 #### __Project Structure:__
  * project.py
  * test_project.py
  * requirements.txt
  * README.md

#### __Libraries:__
  * OPENAI: The OpenAI Python library provides convenient access to the OPENAI REST API form any Python 3.7+ application...[(Readmore)](https://pypi.org/project/openai/)
  * DOTENV: Python-dotenv reads reads key-value pairs from .env file and can set them as environment variables...[(Readmore)](https://pypi.org/project/python-dotenv/)
  * TRANSLATE: Translate is a powerful transalation tool written in Python with support for multiple translation providers...[(Readmore)](https://pypi.org/project/translate/)
  * RESPX: Respx is a simple, yet powerful, utility for mocking out the HTTPX, and HTTP Core libraries...[(Readmore)](https://pypi.org/project/respx/)
  * HTTPX: HTTPX is a fully featured HTTP client library for Python 3...[(Readmore)](https://pypi.org/project/httpx/)
  * DATETIME: This package provides datetime data type...[(Readmore)](https://pypi.org/project/DateTime/)

#### __How to install Libraries__
 These libraries can be installed by executing below command (list of libraries can be found on requirements.txt file):
 `pip install -r requirements.txt`

 #### __How to Setup OpenAI__
  1. Create an OpenAI account and generate API Key
  2. Create a Python Virtual Environment using venv
  3. Create a .env file and configure key-value pair API Key from step 1
  4. `load_dotenv` reads the key-value pair from .env
  5. `Client = OpenAI()` gets the api key value

#### __Usage and Functions__
 Run `python project.py` in CLI terminal to begin

__`main()`__ The main function will handle all events from other functions such as printing the results from any of the tools used. It has a while loop condition to allow continuous interaction between the user and system and be able to exit the program with particular exit input or using CTRL+C command.

__`get_choice()`__ This will prompt user to input any option between 1 to 4 according to the tools to be used. If input value is invalid, user will be prompted again.

__`get_type()`__ This will prompt user to select between built-in Python Translator or OpenAI Translator. If input value is not within the specified options, user will be prompted whether to continue and select a tool again or exit the program.

__`openai_prompt()`__ This gets called when user selected an option in any of 1, 2, 3 or 4. If the selected option is 1, user will be prompted to provide a question of any topic. If 2 is selected, user will be prompted to provide the words or phrases to translate. Prompt is pre-designed to return a pre-designed output such as formatting like `'Translation: '` If 3 is selected, user will be prompted to provide any Mathematical expression to calculate the value. Prompt is pre-designed to return a desired output such as formatting like `'Answer ='` for keyword checking. If 4 is selected, user will be prompted to select a topic of interest which will be the basis for generating a one-item, multiple choice quiz. Prompt is pre-designed to return a desired result such as formatting like `'Answer: '` followed by the correct letter of the answer. All of which will call `use_openai()` and return the result to `main()` function.

__`use_openai()`__ Following the selection of option between 1, 3 or 4. This will send the actual request to OpenAI API endpoint and handles the questions passed from `get_question()`, then calls `check_keyword` function to check for keyword as per the prompt design and return back the result accordingly. Setup includes system and user role, wherein system is represented by ChatGPT with predefined content, and user as the user with content from `get_question()`.

__`check_keyword()`__ This checks for keyword from the response. If it contains the formatted keyword `'answer: a' or 'answer: b' or 'answer: c' or 'answer: d'`, it will return the answer key such as `"A" or "B" or "C" or "D"` for Quiz Generator tool. If keyword format is `'answer = '`, it will return `'Answer = '` for Calculator. Otherwise, if now keyword is found, then the original response will be returned.

__`questionnaire()`__ This is specifically for Quiz generator. Once keyword is checked and comfirmed existing, this function will handle the transformation of the response or question structure to show only the multiple choice question whilst hiding the correct answer from the user.

__`check_answer()`__ The question is printed  without the correct answer and user will be prompted to input their intelligent guess on what the answer could possibly be. If user input matches the correct answer, this will return a message that user input is correct. If user input does not match, the correct answer will printed instead.

__`builtin_translator()`__ This function handles the translation of user input when user opted for a built-in translator over OpenAI translator, calling the `get_words_language()` function via the `main()`.

__`get_words_language()`__ Handles the prompting for user input on what words or phrase to translate and which language they will be translated to.

__Intensive Unit Test with Pytest and Respx can be found on test_project.py file__