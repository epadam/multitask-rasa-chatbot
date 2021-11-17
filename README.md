# Multi-task Rasa Chatbot with Haystack

## Architecture

NLU --> Policy --> Action --> Database
                          
                          --> Other Services

## Multi-task
1. Chitchat with the bot
2. Ask questions about trends/sales or more information with the bot (using haystack as backend)
3. Searching for flights/jobs/hotels, report an incident to database

To develop a production level chatbot, here are some factors to consider.

1. Continual Learning with your bot
Use Rasa X to talk to your bot and identify incorrection prediction of the model and retrain the model

2. CI/CD for the bot

- How to test your with Github actions using GKE
- How to deploy your bot on GKE

3. Monitor the bot with prometheus 



## Channel for the bot:

Use ui.html to fast test your bot.

https://www.npmjs.com/package/@rasahq/rasa-chat
https://chat-widget-docs.rasa.com/?path=/docs/rasa-chat-widget--widget
https://rasa.com/docs/rasa/connectors/your-own-website/#chat-widget
https://github.com/JiteshGaikwad/Chatbot-Widget

## Haystack


## Need to be done

Action code:
1. information query(with haystack)
2. KG query
3. function usage like book a ticket
4. external services or human handoff



 
