# OpenAI
This repo contains a few test scripts and tools for working with (or experimenting with) the OpenAI APIs.

You're welcome to copy or use the scripts however you like, but keep in mind they were created for my fun and learning!

# Prerequisites

You'll need to have an OpenAI account and API key, saved to an `.env` file in this folder. You can get an API key at https://platform.openai.com/account/api-keys

To run the scripts, you'll need to have Python 3.7 or later installed. You'll also need to install the `openai` package. You can do this with `pip install openai` or `pip3 install openai`.

For the langchain examples, you'll also need to install `langchain`. You can do this with `pip install langchain` or `pip3 install langchain`.

For the whisper transcription example, you'll need to install `moviepy`. You can do this with `pip install moviepy` or `pip3 install moviepy`.

# Descriptions

| File(s) | Description |
| -------- | -------- |
| `transcribe-with-whisper.py` | A simple python script that takes a video or audio file and outputs a transcription. It uses the OpenAI Whisper API. |
| `generate-dalle-image.py` | A simply python script that takes a text prompt and generates an image. It uses the OpenAI (DALL-E) image creation API. |
| `answer-a-question.py` | A simple python script that takes a question and generates an answer. It uses the OpenAI gpt-3.5-turbo completions API. |
| `have-a-chat.py` | Similar to the previous example, but it builds a prompt as it goes, keeping track of previous questions. Works very much like ChatGPT. |
| `/langchain` | This folder has a few examples that use langchain to build chains for responding to questions. They all work the same way, taking a question as an argument. |