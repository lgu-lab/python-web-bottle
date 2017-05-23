from bottle import template
from services import addService

'''
Controller
'''
def add(request, response):
    a = float( request.query['a'] )
    b = float( request.query['b'] )
    
    r = addService.add(a, b);
    
    # txt = 'a = {}, b = {} : result = {}'
    # txt.format(a,b,r)
    
    # context = {'title': "Max est le plus beau", 'r' : r} 
    # return context 

    # response.content_type = 'text/html; charset=latin9'
    # return txt.format(a,b,r)

    # Model : context definition
    """
    context = {
        'a' : a,
        'b' : b,
        'r' : r}
    """
    context = dict(a = a, b = b, r = r)
    
    # View : the '.tpl' file
    return template('./templates/add.tpl', context)
