#!/usr/bin/env .venv/bin/python3

import logging
import os
import sys

from dotenv import load_dotenv

from utils.cli import parse_arguments
from utils.content import process_content
from utils.files import read_file, write_file
from utils.logger import setup_logging

load_dotenv()

default_prompt = \
    "You are a grammar tool. "\
    "Fix grammar and punctuation in the user's text, maintaining markdown, line breaks, "\
    "and HTML tags as is. Reply only with the corrected text."

def main():
    setup_logging()
    args = parse_arguments()

    try:
        # Read content from a file
        content = read_file(args.input_path)

        # Exit gracefully if content is empty
        if not content.strip():
            logging.info("The content is empty. Exiting without processing.")
            sys.exit(0)

        prompt = args.prompt or os.getenv("CORRECTOR_PROMPT", default_prompt)
        fixed_content = process_content(content, args.lines, prompt)

        # Save the fixed content
        save_path = args.output or args.input_path
        write_file(save_path, fixed_content)
        logging.info(f"Fixed content saved to {save_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
