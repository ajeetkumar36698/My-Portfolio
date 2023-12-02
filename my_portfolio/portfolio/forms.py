from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django import forms

class input_data(forms.Form):
    number_courses = forms.FloatField()
    time_study= forms.FloatField()



class input_data_house_prediction(forms.Form):
    bedrooms=forms.FloatField()
    bathrooms=forms.FloatField()
    sqft_living=forms.FloatField()
    sqft_lot=forms.FloatField()
    floors=forms.FloatField()
    waterfront=forms.FloatField()
    view=forms.FloatField()
    condition=forms.FloatField()
    grade=forms.FloatField()
    sqft_above=forms.FloatField()
    sqft_basement=forms.FloatField()
    yr_built=forms.FloatField()
    yr_renovated=forms.FloatField()
    zipcode=forms.FloatField()
    lat=forms.FloatField()
    long=forms.FloatField()
    sqft_living15=forms.FloatField()
    sqft_lot15=forms.FloatField()


class input_body_health_prediction(forms.Form):
    Gender=(
        (1,"Male"),
        (2,'Female')
    )

    Gender=forms.ChoiceField(choices=Gender)
    Height=forms.FloatField()
    Weight=forms.FloatField()


class input_data_science_salary_prediction(forms.Form):
    work_year=forms.IntegerField()
    # experience_level=(("EN",1),("MI",2),("SE",3),("EX",4))
    experience_level=forms.CharField()
    # employment_type=(("PT",1),("FT",2),("CT",3),("FL",4))
    employment_type=forms.CharField()
    # job_title=(('Data Scientist',50),('Data Engineer',49),('Data Analyst',48),('Machine Learning Engineer',47),('Research Scientist',46),('Data Science Manager',45),('Data Architect',44),('Big Data Engineer',43),('Machine Learning Scientist',42),('Principal Data Scientist',41),('AI Scientist',40),('Data Science Consultant',39),('Director of Data Science',38),('Data Analytics Manager',37),('ML Engineer',36),('Computer Vision Engineer',35),('BI Data Analyst',34),('Lead Data Engineer',33),('Data Engineering Manager',32),('Business Data Analyst',31),('Head of Data',30),('Applied Data Scientist',29),('Applied Machine Learning Scientist',28),('Head of Data Science',27),('Analytics Engineer',26),('Data Analytics Engineer',25),('Machine Learning Developer',24),('Machine Learning Infrastructure Engineer',23),('Lead Data Scientist',22),('Computer Vision Software Engineer',21),('Lead Data Analyst',20),('Data Science Engineer',19),('Principal Data Engineer',18),('Principal Data Analyst',17),('ETL Developer',16),('Product Data Analyst',15),('Director of Data Engineering',14),('Financial Data Analyst',13),('Cloud Data Engineer',12),('Lead Machine Learning Engineer',11),('NLP Engineer',10), ('Head of Machine Learning',9), ('3D Computer Vision Researcher',8,('Data Specialist',7),('Staff Data Scientist',6),('Big Data Architect',5),('Finance Data Analyst',4),('Marketing Data Analyst',3),('Machine Learning Manager',2),('Data Analytics Lead',1))
    job_title=forms.CharField()
    salary_currency=forms.CharField()
    salary_in_usd=forms.FloatField()
    employee_residence=forms.CharField()
    remote_ratio=forms.FloatField()
    company_location=forms.CharField()
    company_size=forms.CharField()






