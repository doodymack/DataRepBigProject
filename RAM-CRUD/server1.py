# server1.py

# https://github.com/andrewbeattycourseware/datarepresentation/blob/main/code/Topic09x-server1linktoDB.py/server1.py

from flask import Flask, jsonify, request, abort
from rickandmortyDAO import rickandmortyDAO

app = Flask(__name__, static_url_path='', static_folder='static')

#app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/books"
@app.route('/books')
def getAll():
    #print("in getall")
    results = rickandmortyDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/books/2"
@app.route('/books/<int:id>')
def findById(id):
    foundBook = rickandmortyDAO.findByID(id)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"series\":\"hello\",\"episode\":\"someone\",\"rating\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "series": request.json['series'],
        "episode": request.json['episode'],
        "rating": request.json['rating'],
    }
    values =(book['series'],book['episode'],book['rating'])
    newId = rickandmortyDAO.create(values)
    book['id'] = newId
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"series\":\"hello\",\"episode\":\"someone\",\"rating\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBook = rickandmortyDAO.findByID(id)
    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'rating' in reqJson and type(reqJson['rating']) is not int:
        abort(400)

    if 'series' in reqJson:
        foundBook['series'] = reqJson['series']
    if 'episode' in reqJson:
        foundBook['episode'] = reqJson['episode']
    if 'rating' in reqJson:
        foundBook['rating'] = reqJson['rating']
    values = (foundBook['series'],foundBook['episode'],foundBook['rating'],foundBook['id'])
    rickandmortyDAO.update(values)
    return jsonify(foundBook)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    rickandmortyDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)


    