# To call this script, use:
#  python transcribe-with-whisper.py <path_to_audio_file>
# This script will transcribe the audio file and print the transcript to the console.
# If the audio file is a video file, it will be converted to mp3 format first.
# The audio file must be less than 25mb and in mp3 format.
# You must have an OpenAI API key in a .env file in the same directory as this script.

import openai
import sys
from moviepy.editor import *
import os

openai.api_key_path = '.env'

def convert_to_mp3(audio_file_path):
    video = VideoFileClip(audio_file_path)
    audio = video.audio
    audio_file_path = audio_file_path[:-4] + ".mp3"
    audio.write_audiofile(audio_file_path)

def get_file_size_in_mb(file_path):
    file_size = os.path.getsize(file_path)
    return file_size / (1024 * 1024)

if len(sys.argv) < 2:
    print("Please provide the path to the audio file as a command line argument.")
    sys.exit(1)

audio_file_path = sys.argv[1]
# if the audio file path is a video file, convert it to audio only
if audio_file_path.endswith(".mp4"):
    convert_to_mp3(audio_file_path)
    audio_file_path = audio_file_path[:-4] + ".mp3"

# if the audio file is larger than 25mb, exit
file_size = get_file_size_in_mb(audio_file_path)
if file_size > 25:
    print(f"The audio file is {file_size}mb. Please provide an audio file that is less than 25mb.")
    sys.exit(1)


# If all else is good, transcribe the audio file!
with open(audio_file_path, "rb") as audio_file:
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
