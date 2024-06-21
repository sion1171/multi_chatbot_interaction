from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'post_survey7'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    realistic_engaging_un = models.IntegerField(
        label="The UNICEF chatbot’s personality was realistic and engaging",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    too_robotic_un = models.IntegerField(
        label="The UNICEF chatbot seemed too robotic",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    understood_well_un = models.IntegerField(
        label="The UNICEF chatbot understood me well",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    failed_recognition_un = models.IntegerField(
        label="The UNICEF chatbot failed to recognise a lot of my inputs",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    not_relevant_un = models.IntegerField(
        label="UNICEF Chatbot responses were not relevant",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    coped_well_un = models.IntegerField(
        label="The UNICEF chatbot coped well with any errors or mistakes",
        widget=widgets.RadioSelectHorizontal,
        choices=[
            [1, "Disagree strongly"],
            [2, "Disagree a little"],
            [3, "Neutral; no opinion"],
            [4, "Agree a little"],
            [5, "Agree strongly"]
        ],
        blank=False
    )
    email = models.StringField(label="What is your MSU email?", blank=True)

class Demographics(Page):
    form_model = 'player'
    form_fields = [
        'realistic_engaging_un',
        'too_robotic_un',
        'understood_well_un',
        'failed_recognition_un',
        'not_relevant_un',
        'coped_well_un',
        'email'
    ]

page_sequence = [Demographics]
