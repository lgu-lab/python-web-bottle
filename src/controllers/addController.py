from services import addService

'''
Controller
'''
def add(request, response):
    a = float( request.query['a'] )
    b = float( request.query['b'] )
    
    r = addService.add(a, b);
    
    txt = 'a = {}, b = {} : result = {}'
    txt.format(a,b,r)
    # response.content_type = 'text/html; charset=latin9'
    return txt.format(a,b,r)