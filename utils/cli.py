from argparse import ArgumentParser


def parse_arguments():
    """Parse command-line arguments for the CLI tool."""
    parser = ArgumentParser(description="CLI Tool to fix grammar and punctuation in text files using OpenAI.")
    parser.add_argument('input_path', type=str, help="Path to the input file.")
    parser.add_argument('--lines', type=str, help="Range of lines to select in the format 'start:end'.", default=None)
    parser.add_argument('--output', type=str, help="Path to save the fixed output. Defaults to input file path.", default=None)

    return parser.parse_args()
