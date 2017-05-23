from bottle import Bottle, request, response, static_file
from controllers import helloController, addController

app = Bottle()

'''
Standard behavior (index page, error pages, etc)
'''
@app.route('/')
def index():
    # return '<h1>Welcome on my Home Page</h1>'
    return static_file('index.html', root="static")

@app.error(404)
def error404(error):
    return 'Nothing here, sorry (Error 404)'

'''
Controllers 
'''
@app.route('/hello')
def hello():
    return helloController.hello(request, response)

@app.route('/add')
def add():
    return addController.add(request, response)

'''
Start the server
'''
if __name__ == '__main__':
    app.run(port=1234, debug=True)
