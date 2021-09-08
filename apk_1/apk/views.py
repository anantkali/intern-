from . serializers import LoginSerializer , RegisterSerializer # Serializers are imported 
from .models import Login , Register # Models are imported 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import io
import hashlib

@api_view(['POST']) # Specifying the type of requests to be accepted 
@csrf_exempt # CSRF token by-pass
def login_api(request):
    # Type of request validation
    if request.method == 'POST':
        # JSON data is  recieved fron the request (POST)
        json_data = request.body
        # Data is streamed
        stream = io.BytesIO(json_data)  
        # Data is converted into Pythondata 
        pythondata = JSONParser().parse(stream)
        # Password is hashed for hash comparison
        paswd = hashlib.sha256(pythondata['pass_1'].encode()).hexdigest()
        # Validation of credentials
        if Login.objects.get(Email = pythondata['email']).id == Login.objects.get(pass_1=paswd).id :
            # Response message to be shown  is converted intp JSON response
            json_data = JSONRenderer().render({'Success' : 'Login Success'})
            # Returning a response 
            return HttpResponse(json_data, content_type='application/json')
        # If credentials are not found
        else :
            # Response to be shown
            response = {"Invalid" : 'Invalid credentials'}
            # Conversion to JSON response
            json_data = JSONRenderer().render(response)
            # Returning the response 
            return HttpResponse(json_data,content_type='application/json')
    # If request in GET
    else:
        return HttpResponse("You are using login API")




@api_view(['POST'])  # Specifying the type of requests to be accepted 
@csrf_exempt # CSRF token by-pass
def registration_api(request):
    # Type of request validation
    if request.method == 'POST':
        # JSON data is  recieved fron the request (POST)
        json_data = request.body  
        # JSON data is streamed
        stream = io.BytesIO(json_data)   
        # JSON data is converted into python data (Dictionary)
        python_data = JSONParser().parse(stream) 
        # Validation for the existing User
        if Register.objects.get(email=python_data['email']) is not None: 
            # Converting the response to JSON
            json_data = JSONRenderer().render({'Member' : 'This email is already registered ...'})  
            #  Returning a message on the basis of Validation
            return HttpResponse(json_data, content_type = 'application/json')
        # If User is not existing 
        else : 
            # Replacing the value of password with hashed password [ Password is hashed in SHA-256 ] 
            python_data['pass_1'] = hashlib.ha256(python_data['pass_1'].encodde()).hexdigest()
            # Python_data is passed to Serializer class stored in serializers.py
            serializer = RegisterSerializer(data=python_data) 
            # Data validation before it is stored into Model
            if serializer.is_valid():
                # Data is saved in the Registration serializer 
                serializer.save()
                # Data is to be stored in Login Model
                Log_data = {'email' : python_data['email'],'pass_1' : python_data['pass_1'] }
                # Data is passed to LoginSerializerclass stored in serializers.py
                Log_serializer = LoginSerializer(data=Log_data)
                # Data validation and converting to complex data type 
                if Log_serializer.is_valid():
                    # Login data is now saving to the Model
                    Log_serializer.save()
                    # Response to be shown after Registration 
                    res = {'msg':'Registered successfully'}
                    # Response in converted into JSON
                    json_data = JSONRenderer().render(res)
                    # Returning a response
                    return HttpResponse(json_data, content_type = 'application/json')
            # If data is not valid or anythoing else It will show errir according to data recieved .
            else:
                json_data = JSONRenderer().render(serializer.error_messages)
                return HttpResponse(json_data, content_type = 'application/json')
    # If request is GET 
    else :
        return HttpResponse("Hey I am registration_api.You are on making a 'GET' request.Make a POST request to use me.")
    
        