import base64
import openai
import os

openai.api_key = os.environ['OPENAI_API']


def generate_caption(image_url, prompt):
	# Create image features from the image URL

	print(image_url)
	with open(image_url, "rb") as f:
		image_data = f.read()
		encoded_data = base64.b64encode(image_data).decode('ascii')
	# Generate the caption using the image features	
	image_features = {"url": image_url}

	prompt = f"{prompt}: {image_features}"
	response = openai.Completion.create(
	 engine="text-davinci-002",
	 prompt=prompt,
	 max_tokens=50,
	 temperature=0.5,
	)

	# Extract and return the caption from the API response
	caption = response.choices[0].text.strip()
	return caption
