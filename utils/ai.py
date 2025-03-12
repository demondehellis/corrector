import os
import logging
from openai import OpenAI, OpenAIError


def get_model():
    return os.getenv('CORRECTOR_MODEL', 'gpt-4o-mini')


def get_api_key():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError("OpenAI API key not found in environment variables.")
    return api_key


def apply_prompt(content, prompt):
    """Apply the prompt to the content using the OpenAI API."""
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)
    model = get_model()

    try:
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": content}
        ]
        response = client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content
    except OpenAIError as e:
        logging.error(f"OpenAI API: {e}")
        raise RuntimeError(f"OpenAI API request failed: {e}")
