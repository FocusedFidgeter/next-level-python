# -----------------------------------------------
# Project:      Stoic Quote Riffs
# Author:       Paul Devey
# Date:         2020-10-20
# --------------------
# Challenge: Stoic Quote -> Daily Meditation
# -----------------------------------------------
import os

import requests
from openai import OpenAI

## Set the API key and model name
# MODEL = "gpt-4o"
# client = OpenAI(
#     api_key=os.environ.get(
#         "OPENAI_API_KEY", "<your OpenAI API key if not set as an env var>"
#     )
# )

# def generate_daily_meditation(quote: str, author: str) -> str:
#     """
#     Generate a daily meditation from the OpenAI API. Use the quote as the seed.
#     Args:
#         quote (str): The quote to use as the seed.
#         author (str): The author of the quote.
#     Returns:
#         str: The daily meditation.
#     """

#     # Read the prompt template from file.
#     prompt_template = read_file("prompt_template.md")

#     # Format the template with the quote and author.
#     prompt = prompt_template.format(quote=quote, author=author)

#     # Create a chat message with the system message and the user prompt.
#     # The system message provides context to the model.
#     daily_meditation = client.chat.completions.create(
#         model=MODEL,
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are a wise philosopher that focuses on practical matters instead of esoteric navel-gazing.",
#             },
#             {"role": "user", "content": prompt},
#         ],
#     )

#     # Return the response as a string.
#     return repr(daily_meditation)


def read_file(file_path: str):
    """Read a file and return its contents as a string."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_stoic_quote() -> dict[str, str]:
    """Fetch a stoic quote from the API."""

    url = "https://stoic.tekloon.net/stoic-quote"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """Get a stoic quote and print it to the console."""

    stoic_quote: dict[str, str] = get_stoic_quote()
    quote = stoic_quote["quote"]
    author = stoic_quote["author"]

    # print(f"{quote} - {author}")

    # Read the prompt template from file.
    prompt_template = read_file("prompt_template.md")

    # Format the template with the quote and author.
    prompt = prompt_template.format(quote=quote, author=author)
    # meditation: str = generate_daily_meditation(
    #     quote=stoic_quote["quote"], author=stoic_quote["author"]
    # )
    print(prompt)


def test_read_file() -> None:
    """Test the read_file function."""

    with open("prompt_template.md", "r", encoding="utf-8") as file:
        content = file.read()
    assert content


def test_get_stoic_quote() -> None:
    """Test the get_stoic_quote function."""

    stoic_quote = get_stoic_quote()
    assert "quote" in stoic_quote
    assert "author" in stoic_quote


if __name__ == "__main__":
    # test_get_stoic_quote()
    # test_read_file()
    main()
