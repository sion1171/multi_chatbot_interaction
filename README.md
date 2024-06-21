# Designing and Evaluating Multi-Chatbot Interface for Human-AI Communication: Preliminary Findings from a Persuasion Task
##### Created at [Michigan State University](https://msu.edu) by [Yoo Jung (Erika) Oh](mailto:ohyoojun@msu.edu), [Sion Yoon](mailto:yoonsion@msu.edu), and [Tae Eun Kim](mailto:kimtaee3@msu.edu)
## Introduction
The dynamics of human-AI communication have evolved significantly with the advent of sophisticated language models such as ChatGPT. While much research has focused on dyadic (one-on-one) human-AI interactions, there remains a significant gap in understanding how humans interact with multiple AI chatbots simultaneously, especially in group settings. This repository is part of a study aimed at exploring these dynamics in a specific context: promoting charitable donations.

## Overview of Survey and Chatroom Interface

We developed a web platform designed to facilitate simultaneous conversations with multiple chatbots, integrating standard survey functionality with a multi-chatbot chatroom environment. The platform, as illustrated in the figure below, was implemented using the oTree API and includes a pre-survey, [a chatroom for interactions with two chatbots](#chatroom-interface), and a post-survey. We utilized the 'gpt-4-0613' model from the OpenAI ChatGPT-4 API for chatbot interactions. PostgreSQL was chosen as the database system to store and manage the survey and chat data.

![Overview Diagram](/gif/flow_ex_1.png)

### Chatroom Interface

The chatroom offers three random scenarios:
1. Talking only to the "Save the Children" chatbot.
2. Talking only to the "UNICEF" chatbot.
3. Talking with both the "Save the Children" and "UNICEF" chatbots.

As shown in the videos below, the interface provides a natural conversation experience with typing indicators and profile functions, enhancing user interaction.

<p align="center">
  <img src="/gif/stc_2.gif" width="30%" />
  <img src="/gif/uni_2.gif" width="30%" />
  <img src="/gif/both.gif" width="30%" />
</p>

## Installation Steps
1. Install oTree and OpenAI API
   ```sh
   pip install -r requirements.txt
   ```
2. Clone the repository
   ```sh
   git clone https://github.com/sion1171/multi_chatbot_interaction.git
   ```
3. Navigate to the project directory
   ```sh
   cd your-repo-name
   ```
3. Zip otree project
   ```sh
   otree zip
   ```
4. Run oTree server
   ```sh
   otree devserver
   ```

## Contact

For any questions or feedback, please reach out to us:

-**Principal Investigator:** [Yoo Jung (Erika) Oh](mailto:ohyoojun@msu.edu)  
-**Software Engineer:** [Sion Yoon](mailto:yoonsion@msu.edu), [Tae Eun Kim](mailto:kimtaee3@msu.edu)


## Citation
- Chen, D.L., Schonger, M., Wickens, C., 2016. oTree - An open-source platform for laboratory, online and field experiments. Journal of Behavioral and Experimental Finance, vol 9: 88-97.
- McKenna, C., (2023). oTree GPT. https://github.com/clintmckenna/oTree_gpt
