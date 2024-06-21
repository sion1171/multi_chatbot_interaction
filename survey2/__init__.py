from otree.api import *

class C(BaseConstants):
    NAME_IN_URL = 'survey2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LIKERT_LABELS = ['Disagree strongly', 'Disagree a little', 'Neutral; no opinion', 'Agree a little', 'Agree strongly']

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    worries_a_lot = models.StringField(
        choices=[
            (1, 'Disagree strongly'),
            (2, 'Disagree a little'),
            (3, 'Neutral; no opinion'),
            (4, 'Agree a little'),
            (5, 'Agree strongly')
        ],
        label="Worries a lot",
        widget=widgets.RadioSelect,
        blank=False
    )
    nervous_easily = models.StringField(
        choices=[
            (1, 'Disagree strongly'),
            (2, 'Disagree a little'),
            (3, 'Neutral; no opinion'),
            (4, 'Agree a little'),
            (5, 'Agree strongly')
        ],
        label="Gets nervous easily",
        widget=widgets.RadioSelect,
        blank=False
    )
    calm = models.StringField(
        choices=[
            (1, 'Disagree strongly'),
            (2, 'Disagree a little'),
            (3, 'Neutral; no opinion'),
            (4, 'Agree a little'),
            (5, 'Agree strongly')
        ],
        label="Remains calm in tense situations",
        widget=widgets.RadioSelect,
        blank=False
    )
    talkative = models.StringField(
        choices=[
            (1, 'Disagree strongly'),
            (2, 'Disagree a little'),
            (3, 'Neutral; no opinion'),
            (4, 'Agree a little'),
            (5, 'Agree strongly')
        ],
        label="Is talkative",
        widget=widgets.RadioSelect,
        blank=False
    )
    outgoing = models.StringField(
        choices=[
            (1, 'Disagree strongly'),
            (2, 'Disagree a little'),
            (3, 'Neutral; no opinion'),
            (4, 'Agree a little'),
            (5, 'Agree strongly')
        ],
        label="Is outgoing, sociable",
        widget=widgets.RadioSelect,
        blank=False
    )

class Demographics(Page):
    form_model = 'player'
    form_fields = ['worries_a_lot', 'nervous_easily', 'calm', 'talkative', 'outgoing']

    def vars_for_template(self):
        return {
            'likert_5_labels': C.LIKERT_LABELS
        }

page_sequence = [Demographics]
