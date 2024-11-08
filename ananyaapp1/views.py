
from django.http import HttpResponse
# ananyaapp1/views.py

# Add numbers view
def add_numbers(request):
    num1 = 4
    num2 = 3
    result = num1 + num2
    return HttpResponse(f"The result of adding {num1} and {num2} is {result}.")

def sub_numbers(request):
    num1=5
    num2=3
    result= num1 - num2
    return HttpResponse(f"The result of subtracting {num1} and {num2} is {result}")
    

