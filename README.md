# Multi-task Rasa Chatbot with Haystack

## Why use Rasa

1.Flexiable Architecture. TED Policy allows you to directly train end-to-end conversation, also for multi-turn conversation based on Attention mechnism

This is a demo how you can use haystack with chatbot interface using RASA

The basic architecture is as below:


Rasa is also going towards more end-to-end:

Check the blog here: https://rasa.com/blog/were-a-step-closer-to-getting-rid-of-intents/


Action code:
1. information query(with haystack)
2. KG query
3. function usage like register for the vaccacine
4. other external services or human handoff

Rasa is becoming more end-to-end, check the blog:
 
https://rasa.com/blog/were-a-step-closer-to-getting-rid-of-intents/


## Multi-task
1. Chitchat with the bot
2. Ask questions about covid-19 (using haystack as backend)
3. A demo that you can register for vacacine in chabot

## Channel for the bot:

Use ui.html to fast test your bot.

https://www.npmjs.com/package/@rasahq/rasa-chat
https://chat-widget-docs.rasa.com/?path=/docs/rasa-chat-widget--widget
https://rasa.com/docs/rasa/connectors/your-own-website/#chat-widget
https://github.com/JiteshGaikwad/Chatbot-Widget

### TTS and Voice to Text

## Haystack

## CI/CD

1. Use Rasa X
2. Github Actions



## Tips for developing the chatbot
1. Check how many types of intentions, entities, form slots, actions you need in the beginning.
2. Testing and adding conversation data to your bot and retrain the model using rasa X. You may need to change the model configuration to improve the accuracy of NLU and policy prediction.
3. Build the CI/CD to automate the process.
- How to test your with Github actions using GKE
- How to deploy your bot on GKE

4. Monitor your bot
- prometheus 

## Generate more text data

## Other usecase of chatbot

Searching for flights/jobs/hotels, report an incident to database, shopping.


 
