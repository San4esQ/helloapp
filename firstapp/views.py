from django.http import HttpResponse
def products(request, productid):
    output = "<h2>Product № {0}</h2>".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>User</h2><h3>id: {0} name: {1}</h3>".format(id, name)
    return HttpResponse(output)
