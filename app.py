from flask import Flask,request,render_template,redirect,url_for
from pymongo import MongoClient


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/category')
def category():
	return render_template("category.html")

@app.route('/development')
def development():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"development"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Development")


@app.route('/productivity')
def productivity():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"productivity"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Productivity")


@app.route('/personalisation')
def personalisation():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"Personalisation"})
	app = list(cursor)
	myclient.close()	
	return render_template("application.html",app=app,head="Personalisation")

@app.route('/server_n_cloud')
def server_n_cloud():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"Server and cloud"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Server and Cloud")

@app.route('/games')
def games():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"games"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Games")

@app.route('/utilities')
def utilities():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"utilities"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Utilities")

@app.route('/social')
def social():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"social"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Social")

@app.route('/news_n_weather')
def news_n_weather():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"New and Weather"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="News and Weather")

@app.route('/devices_n_iot')
def devices_n_iot():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find({"category":"Devices and IOT"})
	app = list(cursor)
	myclient.close()
	return render_template("application.html",app=app,head="Devices and IOT")

@app.route('/applications')
def applications():
	myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
	mydb = myclient["test_applications"]
	mycollections = mydb["applications"]
	cursor = mycollections.find()
	app = list(cursor)
	myclient.close()
	return render_template('application.html',app=app)	

@app.route('/search')
def search():
	getsearch = request.args.get("search")
	if getsearch=="":
		 return redirect(url_for('applications'))
	else:
		myclient = MongoClient("mongodb://guest:abc1234@ds263156.mlab.com:63156/test_applications")
		mydb = myclient["test_applications"]
		mycollections = mydb["applications"]
		if mycollections.find({'appname':{'$regex' : getsearch }}).count()>0:	
			cursor = mycollections.find({'appname':{'$regex' : getsearch }})		
			app = list(cursor)
			myclient.close()
			return render_template('application.html',app=app)
		else:
			return render_template("no-match.html")	


@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/contributor')
def contributor():
	return render_template('contributor.html')	

if __name__ == '__main__':
	app.run()