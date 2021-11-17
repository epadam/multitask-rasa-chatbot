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



## Frontend for the bot:


## Haystack


## Need to be done

- Switch to human service


 
