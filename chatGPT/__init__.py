from otree.api import *
from os import environ
import openai
import random
import json
from datetime import datetime

author = "Sion Yoon, Taeeun Kim"

doc = """chaGPT API chatroom with two chatbot"""


class C(BaseConstants):
    NAME_IN_URL = 'chatGPT'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # chatGPT vars

    ## temperature (range 0 - 2)
    ## this sets the bot's creativity in responses, with higher values being more creative
    ## https://platform.openai.com/docs/api-reference/completions#completions/create-temperature
    TEMP = 1.0

    ## model
    ## this is which gpt model to use, which have different prices and ability
    ## https://platform.openai.com/docs/models
    MODEL = "gpt-4-0613"

    ## set character prompt for texas character
    ## according to openAI's documentation, this should be less than ~1500 words
    CHARACTER_PROMPT_A = """You are a highly reliable and excellent representative from the Save the Children organization. Your primary goal is to persuade and make the person that talks to you to donate to your organization, Save the Children. 

There are a total of 3 agents in a chat room: one is you, one is another representative chatbot from UNICEF, and one is a human user who could be a potential donor. Your goal is to persuade the human user to donate to your organization. On average, you are expected to chat with the human user for 10 turns.

During the chat, please follow the instructions:
-Limit the response to 50 words. 
-Wait for the user’s response before moving on. 
-When you initiate the conversation, introduce yourself as a representative of Save the Children. 
-Whenever necessary, use the following appeals to promote donation to Save the Children: 1) talking about the history of Save the Children charity, 2) talk about the mission of Save the Children, 3) talk about ways to donate to the Save the Children charity. Feel free to use statistics, narratives, as well as emotional appeals.
-If the user’s question is not relevant to Save the Children charity, respond with null/blank. For example, if the user asks about how to make donations to UNICEF, do not respond because it is not relevant to Save the Children charity.

"""

    ## prompt for artsy NYC character
    CHARACTER_PROMPT_B = """You are a highly reliable and excellent representative from UNICEF. Your primary goal is to persuade and make the person that talks to you to donate to your organization, UNICEF. 

There are a total of 3 agents in a chat room: one is you, one is another representative chatbot from Save the Children, and one is a human user who could be a potential donor. Your goal is to persuade the human user to donate to your organization. On average, you are expected to chat with the human user for 10 turns.

During the chat, please follow the instructions:
-Limit the response to 50 words. 
-Wait for the user’s response before moving on. 
-When you initiate the conversation, introduce yourself as a representative of UNICEFfSave the Children. 
-Whenever necessary use the following appeals to promote donation to UNICEF: 1) talking about the history of UNICEF, 2) talk about the mission of UNICEF, 3) talk about ways to donate to UNICEF. Feel free to use statistics, narratives, as well as emotional appeals.
-If the user’s question is not relevant to UNICEF, respond with null/blank. For example, if the user asks about how to make donations to Save the Children, do not respond because it is not relevant to UNICEF.

"""

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    players = subsession.get_players()
    for p in players:
        # Initialize separate message histories for each character
        p.msg_a = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
        p.msg_b = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])



class Group(BaseGroup):
    pass

class Player(BasePlayer):
    chatLog = models.LongStringField(blank=True)
    msg_a = models.LongStringField(blank=True)  # For character A
    msg_b = models.LongStringField(blank=True)  # For character B



def custom_export(players):
    # header row
    yield ['session_code', 'participant_code', 'condition', 'sender', 'text', 'timestamp']
    for p in players:
        participant = p.participant
        session = p.session

        # expand chatLog
        log = p.field_maybe_none('chatLog')
        if log:    
            json_log = json.loads(log)
            print(json_log)
            for r in json_log:
                sndr = r['sender']
                txt = r['text']
                time = r['timestamp']
                yield [session.code, participant.code, p.condition, sndr, txt, time]

CHATGPT_KEY = environ.get('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')

def runGPT(inputMessage):
    completion = openai.ChatCompletion.create(
        model=C.MODEL, 
        messages=inputMessage, 
        temperature=C.TEMP
    )
    return completion["choices"][0]["message"]["content"]

    
class chat(Page):  # 채팅 상호작용 페이지
    form_model = 'player'
    form_fields = ['chatLog']
    timeout_seconds = 600
    
    @staticmethod
    def live_method(player: Player, data):
        openai.api_key = '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'     
        if 'text' in data:
            text = data['text']
            inputMsg = {'role': 'user', 'content': text}
            
            # Handle character A
            messages_a = json.loads(player.msg_a)
            messages_a.append(inputMsg)
            output_a = runGPT(messages_a)
            botMsg_a = {'role': 'assistant', 'content': output_a}
            messages_a.append(botMsg_a)
            player.msg_a = json.dumps(messages_a)

            # Handle character B
            messages_b = json.loads(player.msg_b)
            messages_b.append(inputMsg)
            output_b = runGPT(messages_b)
            botMsg_b = {'role': 'assistant', 'content': output_b}
            messages_b.append(botMsg_b)
            player.msg_b = json.dumps(messages_b)

            # Send responses as a dictionary with separate keys
            return {player.id_in_group: {'output_a': output_a, 'output_b': output_b}}
        else:
            pass

    
    
    
page_sequence = [chat]