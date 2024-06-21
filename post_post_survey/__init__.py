from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'post_post_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rate = models.IntegerField(label='On a scale of 1 to 10, how would you rate our chatbot based on that rating?', max=10, min=0,blank=False)
    comment = models.LongStringField(label='Please share your feedback about the chatbot. How can we improve for future experiments? What aspects of the chatbot did you find effective?' ,blank=True)


class Demographics(Page):
    form_model = 'player'
    form_fields = ['rate','comment']


page_sequence = [Demographics]
