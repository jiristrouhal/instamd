This repository contains a simple script, that reads text (from a command line or a specified file), removes embedded images (if added in a markdown format) and outputs text.

The original purpose is to read a markdown text and output a text for an instagram post and tags using LLM.

# How to use it

## Setup

You need to have

- Python 3.10 or newer
- an account on OpenAI and a API key (optionally)

Install `instamd` package:

```bash
pip install git+https://github.com/jiristrouhal/instamd.git@master
```

If you want to auto-generate tags, create an environment variable `OPENAI_API_KEY` containing you OpenAI API key.

## Running the script

You can either specify path to markdown file:

```bash
instamd <path-to-md-file> [-t]
```

or the text directly in the command line (in double quotes):

```bash
instamd <text-to-process> [-t]
```

The optional `-t` flag prepends the text with auto-generated tags (from 3 to 5 tags).

The final text is printed to the console.
