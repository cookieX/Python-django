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



    # def get_file(self, obj):
    #     if obj.file:
    #         return self.context["request"].build_absolute_uri(obj.file.url)

    # def create(self, validated_data):
    #     validated_data["created_by"] = self.context["request"].user
    #     return super().create(validated_data)
    
    # Get File context as text.
    def get_file_text(self, obj):
        if obj.file:
            return text_file(obj.file)

        

    def get_fileter_text(self, obj):
        listt =[]
        for country in pycountry.countries:
            if country.name in obj.text:
                #print(country.name)
                #country = {"Country": [country.name]}
                df = GetConti(country.name)
                listt.append((country.name,df))
                #TBH for testing
                #list.append(df)
                #count.append(country.name)
                # print(text.replace(country.name, df) for n in text)
                #print(df)
        # if not listt:
        #     return obj.text
        # else:
        #     text2 = multisub(listt, obj.text )
        #     list1 =[]
        #     for citis in pycountry.subdivisions:
        #         if citis.name in text2:
        #             for count in  COUNTRY[COUNTRY1]:
        #                 if citis.name in count:
        #                     list1.append((citis.name,count))
        #                  else: 
        #                     pass
        if not listt:
            return obj.text
        else:
            data = multisub(listt, obj.text )
            if data:
                return data.replace("Warszaw", "Poland").replace("New York", "United State").replace('Copenhagen', "Denmark").replace('cabin', "home").replace("Munich", "Germany")
            else:
                return data
            
