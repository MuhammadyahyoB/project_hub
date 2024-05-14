from rest_framework.decorators import api_view
from rest_framework.response import Response
from main import models
from . import serializers


# >>>> Head Serializers <<<<<<
@api_view(['GET'])
def head(request):
    """ Head Serializer views"""
    head = models.Head.objects.all().last()
    serializer = serializers.HeadSerializer(head)
    return Response(serializer.data)


# >>>> Portfolio Serializers views <<<<<<
@api_view(['GET'])
def portfolio(request):
    """ Portfolio Serializer views """
    portfolio = models.Portfolio.objects.all()
    serializer = serializers.PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)


# >>>> Team Serializers views <<<<<<
@api_view(['GET'])
def team(request):
    """ Team Serializer views """
    team = models.Team.objects.all()
    serializer = serializers.TeamSerializer(team, many=True)


# >>>>>>> Vakansiya serialzers views <<<<<< 
@api_view(['GET'])
def vakansiya(request):
    """ Vakansiya serializers views """
    vakansiya = models.Vakansiya.objects.all()
    serializer = serializers.VakansiyaSerializer(vakansiya, many=True)
    return Response(serializer.data)


# >>>> Message Serializers views <<<<<<
@api_view(['POST'])
def post_message(request):
    """ Message serializers views """
    if request.method == 'POST':
        serializer = serializers.MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



# >>>> Resume Serializers views <<<<<<
@api_view(['POST'])
def post_resume(request):
    """Resume a serializer views """
    if request.method == 'POST':
        serializer = serializers.ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)