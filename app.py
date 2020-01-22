from flask import Flask, render_template


app = Flask(__name__)




@app.route("/getmsg/",methods = ['GET'])
def respond():
	url = request.args.get("url",None)

	response = {}

	if not url:
		response["error"] = "No name found please try again"
	else:
		
		r = requests.get(url)

		xx = re.compile('[\d]*[:]*[\d]+[:][\d]+')

		a3 = r.text
		a4 = re.findall(xx,a3)


		min_ = 0 
		sec_ = 0

		for i in a4:
			
			if(len(i) > 5):
				min_ += int(i.split(":")[0]) * 60 + int(i.split(":")[1]) 
				sec_ += (int(i.split(":")[2]))
			elif(len(i)<=5):
				min_ += int(i.split(":")[0])
				sec_ += (int(i.split(":")[1]))

		ssec = int(sec_/60)
		msec = sec_%60

		min_ = min_ + ssec 

		abshr = int(min_/60)
		mhr = min_%60

		fstring = ""+abshr+"hours "+mhr+" minutes"+msec+"seconds"
		print(min_+ ssec, "minutes and ",msec,"seconds")
		print(abshr,"hours ",mhr," minutes",msec,"seconds")


		response["message"] = fstring
		return jsonify(response)	
	



@app.route("/respond/",methods = ['POST'])			
def posting():
	urlstring = request.form.get('url')
	print(urlstring)
	
	if(fstring):
		return jsonify({
			"Message": "url received is : " + urlstring,
			"Method" : "post"

			})
	else:
		return jsonify({
			"error":"wassup with that url"
			})	



@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__': app.run(debug=True)