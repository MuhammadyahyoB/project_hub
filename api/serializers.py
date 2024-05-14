from main import models
from rest_framework.serializers import ModelSerializer



# ---------- head serializers --------
class HeadSerializer(ModelSerializer):
    """ Head serializer """
    class Meta:
        model = models.Head
        fields = '__all__'



# ---------- Portfolio serializers --------
class PortfolioSerializer(ModelSerializer):
    """ Portfolio serializer """
    class Meta:
        model = models.Portfolio
        fields = '__all__'



# ---------- Team serializers --------
class TeamSerializer(ModelSerializer):
    """ Team serializer """
    class Meta:
        model = models.Team
        fields = '__all__'



# ---------- Massage serializers --------
class MessageSerializer(ModelSerializer):
    """ Massage serializer """
    class Meta:
        model = models.Message
        fields = '__all__'



# ---------- Resume serializers --------
class ResumeSerializer(ModelSerializer):
    """ Resume serializers """
    class Meta:
        model = models.Resume
        fields = '__all__'


# ---------- Vacancy serializers --------
class VakansiyaSerializer(ModelSerializer):
    """ Vakansiya serializers """
    class Meta:
        model = models.Vakansiya
        fields = '__all__'