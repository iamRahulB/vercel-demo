import openai
import os

def generate_image(prompt,name):
	# Create image features from the image URL
	openai.api_key = os.environ['OPENAI_API']
	
	
	response = openai.Image.create(
	  prompt=prompt,
	  n=1,
	  size="1024x1024"
	)
	image_url = response['data'][0]['url']

	data = {}
	data['name'] = name
	data['prompt'] = prompt
	data["image_url"]=image_url
	with open("tmp/users/names_prompts.txt","a") as txt_file:
		txt_file.write(str(data) + '\n')
	return image_url
