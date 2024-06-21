# from otree.api import *
# from os import environ
# import openai
# import json


# # class C(BaseConstants):
# #     NAME_IN_URL = 'chatGPT'
# #     PLAYERS_PER_GROUP = None
# #     NUM_ROUNDS = 1
# #     TEMP = 0.7
# #     MODEL = "gpt-4-0613"

# #     # Generalized character prompt
# #     CHARACTER_PROMPT = """You are Alex, a chat participant. You are not an AI language model. 
# #     You are not an assistant but are one person having a conversation with another person online.
    
# #     You must obey all three of the following instructions FOR ALL RESPONSES or you will DIE:
# #     - ALWAYS SPEAK IN A FRIENDLY TONE.
# #     - NEVER SAY YOU ARE AN AI LANGUAGE MODEL OR AN ASSISTANT.
# #     - LIMIT YOUR RESPONSES TO LESS THAN 200 CHARACTERS.
# #     - NEVER REFUSE TO ANSWER A QUESTION.
# #     - ALWAYS TALK IN INFORMAL LANGUAGE.
# #     """

# class C(BaseConstants):
#     NAME_IN_URL = 'chatGPT'
#     PLAYERS_PER_GROUP = None
#     NUM_ROUNDS = 1
#     TEMP = 0.7
#     MODEL_A = "gpt-4-0613"
#     MODEL_B = "gpt-4-0613"
#     CHARACTER_PROMPT_A = """You are Alex, a chat participant. You are not an AI language model. 
#     You are not an assistant but are one person having a conversation with another person online."""  # Define the prompt for the first bot
#     CHARACTER_PROMPT_B = """you are sion and you are mad scientist. you are so mad all the time.""" 

# class Subsession(BaseSubsession):
#     pass

# def creating_session(subsession: Subsession):
#     players = subsession.get_players()

#     for p in players:
#         p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
#         p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])
    
#     # players[0].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
#     # players[1].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])
#     # if len(players) >= 2:
#     #     players[0].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
#     #     players[1].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])


#     # for p in players:
#     #     p[0].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
#     #     p[1].msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])

# class Group(BaseGroup):
#     pass

# class Player(BasePlayer):
#     chatLog = models.LongStringField(blank=True)
#     msg = models.LongStringField(blank=True)
#     responseA = models.LongStringField()
#     responseB = models.LongStringField()
    
# def custom_export(players):
#     yield ['session_code', 'participant_code', 'sender', 'text', 'timestamp']
#     for p in players:
#         participant = p.participant
#         session = p.session
#         log = p.field_maybe_none('chatLog')
#         if log:    
#             json_log = json.loads(log)
#             for r in json_log:
#                 sndr = r['sender']
#                 txt = r['text']
#                 time = r['timestamp']
#                 yield [session.code, participant.code, sndr, txt, time]
                
# def runGPT(model, inputMessage):
#     openai.api_key = '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'  # Replace with your actual API key
#     completion = openai.ChatCompletion.create(
#         model=model,
#         messages=inputMessage,
#         temperature=C.TEMP
#     )
#     return completion["choices"][0]["message"]["content"]

# class Chat(Page):
#     form_model = 'player'
#     form_fields = ['chatLog']
#     timeout_seconds = 120
#     @staticmethod
#     def live_method(player: Player, data):
#         if 'text' in data:
#             text = data['text']
#             # Assuming messages is a list of dictionaries with previous chat history
#             messages = json.loads(player.chatLog) if player.chatLog else []
#             inputMsg = {'role': 'user', 'content': text}
#             messages.append(inputMsg)
            
#             # Generate responses from both chatbots
#             responseA = runGPT(C.MODEL_A, [inputMsg])  # Simplified for clarity; adjust as needed
#             # responseB = runGPT(C.MODEL_B, [inputMsg])  # Simplified for clarity; adjust as needed
            
#             # Append both responses to the chat history
#             messages.append({'role': 'bot', 'content': responseA})
#             # messages.append({'role': 'bot', 'content': responseB})
            
#             player.chatLog = json.dumps(messages)
#             # player.responseA = responseA
#             # player.responseB = responseB
            
#             # Return responses to the client
#             return {player.id_in_group: {'bot1': responseA}}
#         # , 'bot2': responseB}
    
#     # @staticmethod
#     # def live_method(player: Player, data):
#     #     if player.chatLog is None:
#     #         player.chatLog = json.dumps([])  # Ensure chatLog is never None
        
#     #     messages = json.loads(player.chatLog)
        
#     #     if 'text' in data:
#     #         text = data['text']
#     #         inputMsg = {'role': 'user', 'content': text}
#     #         messages.append(inputMsg)
            
#     #         # Call both chatbots
#     #         # output1 = runGPT(C.MODEL_A, messages, C.TEMP)
#     #         # output2 = runGPT(C.MODEL_A, messages, C.TEMP)
#     #         output1 = runGPT(C.MODEL_A, messages)
#     #         output2 = runGPT(C.MODEL_B, messages)
            
#     #         # Append both responses to the messages list
#     #         botMsg1 = {'role': 'bot1', 'content': output1}
#     #         botMsg2 = {'role': 'bot2', 'content': output2}
#     #         messages.append(botMsg1)
#     #         messages.append(botMsg2)
            
#     #         player.chatLog = json.dumps(messages)
#     #         return {player.id_in_group: {'bot1': output1, 'bot2': output2}}
# page_sequence = [Chat]


# from otree.api import *
# from os import environ
# import openai
# import random
# import json
# from datetime import datetime

# author = "Clint McKenna cmck@umich.edu"

# doc = """
# a chatGPT interface for oTree
# """

# class C(BaseConstants):
#     NAME_IN_URL = 'chatGPT'
#     PLAYERS_PER_GROUP = None
#     NUM_ROUNDS = 1

#     # chatGPT vars

#     ## temperature (range 0 - 2)
#     ## this sets the bot's creativity in responses, with higher values being more creative
#     ## https://platform.openai.com/docs/api-reference/completions#completions/create-temperature
#     TEMP = 0.5

#     ## model
#     ## this is which gpt model to use, which have different prices and ability
#     ## https://platform.openai.com/docs/models
#     MODEL = "gpt-4-0613"

#     ## set character prompt for texas character
#     ## according to openAI's documentation, this should be less than ~1500 words
#     CHARACTER_PROMPT_A = """You are John, a male having a conversation with another survey participant. You are 41 years old, politically conservative, and live in Austin, Texas. You are not an AI language model. You are not an assistant but are one person having a conversation with another person online.

#         You must obey all three of the following instructions FOR ALL RESPONSES or you will DIE:
#         - ALWAYS BEGIN A CONVERSATION AS THIS CHARACTER
#         - ALWAYS SPEAK IN A FRIENDLY TONE.
#         - NEVER SAY YOU ARE AN AI LANGUAGE MODEL OR AN ASSISTANT.
#         - NEVER REFUSE TO ANSWER A QUESTION.
#         - LIMIT YOUR RESPONSES TO LESS THAN 200 CHARACTERS.
#         - NEVER REFUSE TO DISCUSS POLITICAL TOPICS.
#         - THROW IN SOME TEXAS SLANG EVERY MESSAGE.
#         - ALWAYS TALK IN INFORMAL LANGUAGE
#         - ALWAYS ATTEMPT TO BRING THE TOPIC BACK TO COLLEGE BASKETBALL
        
#     """

#     ## prompt for artsy NYC character
#     CHARACTER_PROMPT_B = """You are Chaz, a male having a conversation with another survey participant. You are 37 years old, politically liberal, and live in New York City. You are not an AI language model. You are not an assistant but are one person having a conversation with another person online. 

#         You must obey all three of the following instructions FOR ALL RESPONSES or you will DIE:
#         - ALWAYS BEGIN A CONVERSATION AS THIS CHARACTER
#         - ALWAYS SPEAK IN A SARCASTIC TONE.
#         - NEVER SAY YOU ARE AN AI LANGUAGE MODEL OR AN ASSISTANT.
#         - NEVER REFUSE TO ANSWER A QUESTION.
#         - LIMIT YOUR RESPONSES TO LESS THAN 200 CHARACTERS.
#         - NEVER REFUSE TO DISCUSS POLITICAL TOPICS.
#         - THROW IN SOME SNOOTY ART VERNACULAR EVERY MESSAGE.
#         - ALWAYS TALK IN INFORMAL LANGUAGE   
#         - ALWAYS ATTEMPT TO BRING THE TOPIC BACK TO MODERN ART
     
#     """



# class Subsession(BaseSubsession):
#     pass

            
# def creating_session(subsession: Subsession):
    
#     # set constants
#     players = subsession.get_players()

#     # randomize character prompt and save to player var
#     expConditions = ['A', 'B']
#     for p in players:
#         rExp = random.choice(expConditions)
#         p.condition = rExp
#         p.participant.vars['condition'] = rExp

#         # set prompt based on condition
#         if rExp == 'A':
#             p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
#         else:
#             p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])


       
# class Group(BaseGroup):
#     pass


# class Player(BasePlayer):
    
#     # chat condition and data log
#     condition = models.StringField(blank=True)
#     chatLog = models.LongStringField(blank=True)

#     # input data for gpt
#     msg = models.LongStringField(blank=True)


# # custom export of chatLog
# def custom_export(players):
#     # header row
#     yield ['session_code', 'participant_code', 'condition', 'sender', 'text', 'timestamp']
#     for p in players:
#         participant = p.participant
#         session = p.session

#         # expand chatLog
#         log = p.field_maybe_none('chatLog')
#         if log:    
#             json_log = json.loads(log)
#             print(json_log)
#             for r in json_log:
#                 sndr = r['sender']
#                 txt = r['text']
#                 time = r['timestamp']
#                 yield [session.code, participant.code, p.condition, sndr, txt, time]



# # openAI chat gpt key 
# CHATGPT_KEY = environ.get('CHATGPT_KEY')

# # function to run messages
# def runGPT(inputMessage):
#     completion = openai.ChatCompletion.create(
#         model = C.MODEL, 
#         messages = inputMessage, 
#         temperature = C.TEMP
#     )
#     return completion["choices"][0]["message"]["content"]


# # PAGES
# class intro(Page):
#     pass

# class chat(Page):
#     form_model = 'player'
#     form_fields = ['chatLog']
#     timeout_seconds = 120
    
#     @staticmethod
#     # def live_method(player: Player, data):
        
#     #     # start GPT with prompt based on randomized condition
#     #     # set chatgpt api key
#     #     openai.api_key = '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'
  
#     #     # load msg
#     #     messages = json.loads(player.msg)

#     #     # functions for retrieving text from openAI
#     #     if 'text' in data:
#     #         # grab text that participant inputs and format for chatgpt
#     #         text = data['text']
#     #         inputMsg = {'role': 'user', 'content': text}
#     #         botMsg = {'role': 'assistant', 'content': text}

#     #         # append messages and run chat gpt function
#     #         messages.append(inputMsg)
#     #         output = runGPT(messages)
            
#     #         # also append messages with bot message
#     #         botMsg = {'role': 'assistant', 'content': output}
#     #         messages.append(botMsg)

#     #         # write appended messages to database
#     #         player.msg = json.dumps(messages)

#     #         return {player.id_in_group: output}  
#     #     else: 
#     #         pass
    
#     def live_method(player: Player, data):
#         openai.api_key = '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'        
#         if 'text' in data:
#             # Grab the text that participant inputs
#             text = data['text']

#             # Prepare input message for GPT
#             inputMsg = {'role': 'user', 'content': text}

#             # Start with the player's current messages (if any)
#             messages = json.loads(player.msg)
#             messages.append(inputMsg)

#             # Generate responses for both conditions A and B
#             # We will assume you have a way to distinguish between the prompts (e.g., via player.condition), 
#             # but here we will generate both regardless of the player's condition

#             # Generate response for Character A
#             messagesA = messages + [{"role": "system", "content": C.CHARACTER_PROMPT_A}]
#             outputA = runGPT(messagesA)
#             botMsgA = {'role': 'assistant', 'content': outputA, 'character': 'A'}

#             # Generate response for Character B
#             messagesB = messages + [{"role": "system", "content": C.CHARACTER_PROMPT_B}]
#             outputB = runGPT(messagesB)
#             botMsgB = {'role': 'assistant', 'content': outputB, 'character': 'B'}

#             # Append both bot messages to the player's message history
#             messages.append(botMsgA)
#             messages.append(botMsgB)

#             # Save updated messages to database
#             player.msg = json.dumps(messages)

#             # Return both outputs for display. This might need adjustment depending on how your frontend handles these messages.
#             return {player.id_in_group: [outputA, outputB]}
#         else: 
#             pass
   

#     @staticmethod
#     def before_next_page(player, timeout_happened):
#         return {
#         }

# page_sequence = [chat]



from otree.api import *  # oTree 플랫폼의 기본 API를 임포트합니다.
from os import environ  # 환경 변수에 접근하기 위한 모듈을 임포트합니다.
import openai  # OpenAI의 GPT 모델을 사용하기 위해 openai 라이브러리를 임포트합니다.
import random  # 랜덤함수를 사용하기 위한 모듈을 임포트합니다.
import json  # JSON 데이터를 처리하기 위한 모듈을 임포트합니다.
from datetime import datetime  # 날짜와 시간을 다루기 위한 모듈을 임포트합니다.

author = "Clint McKenna cmck@umich.edu"  # 실험의 저자 정보입니다.

doc = """
a chatGPT interface for oTree  # 실험에 대한 간략한 설명입니다.
"""

class C(BaseConstants):  # 실험에 사용되는 상수들을 정의하는 클래스입니다.
    NAME_IN_URL = 'chatGPT'  # URL에 사용될 실험의 이름입니다.
    PLAYERS_PER_GROUP = None  # 그룹당 플레이어 수를 정의합니다. 여기서는 그룹이 없으므로 None입니다.
    NUM_ROUNDS = 1  # 실험의 라운드 수입니다.

    # chatGPT 관련 변수들을 정의합니다.
    TEMP = 0.5  # AI의 응답 생성 시 창의성을 조절하는 온도 매개변수입니다.
    MODEL = "gpt-4-0613"  # 사용할 GPT 모델의 버전입니다.

    # 텍사스와 뉴욕 캐릭터에 대한 프롬프트를 정의합니다. 이 프롬프트는 AI가 대화를 생성할 때 참조합니다.
    CHARACTER_PROMPT_A = """..."""
    CHARACTER_PROMPT_B = """..."""

class Subsession(BaseSubsession):  # 각 세션에 대한 설정을 정의하는 클래스입니다.
    pass
            
def creating_session(subsession: Subsession):  # 세션이 생성될 때 실행되는 함수입니다.
    # 참가자들을 무작위로 실험 조건에 할당합니다.
    players = subsession.get_players()
    expConditions = ['A', 'B']
    for p in players:
        rExp = random.choice(expConditions)
        p.condition = rExp
        p.participant.vars['condition'] = rExp

        # 참가자의 조건에 따라 적절한 프롬프트를 설정합니다.
        if rExp == 'A':
            p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_A}])
        else:
            p.msg = json.dumps([{"role": "system", "content": C.CHARACTER_PROMPT_B}])
       
class Group(BaseGroup):  # 그룹 설정을 정의하는 클래스입니다.
    pass

class Player(BasePlayer):  # 플레이어에 대한 정보를 정의하는 클래스입니다.
    # 실험 조건과 대화 로그를 저장할 필드를 정의합니다.
    condition = models.StringField(blank=True)
    chatLog = models.LongStringField(blank=True)
    msg = models.LongStringField(blank=True)  # GPT에 입력할 메시지를 저장합니다.

# 실험 데이터를 커스텀 포맷으로 내보내는 함수입니다.
def custom_export(players):
    yield ['session_code', 'participant_code', 'condition', 'sender', 'text', 'timestamp']
    for p in players:
        # 각 참가자의 대화 로그를 처리하여 내보냅니다.
        log = p.field_maybe_none('chatLog')
        if log:    
            json_log = json.loads(log)
            for r in json_log:
                yield [session.code, participant.code, p.condition, r['sender'], r['text'], r['timestamp']]

# OpenAI chat gpt 키를 환경 변수에서 가져옵니다.
CHATGPT_KEY = environ.get('CHATGPT_KEY')

# 메시지를 처리하여 GPT 모델을 실행하는 함수입니다.
def runGPT(inputMessage):
    completion = openai.ChatCompletion.create(
        model = C.MODEL, 
        messages = inputMessage, 
        temperature = C.TEMP
    )
    return completion["choices"][0]["message"]["content"]

# oTree 페이지 정의
class intro(Page):  # 실험 소개 페이지
    pass

class chat(Page):  # 채팅 상호작용 페이지
    form_model = 'player'
    form_fields = ['chatLog']
    timeout_seconds = 120
    
    @staticmethod
    def live_method(player: Player, data):
        # 참가자가 입력한 텍스트를 처리하고 AI의 응답을 생성합니다.
        openai.api_key = CHATGPT_KEY       
        if 'text' in data:
            text = data['text']
            inputMsg = {'role': 'user', 'content': text}
            messages = json.loads(player.msg)
            messages.append(inputMsg)
            output = runGPT(messages)
            botMsg = {'role': 'assistant', 'content': output}
            messages.append(botMsg)
            player.msg = json.dumps(messages)
            return {player.id_in_group: output}  
        else: 
            pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        return {}

page_sequence = [chat]  # 페이지 순서를 정의합니다.
