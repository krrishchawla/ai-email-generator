import sys
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
import os
from llm import GPT4QAModel


def generate_email(email, instructions, reply_field):
    # Your email generation logic here
    model = GPT4QAModel()
    if reply_field:
        prompt = f"""
        You are an email writing expert. I am writing an email response. Here is the email I received: {email}. 
        I want you to follow the following instructions : {instructions}. Now write me an email for this."
        """
    else:
        prompt = f"""
        I want to compose an email. I will give you instructions to compose my email. Compose an email according to 
        the instructions. The instructions are: {instructions}.
        """
    response = model.answer_question(prompt)
    return response

def main():
    pass

if __name__ == "__main__":
    main()
