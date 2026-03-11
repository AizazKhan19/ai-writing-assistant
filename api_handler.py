

""" 
API handler module
Handles all Groq API interactions
"""
# importing Groq class form groq library
from groq import Groq
# importing os module to read environment variables from .env file
import os
# importing load_dotenv function from dotenv library to load environment variables
from dotenv import load_dotenv
# importing get_system_prompt function from prompts module to get system prompt for Groq API
from prompts import get_system_prompt


load_dotenv() # Load environment variables from .env file


def generate_content(content_type, topic):
    """
    Generate content using Groq API

    Args:
        topic (str): The topic for which content needs to be generated
        content_type (str): The type of content to be generated (Blog Introduction, Twitter Post, Professional Email, LinkedIn Post)

    Returns:
        str: Generated content based on the provided arguments

    """

    try:
        # Initialize Groq client
        client = Groq(api_key = os.getenv("Groq_API_Key"))

        # Get the system prompt based on the content type
        system_prompt = get_system_prompt(content_type)

        # Create user message
        user_message = f"Write about : {topic}"

        # Call Groq API
        response  = client.chat.completions.create(
            model = "llama-3.3-70b-versatile",

            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature = 0.7,
            max_tokens= 500

        )


        # Extracting actual text form response
        generated_text = response.choices[0].message.content
        return generated_text
    
    except Exception as e:
        return f"Error generating content: {str(e)}"
        



