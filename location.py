from flask import Flask , render_template,request
import requests
import json
import flask

app = Flask("MyApp")

@app.route("/")
def home():
	return render_template ("./templates/index.html") 

@app.route("/send", methods=["POST"])
def read_form_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	startcoord =  form_data["startcoord"] # from the form object getting value of dob field.
	endcoord =  form_data["endcoord"]
	
	res = calculate_distance(startcoord, endcoord)

	return "Time to reach location: " + str(res) + " minutes"


@app.route("/towerbridge", methods=["GET"])
def readlist():
	d = [ ["Hays Galleria" ,"51.505524,-0.083599", 0,"desc1", "img1"], ["Science Gallery" , "51.502831,-0.088251",0,"desc2","img2"], ["London Glassblowing" , "51.50162,-0.082318",0,"desc2","img2"] ]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

	return render_template ("towerbridge.html" , list=d) 

def calculate_distance(startcoord, endcoord):
	print 'start' + startcoord
	print 'end' + endcoord
	apikey = '7b8dfb52ce44969caf94ca4093857d58'
	url = "https://developer.citymapper.com/api/1/traveltime/?startcoord=" + startcoord + "&endcoord=" + endcoord + "&time=2014-11-06T19%3A00%3A02-0500&time_type=arrival&key=" + apikey
	req = requests.get(url)

	print url
	data = json.loads(req.text)
	print req.text
	if 'travel_time_minutes' in data:
		return data["travel_time_minutes"]

	return -1
	
	

app.run(debug=True)
