from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(["POST","GET"])
def calc(request):
    data=request.data
    print(data)
    num1=data.get('num1')
    num2=data.get('num2')
    print(num1,num2)
    sumtion=num1+num2
    return Response({'sum':sumtion})
