from django.shortcuts import redirect
#to check if user is logged in

def unauthenticated_user(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function
    

    #to give access to amdin if the request comes fromm the admin  otherwise the access is given to normal page for the normal user


def admin_only(view_function):
    def wrapper_function(request,*args,**kwargs):
        if request.user.is_staff:
            return view_function(request,*args,**kwargs)
        else:
            return redirect('/')
    return wrapper_function