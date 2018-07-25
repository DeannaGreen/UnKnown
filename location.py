from flask import Flask , render_template,request
import requests
import json
import flask
from sendemailapi import send_simple_message

app = Flask("MyApp")

Knownplaces = {
	'SouthBank': ['Southwark Bridge at Night',"Shakespeare's Globe Theatre",'Guided Tour the Globe theatre'],
	'LeicesterSquare': ["Forbidden Planet London","Golden Square", "House of MinaLima","Covent Garden Live music","Second Hand Book Shop"],
	'HydePark': ["Aplsey House","Duke of Wellington","Serpintine Gallery","Summer of sound on the roof"],
	'TowerBridge': ["Hays Galeria","Science gallery","London glassblowing"],
	'CanaryWharf': ["The Grapes","Giant Robot","Crossrail Garden"],
	'Rooftop': ["Netil 360","Queen Elizabeth Hall's rooftop","Coq d'argent","Sushi Samba"]
	}

@app.route("/")
def home():
	placeslist = sorted(Knownplaces.keys())
	return render_template ("index.html",Knownplaces=placeslist)

@app.route("/loginhomepage", methods=["POST"])
def loggedin():
	placeslist = sorted(Knownplaces.keys())
	return render_template ("loginhomepage.html",Knownplaces=placeslist)

def random_location_generator(location_selector):
	location_chosen = 'No Match Found, please try again'
	if(location_selector in Knownplaces): 
		rand_num = random.randint(0,int(len(Knownplaces[location_selector])) - 1)
		print rand_num
		location_chosen = Knownplaces[location_selector][rand_num]
	return location_chosen

@app.route("/send", methods=["POST"])
def read_form_data():
	form_data = request.form 
	startcoord =  form_data["startcoord"]
	endcoord =  form_data["endcoord"]
	
	res = calculate_distance(startcoord, endcoord)

	return "Time to reach location: " + str(res) + " minutes"

@app.route("/southbank", methods=["GET"])
def readlist_southbank():
	d = [ ["Southwark Bridge at Night" ,"51.505524,-0.083599", 0,"&bull; Views of The Thames lit up at night by the bridge and monuments like the Shard<br/> &bull; Many bars and restaurants<br/> &bull; London skyline lit up<br/>", "img1"], ["Globe Theatre" , "51.502831,-0.088251",0,"&bull; See where Shakespeares plays were hosted in the 1600s<br/> &bull; Plaque on the building marking its history<br/> &bull; Anchor Terrace itself is a Grade II listed building<br/>","img2"], ["Guided Tour of Globe Theatre" , "51.502831,-0.088251",0,"&bull; Experts guide you through the history of both the Shakespearean and modern Globe theatres, the building itself and renovation<br/> &bull; Tours are in English but there are complementary sheets in French, German, Spanish, Italian, Russian, Simplified Chinese and Japanese<br/> &bull; Tours take 40 minutes<br/> &bull; Audioguide is included and is available in English, French, German, Spanish, Italian, Russian, Mandarin and Japanese. Equivalent video content is available in British Sign Language with English subtitles.<br/>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("londoneye.html" , list=d) 


@app.route("/towerbridge", methods=["GET"])
def readlist_towerbridge():
	d = [ ["Hays Galleria" ,"51.505524,-0.083599", 0,"&bull; Open air shopping and cafes</br> &bull; Old fashioned atmospheric market stalls everything from London souvenirs to with good quality jewellery and leather goods</br> &bull; Fountain in the centre - 60 foot sculpture by artist David Kemp was installed in 1987</br> &bull; View of the Thames, sky garden, and other skyscrapers including the Gherkin</br> &bull; Access to the riverbank of the Thames", "img1"], ["Science Gallery" , "51.502831,-0.088251",0,"&bull; Gallery of Exhibitions, events performances and festivals that combine technology, science, art and sound</br> &bull; Collaboration between Kings College London University of London and Science Gallery International to create a unique exhibition","img2"], ["Glassblowing" , "51.5016,0.0823",0,"&bull; One of the top glassblowing houses in Europe<br/> &bull; Exhibitions from resident artists<br/> &bull; Glass blowing demonstrations <br/> &bull; Possible to take classes taught by professionals (but very expensive and must be booked well in advance)<br/>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("towerbridge.html" , list=d) 

@app.route("/hydepark", methods=["GET"])
def readlist_hydepark():
	d = [ ["Aplsey House" ,"51.505524,-0.083599", 0,"&bull; National Trust Georgian mansion<br/> &bull; Decor has hardly changed since it was owned by the conquerer of Napoleon, the Duke of Wellington, in the Battle of Waterloo 1815<br/> &bull; History and architecture go back even further than the Duke of Wellington<br/> &bull; Gifts from Emperors and Royalty on display<br/> &bull; Art collection<br/> &bull; Multimedia guided tour<br/>", "img1"], ["Serpentine Gallery" , "51.502831,-0.088251",0,"&bull; Small art gallery<br/> &bull; Exhibits on either side of Lake Serpentine which runs through Hyde Park Kensington<br/> &bull; Constant changeover of popup exhibitions by different artists working with different mediums and styles<br/>","img2"], ["Summer of Sound On The Roof" , "51.5016,0.0823",0,"&bull; Oxford Circus John Lewis Rooftop attraction<br/> &bull; Venue for music - daytime gigs and DJ sets, street food pop ups and crazy golf throughout the summer<br/> &bull; Pop up stalls<br/> &bull; Musicians vary each day so check the schedule on the John Lewis website to see who is playing when<br/>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("hydepark.html" , list=d) 

@app.route("/canarywharf", methods=["GET"])
def readlist_canarywharf():
	d = [ ["Giant Robot" ,"51.505524,-0.083599", 0,"&bull; A seven-day-a-week food arena right on the rooftop of the Crossrail brought to you by Shoreditch very own Dinerama</br> &bull;Whether you're in the need for afterwork drinks or a crazy street feast this place has it all</br> &bull; Retro furniture and tunes to make you feel you're back at a nightclub, the vibe is alway on point</br>", "img1"], ["Crossrail Rooftop Garden" , "51.502831,-0.088251",0,"&bull; A hidden gem surrounded by skyscrappers, as the newly built Crossrail beholds this enchanted rooftop garden at the heart of Canary Wharf</br> &bull; A 300 metres enclosed garden with an abundance of exotic plants and trees, perfect for you to escape that city life right at the very heart of canary wharf</br> &bull; Get the chance to see a variety of live music and performances whilst there</br>","img2"], ["The Grapes" , "51.5016,0.0823",0,"&bull; Dating all the way back to 1583, what may appear as your average pub hides the biggest secret to it all, as this Victorian pub is owned by the one and only Sir Ian McKellan</br> &bull; The Grapes is even more unique as it appears, scarcely disguised, in the opening chapter of Charles Dicken's novel - Our Mutual Friend, who knew Limehouse well for over 40 years</br> &bull;Above it all, the Grapes provide the perfect view as you step on to their back porch and gaze along the Thames and the London skyline</br>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("canarywharf.html" , list=d) 

@app.route("/leicestersquare", methods=["GET"])
def readlist_leicestersquare():
	d = [ ["Second Hand Book Shopping" ,"51.505524,-0.083599", 0,"&bull; Charing Cross Road has 3 Second hand bookshops on one parade Any Amount of Books Henry Pordes and Quintos Bookshop based in the basement of Francis Edwards Antique and Rare books.<br/> &bull; Most books 4 and under<br/> &bull; Any Amount of Books periodically has basement sales where any book Is 1 or 5 books for 4 check their social media for basement sale announcements if interested<br/> &bull; Quintoss restocks completely each month<br/>", "img1"], ["Live Music Every Day in Covent Garden" , "51.502831,-0.088251",0,"&bull; Either opera or musicians live every day in the shopping complex between the streets and the Jubilee market one level below street level<br/> &bull; Not particularly crowded <br/> &bull; Good acoustics<br/>","img2"], ["House of MinaLima" , "51.5016,0.0823",0,"&bull; 4 floors of exhibitions of the work by the graphic designers of the Warner Brothers Harry Potter and Fantastic Beasts franchises and 1 floor gift shop<br/> &bull; See props designs artwork and photos from both Fantastic Beasts and Where to find them and the Harry Potter Franchises<br/> &bull; Gift Shop with signed merchandise and prop replicas as well as limited edition prints<br/> &bull; Miraphora MIna and Eduardo Lima the graphic designers often pop in and surprise visitors<br/>","img2"], ["Golden Square" , "51.502831,-0.088251",0,"&bull; Square gardens with lawns and shrubs<br/> &bull; Statue of George II on a plinth one of the only two public statues of George II in the capital<br/> &bull; Thought to have been laid out according to plans by Sir Christopher Wren around the year 1670s<br/>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("soho.html" , list=d) 

@app.route("/rooftops", methods=["GET"])
def readlist_rooftops():
	d = [ ["Netil 360" ,"51.505524,-0.083599", 0,"&bull; Cosy, laid back rooftop just a stone throw away from Broadway Market</br> &bull; Unlike other rooftops, Netil 360 provides a workspace with great views during the day, turning into a nightclub at dark, as it hosts live DJ sets</br> &bull; Experience a panoramic view of London</br>", "img1"], ["Coq d'Argent" , "51.502831,-0.088251",0,"&bull; Great place for afterwork drinks with a view of the Bank of England and city skyscrappers</br> &bull; A French brasserie with a heated rooftop garden serving food and cocktails whether its day or night</br>","img2"], ["Sushi Samba" , "51.5016,0.0823",0,"&bull; Experience views from the 38th floor of Heron Tower</br> &bull; Sushi samba not only provides great views but satisfies everyones craving, whether youre in the mood for Peruvian, Brazilian or even Japanese</br> &bull; Its fusion cuisine like youve never had before!</br>","img2"]]
	x = 0
	startcoord = ""
	if 'location' in request.cookies:
		startcoord = flask.request.cookies.get('location')
	

	   	print startcoord
		for i in (d):
				d[x][2] = calculate_distance(startcoord, (i[1]))
				
				x =+1

				if x==4:
					break

	return render_template ("rooftops.html" , list=d) 


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
