# External Tool for Grammar and Punctuation Correction

## Overview

This simple script is designed for use as an **external tool** in JetBrains IDEs like **IntelliJ IDEA**, **PhpStorm**, and **PyCharm**, enabling quick text corrections on **selected lines** directly from the context menu or through keyboard shortcuts.

![corrector-demo](https://github.com/user-attachments/assets/8a50b8d4-e9c9-4562-bb00-66bf81d2091c)

## Features

- **Correction of selected lines**: Select lines in your IDE and run the tool to correct grammar and punctuation.  
- **Configurable settings**: Adjust the model and prompt via environment variables or shell configuration files.

## Requirements

- Python 3.7+
- OpenAI Python library
- dotenv for optional environment configuration

## Installation

1. Clone the repository:

```bash
git clone git@github.com:demondehellis/corrector.git
cd corrector
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Configure environment variables:

You can set environment variables in your `.bashrc`, `.zshrc`, or any shell configuration file. Optionally, you can also create a `.env` file with the following variables:

```dotenv
OPENAI_API_KEY=your-api-key
CORRECTOR_MODEL=gpt-4o-mini  # Optional, default model is gpt-4o-mini
```

## Basic Usage

To correct grammar and punctuation in an entire file:

```bash
python corrector.py input.txt
```

To save the corrected content to a specific file:

```bash
python corrector.py input.txt --output output.txt
```

To correct specific lines from the input file (e.g., lines 1 to 5) and save the result:

```bash
python corrector.py input.txt --lines 1:5 --output output.txt
```

## Using as an External Tool in JetBrains IDEs

To use this script as an external tool, follow these steps:

1. Open your IDE and navigate to `Preferences` > `Tools` > `External Tools`.
2. Click the `+` button to add a new tool.
3. Fill in the following details:
   - **Name**: Grammar Corrector
   - **Program**: Path to your Python executable (e.g., `/opt/homebrew/bin/python3.11`).
   - **Arguments**: `/path/to/corrector.py $FilePath$ --lines $SelectionStartLine$:$SelectionEndLine$`
   - **Working Directory**: `$ProjectFileDir$`
   - Enable `Synchronize files after execution`.
   - (Optional) Check `Open console for tool output` to view the output or any errors.
4. Click `OK` to save the configuration.

<img width="1118" alt="Screenshot 2024-09-27 at 02 18 17" src="https://github.com/user-attachments/assets/7035c86a-9e33-4f22-bcd1-3fbffb59a609">

### Tips for Quick Access

- **Keyboard Shortcuts**: Assign a custom keyboard shortcut to the external tool for instant access. Go to `Preferences` > `Keymap`, search for your external tool, and set your desired shortcut.
- **Add to Menus or Toolbars**: For even quicker access, add the external tool to your IDE’s menu or toolbar by right-clicking on the menu or toolbar and selecting `Customize Menus and Toolbars`.

## License

This project is licensed under the MIT License.
