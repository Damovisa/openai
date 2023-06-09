# OpenAI
This repo contains a few test scripts and tools for working with (or experimenting with) the OpenAI APIs.

You're welcome to copy or use the scripts however you like, but keep in mind they were created for my fun and learning!

| File(s) | Description |
| -------- | -------- |
| `transcribe-with-whisper.py` | A simple python script that takes a video or audio file and outputs a transcription. It uses the OpenAI Whisper API. |
| `generate-dalle-image.py` | A simply python script that takes a text prompt and generates an image. It uses the OpenAI (DALL-E) image creation API. |
| `answer-a-question.py` | A simple python script that takes a question and generates an answer. It uses the OpenAI gpt-3.5-turbo completions API. |
| `have-a-chat.py` | Similar to the previous example, but it builds a prompt as it goes, keeping track of previous questions. Works very much like ChatGPT. |
| `langchain` | This folder has a few examples that use langchain to build chains for responding to questions. They all work the same way, taking a question as an argument |