# Persona
This program can automate the tweeting based on randomization. It contains one that can be used with user interface and the other one with command line tools.

## OAuth
A module that can read your twitter account information before you can do any manipulation with other modules. You need to create an app on Twitter's dev page. See instructions in [sixohsix](https://github.com/sixohsix/twitter).

The Twitter API use the API developed by [sixohsix](https://github.com/sixohsix/twitter)

##Tweet Picker with user interface
It utilize Tkinter module in python to develope a usable interface that can show picture with text, after the randomization procedure. 

##Tweet Picker without user interface
It specializes in the service for users who want to run the automation around the clock/on the server. Potential timer feature would be added in.

##Tweet Sender
This module analyzes the options user put in, such as send new tweet or retweet an old tweet. Moreover, if the tweet is over 140 limit when you send it, this module would truncate it without losing the core meaning of the text, to satisfy the 140- character limit.

##Example
Please look up in the [main.py](https://github.com/flyws/Persona/blob/master/main.py)
