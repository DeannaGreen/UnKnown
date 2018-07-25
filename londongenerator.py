from flask import Flask , render_template,request
import random
import requests
from sendemailapi import send_simple_message

#This is create instance of Flask. app is variable
app = Flask("MyApp")

Knownplaces = {
	'SouthBank': ['Southwark Bridge at Night',"Shakespeare's Globe Theatre",'Guided Tour the Globe theatre'],
	'LeicesterSquare': ["Forbidden Planet London","Golden Square", "House of MinaLima","Covent Garden Live music","Second Hand Book Shop"],
	'HydePark': ["Aplsey House","Duke of Wellington","Serpintine Gallery","Summer of sound on the roof"],
	'TowerBridge': ["Hays Galeria","Science gallery","London glassblowing"],
	'CanaryWharf': ["The Grapes","Giant Robot","Crossrail Garden"],
	'Rooftop': ["Netil 360","Queen Elizabeth Hall's rooftop","Coq d'argent","Sushi Samba"]
}

#Default route his method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
	placeslist = sorted(Knownplaces.keys())
	return render_template ("loginhomepage.html",Knownplaces=placeslist) # render_template method is a special function flask which redirect to the html file mentioned in the paramter

def random_location_generator(location_selector):
	location_chosen = 'No Match Found, please try again'
	if(location_selector in Knownplaces): 
		rand_num = random.randint(0,int(len(Knownplaces[location_selector])) - 1)
		print rand_num
		location_chosen = Knownplaces[location_selector][rand_num]
	return location_chosen

@app.route('/locgame', methods=['POST'])
def read_location_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	location_selector = form_data["loc_list"]
	print location_selector + " ALL WORKED" # from the form object getting the location input
	location_chosen= random_location_generator(location_selector) #Takes location and returns random number
	return render_template ("showlocationchosen.html",location_chosen=location_chosen)

@app.route("/signup")
def signup():
	return render_template ("signup.html") 

@app.route("/send", methods=["POST"])
def read_signup_data():
	form_data = request.form #Getting hold of a Form object that is sent from a browser.
	name =  form_data["username"] # from the form object get the Username
	emailto =  form_data["email"] # from the form object get the email
	
	emailtext = "Hello " + name + "Welcome to the (Un)Known"

	send_simple_message(emailto, emailtext)

	return render_template ("emailsent.html")

app.run(debug=True)

