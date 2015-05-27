from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from perform.forms import UserForm
from django.template import RequestContext
from django.contrib.auth import views

class IndexView(generic.ListView):
    template_name = 'index.html'
    def get_queryset(self):
        return render_to_response('index.html')


def manage_performance(request):
	return render_to_response('manage_performance.html')

def view_performance(request):
		return render_to_response('view_performance.html')

def employees(request):
		return render_to_response('employees.html')



def register(request):
    context = RequestContext(request)
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print (user_form.errors)

    else:
        user_form = UserForm()
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'registered': registered},
            context)




def login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/perform/')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid Username or Password entered.")

    else:
        return render_to_response('login.html', {}, context)
# Create your views here.
