"""Lets understand how we can make our own llm assitant in most of the ai engineering we dont trian our model or  something like that we use pre trained model and we use that model to make our own llm assistant. In this example we will use the google gemini model. why becaus its free to use not forever but we get a few request like we learned in rate limit so we will use gemini's official SDK """

"""
First step get api key 
go to "https://aistudio.google.com/api-keys" to get api key click on create api key and copy the api key and save it in your environment variable as GEMINI_API_KEY
i  will leave env.example file in the repo you can use that to set your environment variable
"""

"""
Next we need the SDK 
so go "https://googleapis.github.io/python-genai/" and follow the instruction to install the SDK

"""
"""
steps 
open your terminal use ctrl + J or cmmd + J to open the terminal and run the following command

use `pip install google-genai` if pip
use `uv pip install google-genai` if uvicorn

now install python-dotenv to load the environment variable from .env file
use `pip install python-dotenv` if pip
use `uv pip install python-dotenv` if uvicorn


create two files .env and main.py and copy the code from env.example to .env file and set your api key in the .env file 
and make sure to add .env file in your .gitignore file so that you dont push your api key to github

"""

"""Now follow the steps  you can also follow the stpes form offical documentation of google gemini sdk to make your own llm assistant

create .env add
GEMINI_API_KEY=your_api_key


"""
