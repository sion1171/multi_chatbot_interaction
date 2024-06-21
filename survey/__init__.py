
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    
    
class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age in years? (Write numbers only) ', max=125, min=1,blank=False)
    English = models.StringField(choices=[['Yes', 'Yes'], ['No', 'No']], label='Are you able to speak and read English?', widget=widgets.RadioSelect,blank=False)
    residing = models.StringField(choices=[['Yes', 'Yes'], ['No', 'No']], label='Are you currently residing in the United States?', widget=widgets.RadioSelect,blank=False)
    gender = models.StringField(choices=[['Male', 'Male'], ['Female', 'Female'], ['Other', 'Other']], label='What is your sex?', widget=widgets.RadioSelect,blank=False)
    marital = models.StringField(choices=[['1', 'Married/ Living with partner'], ['2', 'Widowed/ Divorced/ Separated'], ['3', 'Never married/ Single']], label='What is your marital status?', widget=widgets.RadioSelect,blank=False)
    education = models.StringField(choices=[['1', 'Less than high school degree'], ['2', 'High school graduate/ GED or some college/ Associate of Arts (AA) degree'], ['3', 'College graduate or above']], label='What is the highest educational degree you have obtained??', widget=widgets.RadioSelect,blank=False)
    race = models.StringField(choices=[['American Indian or Alaskan Native', 'American Indian or Alaskan Native'], ['Asian or Pacific Islander', 'Asian or Pacific Islander'], ['Black or African American', 'Black or African American'], ['Hispanic/Latino', 'Hispanic/Latino'], ['White', 'White'], ['Mixed Race', 'Mixed Race'], ['Other', 'Other']], label='What is your race or ethnicity?',blank=False)
    political = models.StringField(choices=[['1', ' 1 - Extreme liberal'], ['2', '2 - liberal'], ['3', '3 - Slight liberal'], ['4', '4 - Moderate'], ['5', '5 - Slight conservative'],['6', '6 - conservative'],['7', '7 - Extreme conservative']], label='What is your political ideology? [please rate on a scale of 1-7]', widget=widgets.RadioSelect,blank=False)
    employment = models.StringField(choices=[['1', 'Full/part time job for pay'], ['2', 'Unemployed/looking for a job/retired/disabled/student']], label='What is your employment status?', widget=widgets.RadioSelect,blank=False)
    birth = models.StringField(choices=[['1', 'US born'], ['2', 'Non-US born']], label='What is your country of birth?', widget=widgets.RadioSelect,blank=False)


class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'English', 'residing', 'gender', 'marital', 'education','race','political','employment','birth']


class CognitiveReflectionTest(Page):
    form_model = 'player'

page_sequence = [Demographics]

