# To call this script, use:
#  python generate-dalle-image.py <image_filename> <prompt> [optional: S/M/L]
#  The image will be in png format
#  Default size is M (512x512), but you can also add S (256x256) or L (1024x1024) as the third argument

import openai
import sys
import base64

openai.api_key_path = '.env'

if len(sys.argv) < 3:
    print("Please provide the path to the image file and the prompt as command line arguments.")
    sys.exit(1)
# get the image filename and prompt from the command line arguments. The prompt should be in quotes.
image_filename = sys.argv[1]
prompt = sys.argv[2]
sizelabel = sys.argv[3] if len(sys.argv) > 3 else "M"
if sizelabel == "S":
    size = "256x256"
elif sizelabel == "M":
    size = "512x512"
elif sizelabel == "L":
    size = "1024x1024"

# if the image filename doesn't end in .png, add .png
if not image_filename.endswith(".png"):
    image_filename = image_filename + ".png"

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size=size,
  response_format="b64_json"
)
image = response['data'][0]['b64_json']
#print(f"Image Base64 is {image}")

# write the file to the filesystem
with open(image_filename, "wb") as fh:
    fh.write(base64.decodebytes(image.encode()))

print(f"Image saved to {image_filename}")