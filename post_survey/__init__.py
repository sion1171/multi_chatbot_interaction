from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'post_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    donate = models.IntegerField(
        label="Which charity would you like to donate to?",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Save the Children"],
            [2, "UNICEF"],
        ],
        blank=False
    )    
    money = models.IntegerField(label='If you could, how much would you like to donate? Please provide your answer in the space below.(In US Dollar) ', max=999999, min=0,blank=False)


class Demographics(Page):
    form_model = 'player'
    form_fields = ['donate','money']


page_sequence = [Demographics]
