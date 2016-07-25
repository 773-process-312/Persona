import time
from datetime import datetime, timedelta
import random
import OAuth
from Tweet_picker import RandamTweeter, A_Basket_Of_Users

t = OAuth.Create_Apps()

Persona = RandamTweeter(3, 5, 'combine')
Persona.Randomizer()

Persona = A_Basket_Of_Users(['verge','cnn'], 5, 'retweet')
Persona.Randomizer()


	