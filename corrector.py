#!/usr/bin/env .venv/bin/python3

import logging
import sys

from dotenv import load_dotenv

from utils.cli import parse_arguments
from utils.content import process_content
from utils.files import read_file, write_file
from utils.logger import setup_logging

load_dotenv()


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

        fixed_content = process_content(content, args.lines)

        # Save the fixed content
        save_path = args.output or args.input_path
        write_file(save_path, fixed_content)
        logging.info(f"Fixed content saved to {save_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
