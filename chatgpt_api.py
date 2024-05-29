from openai import OpenAI
from dotenv import load_dotenv
import os

#Copy the openAI API Key in a file named .env on your project root folder, in same folder where this Python file resides

#.env file follows a simple key=value format where you can provide all project configurations 

#e.g. I have my .env file locally stored which has 

#OPENAI_API_KEY = "sk-**** redacted for security ***************"

#In your setup the .env file you have should have your API key.


load_dotenv() # Load all the config variables set as key=value pairs in .env file locally stored

API_KEY = os.getenv('OPENAI_API_KEY') # Get the value of the variable OPENAI_API_KEY stored in .env file

MODEL_NAME="gpt-3.5-turbo" # Specify the openAI model you want to use 

#It could be the latest gpt-4o  , OpenAIs latest model GPT-4 omni
#or gpt-4-turbo or gpt-3.5-turbo



#Create the openAI client object

client = OpenAI(

    # This is the default and can be omitted

    api_key=API_KEY,

)



# # Invoke the  gpt-3.5 turbo model, Pass the text query to it  and get its response back

response = client.chat.completions.create(

    messages=[

        {"role": "system", "content": 'You are an expert in Machine learning, Data science.'}, 

        {

            "role": "user",

            "content": "You are an expert in Machine learning, Data science. Give me a study map for learning data science , courses and websites to learn from ",

        }

    ],

    model=MODEL_NAME,

)



#Print the data from the model response 

if response.choices:

    print(response.choices[0].message.content)

else:

    print("No choices received.")

