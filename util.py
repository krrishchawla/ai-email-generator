import sys
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
import os
from llm import GPT4QAModel

style = """
        Here is my style of writing emails:

        Example 1:
        Hi Ria,

        I'm Shubh - I'm a third-year CS and Math student at Stanford working on decoding EMG signals. I've been interested recently in what all we can decode from EMG -- if it's solely motor movement, or other thoughts as well. I saw the work you're doing in the field and was really interested. 

        Would love to chat about this and hear your perspective, whether on Zoom or if you're free to grab coffee at some point on campus?

        Thanks so much,
        Shubh


        Example 2:
        Hi Simran,

        Would it be possible to hop on a ~15 minute Zoom call tomorrow to discuss logistics for CS 229S? 

        Thanks so much,
        Shubh


        Example 3:
        Hey Yousef, 

        Sorry for not responding sooner! Hadil--great to meet you! Congrats on getting into Stanford! As Yousef has probably told you, get ready for such a fun and transformative experience :) 

        Happy to chat and give advice -- feel free to shoot me a text on WhatsApp, my # is 646-617-3631.

        Take care,
        Shubh
    """


def generate_email(email, instructions, reply_field):
    # Your email generation logic here
    model = GPT4QAModel()
    if reply_field:
        prompt = f"""
        You are an email writing expert. I am writing an email response. Here is the email I received: {email}. 
        I want you to follow the following instructions and format properly with proper indentation. The instructions are: {instructions}. 
        {style}
        Now write me an email for this.
        """
    else:
        prompt = f"""
        I want to compose an email. I will give you instructions to compose my email. Compose an email according to 
        the instructions and format properly with proper indentation. The instructions are: {instructions}.
        {style}
        """
    response = model.answer_question(prompt)
    return response

def main():
    pass

if __name__ == "__main__":
    main()
