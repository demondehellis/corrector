import logging
from utils.ai import fix_grammar


def parse_line_range(line_range):
    """Parse line range in the format 'start:end' and validate the positions."""
    if line_range:
        try:
            start, end = map(int, line_range.split(':'))
            if start <= 0 or end <= 0:
                raise ValueError("Line numbers must be positive integers.")
            if start > end:
                raise ValueError("Start line must be less than or equal to the end line.")
            return start, end
        except ValueError:
            raise ValueError("Selection range must be in the format 'start:end' with integers.")
    return None, None


def select_lines(content, start, end):
    """Extract lines from content based on provided start and end indices."""
    lines = content.split('\n')
    selected = '\n'.join(lines[start - 1:end])
    return selected


def adjust_formatting(original, fixed):
    """Ensure fixed content maintains the original formatting."""
    if original.startswith('\n'):
        fixed = '\n' + fixed
    if original.endswith('\n'):
        fixed += '\n'
    return fixed


def process_content(content, line_range):
    """Process content by selecting lines (if specified) and fixing grammar."""
    start, end = parse_line_range(line_range)
    selected_content = content

    if start and end:
        logging.info("Selected lines: %d to %d", start, end)
        selected_content = select_lines(content, start, end)

    logging.info("Content to fix:\n%s", selected_content)
    fixed_content = fix_grammar(selected_content)
    fixed_content = adjust_formatting(selected_content, fixed_content)
    logging.info("Fixed content:\n%s", fixed_content)

    if start and end:
        lines = content.split('\n')
        lines[start - 1:end] = fixed_content.split('\n')
        fixed_content = '\n'.join(lines)

    return fixed_content
