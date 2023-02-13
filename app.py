from flask import Flask,jsonify

app=Flask(__name__)
@app.route("/")
def Hello():
    return"<h3>Here are my articles</>"

    
@app.route("/articles")

def get_articles():
    articles={
       "art1":{
        "id":1,
        "title":"computer programming for beginners",
        "body":"We Help People Earn MRP Money, Respect & Peace of Mind",
        "author":"zearah"
       },
         "art2":{
        "id":2,
        "title":"start your application",
        "body":"Gain the knowledge, skills, tools, and network you need to be successful & make an impact.",
        "author":"kislev"
       },

        "art3":{
        "id":3,
        "title":"how python works",
        "body":"Gain the knowledge, skills, tools, and network you need to be successful & make an impact.",
        "author":"Royal"
       }

    }
    return jsonify( articles)

if __name__=='main':
   app.run(debug=True)