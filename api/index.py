from flask import Flask, render_template, request
import os
import openai
# from image_generator import generate_image
from flask import session
# from job_result import JobSuggestionResult

app = Flask(__name__)
app.secret_key = 'ihfheiufhiweuhf7efyw8eyf8ye4y4'

openai.api_key = os.os.getenv["OPENAI_API"]


@app.route('/')
def index():
	return render_template("index.html")
	# /projects/project2/project2.html


@app.route("/projects", methods=["POST"])
def projects():
     
	name = request.form.get("name").capitalize()
	session['name'] = name

	
	if name.strip() == '':
		return render_template("index.html", name="Please Enter Your Name!")

	else:
		return render_template("projects.html", name=name)


@app.route("/project1", methods=["POST"])
def first():
	return render_template("projects/project1/first.html")


@app.route("/captions", methods=["POST"])
def project1():

	
	prompt = request.form.get("user_text")

	if not prompt:
		return 'Please enter a query'

	name = session.get('name')
# Process the image file and get the caption
	hey = generate_image(prompt,name)

	return render_template("projects/project1/result.html", name=hey)


@app.route("/project2", methods=["POST"])
def project2():
	return render_template("/projects/project2/project2.html")


@app.route("/project3", methods=["POST"])
def project3():
	return "Developement in Progress By Rahul"


@app.route("/job", methods=["POST"])
def job():
	user=request.form.get("pro2_name")
	interest=request.form.get("pro2_interest")
	resume = request.files.get('pro2_file')
	
	if resume and user.strip() and interest.strip():
		resume.save('tmp/users/resume' + resume.filename)
		resume_path = 'tmp/users/resume' + resume.filename

		suggestion=JobSuggestionResult()
		results=suggestion.job_suggestion(user,interest,resume_path )
		
		return render_template("/projects/project2/project2-final.html", name=results)
	else:
		return "Please provide all the required inputs"
