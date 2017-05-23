from services import helloService

'''
Controller
'''
def hello(request, response):
    # name = request.query.name # Error if no query parameter
    # name = request.query['name'] # Error if no query parameter
    name = request.query.get('name')  # NO Error if no query parameter
    
    # call the service
    r = helloService.hello(name)
    
    response.content_type = 'text/html'
    return '<body><h1>' + r + '</h1></body>'