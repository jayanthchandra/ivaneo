from flask import Flask,render_template ,current_app,jsonify,url_for,redirect
import subprocess,bookrec,requests,json,webbrowser


app=Flask(__name__,static_url_path="")

@app.route('/')
def index():
	a=json.dumps('meta-data')
	webbrowser.open_new('http://172.168.2.88:5555/books')
	


@app.route('/books')
def getbooks():
	data=bookrec.recomend("Vishruth Nair")
	books=[]
	for i in data:
		books.append(i[1]+ ' book')
	print(books)
	req="http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="
	images=[]
	for i in books:
		urlify=req + i
		resp=requests.get(urlify)
		a=resp.json()
		images.append( a['responseData']['results'][0]['unescapedUrl'])

	return render_template('index.html',**locals())




if __name__ =='__main__' :
	app.run(host="172.168.2.88",port=5555)

