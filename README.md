# Reddit-comment-bot
this is a reddit bot that reply's to the newest post when searching a chosen keyword. A use-case for this bot is for marketing a certain product or service. 

This bot creates a function called "Comment_on_posts" which consists of the keywords and message which are both declared variables that can be changed. The bot uses Pickle to collect the posts ID that the bot has commented on and compares it to other posts so the bot doesnt comment under the same post twice. The bot also uses time so that the bot can sleep during the function itself and in the infinite loop calling the functions. This bot has been written with the least amount of lines possible so it is very efficient. 
