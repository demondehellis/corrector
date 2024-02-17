import os
import logging
from openai import OpenAI, OpenAIError


def get_system_message():
    return os.getenv(
        'CORRECTOR_PROMPT',
        "You are a grammar tool. "
        "Fix grammar and punctuation in the user's text, maintaining markdown, line breaks, "
        "and HTML tags as is. Reply only with the corrected text."
    )


def get_model():
    return os.getenv('CORRECTOR_MODEL', 'gpt-4o-mini')


def get_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError("OpenAI API key not found in environment variables.")
    return api_key


def fix_grammar(content):
    """Use OpenAI's API to fix the provided content."""
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)
    system_message = get_system_message()
    model = get_model()

    try:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": content}
        ]
        response = client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content
    except OpenAIError as e:
        logging.error(f"OpenAI API: {e}")
        raise RuntimeError(f"OpenAI API request failed: {e}")
