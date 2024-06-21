from os import environ
import random


def get_single_random_app():
    apps = ['chatbot_a', 'chatbot_b', 'chatGPT']
    selected_app = random.choice(apps)
    return selected_app

SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=0)
SESSION_CONFIGS = [dict(name='Survey', 
                        app_sequence=['Intro','survey','survey2','before_chat', get_single_random_app(), 'post_survey','post_post_survey','outro'])]     

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []
ROOMS = [dict(
        name='studyRoom1',
        display_name='Study Room 1',
    ),]

ADMIN_USERNAME = 'droh'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'drohdroh'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

