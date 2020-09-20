from rest_framework import serializers
from django.utils.translation import ugettext as _
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .. import models
import pycountry
import pandas as pd
from ..utils import GetConti , multisub,text_file
import pandas as pd
import re
from Legal.api.Country import COUNTRY
from Legal.api.Continent import COUNTRY1



class LegalDocuments(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    # file = serializers.FileField(
    #     max_length=None, use_url=True, allow_null=True, allow_empty_file=True,
    # )
    file_text = serializers.SerializerMethodField()
    fileter_text = serializers.SerializerMethodField()
   

    class Meta:
        model = models.Documents
        exclude = ["deleted_at", "timestamp","file"]

    def get_file_text(self, obj):
        if obj.file:
            return text_file(obj.file)

        
    def get_fileter_text(self, obj):
        listt =[]
        for country in pycountry.countries:
            if country.name in obj.text:
                df = GetConti(country.name)
                listt.append((country.name,df))
        if not listt:
            return obj.text
        else:
            data = multisub(listt, obj.text )
            if data:
                return data.replace("Warszaw", "Poland").replace("New York", "United State").replace('Copenhagen', "Denmark").replace('cabin', "home").replace("Munich", "Germany")
            else:
                return data
            
