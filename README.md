# Multi-task Rasa Chatbot

## Advantages of Rasa

1.Flexiable Architecture. TED Policy allows you to directly train end-to-end conversation, also for multi-turn conversation based on Attention mechnism

The basic architecture is as below:

Input -> intention and NER - (QA)  --> action policy -> encode the sentence -> retrieve -> reader -> return 
                           
                           - (task)--> action policy -> doing action -> return results
                           
                           - (KG)  --> action policy -> matching NER in KG -> data to text -> return
## When to use Rasa

1. task oriented chatbot
2. multi-turn conversation

## When you don't need Rasa

Single turn question without context like: 
  * simple FAQ chatbot
  * simple information retrieval


## Multi-task
1. Chitchat with the bot
2. Ask questions about covid-19 (using haystack as backend)
3. A demo that you can register for vacacine in chabot

## Actions :
1. information query(with haystack)
2. KG query
3. function usage like register for the vaccacine
4. other external services or human handoff

Rasa is becoming more end-to-end, check the blog:
 
https://rasa.com/blog/were-a-step-closer-to-getting-rid-of-intents/


## Channel for the bot:

Use ui.html to fast test your bot.

https://www.npmjs.com/package/@rasahq/rasa-chat
https://chat-widget-docs.rasa.com/?path=/docs/rasa-chat-widget--widget
https://rasa.com/docs/rasa/connectors/your-own-website/#chat-widget
https://github.com/JiteshGaikwad/Chatbot-Widget

### TTS and Voice to Text

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

## How to generate more text data

## Text Encryption

## Other usecase of chatbot

Searching for flights/jobs/hotels, report an incident to database, shopping.


 
