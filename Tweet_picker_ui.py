import OAuth
import twitter
from Tkinter import *
from urllib2 import urlopen
from PIL import Image, ImageTk
from StringIO import StringIO
import random
from Tweet_sender import TweetSender

# user_name = raw_input('Enter the username of which timeline to be seen:')


class Application(Frame):
    def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Enter', command=self.RandomPicker)
        self.alertButton.pack()

    def RandomPicker(self):
        # Change text and create a new "send" button
        if self.alertButton['text'] == 'Enter':
            self.alertButton['text'] = 'Update'
            self.CreateUI()

            send_handler = TweetSender(self.nameInput.get(),j)
            # use lambda to avoid function's auto-execution
            self.alertButton2 = Button(self, text='Send', 
                command=lambda: send_handler.send())
            self.alertButton2.pack()
        # Update the tk label when "update" button is pressed
        elif self.alertButton['text'] == 'Update':
            self.update()
            # Refresh the TweetSender's parameter
            send_handler = TweetSender(self.nameInput.get(),j)
            self.alertButton2['command'] = lambda: send_handler.send()

    def CreateUI(self):
        # global names to be used in update()
        global TweetLabel, j, photo
        # generate a random index
        num = t.statuses.user_timeline(screen_name=self.nameInput.get())
        j = random.choice(list(range(0,len(num)))) 
        i = num[j]
        try:
            url = i['extended_entities']['media'][0]['media_url']
            file = urlopen(url)
            # convert to a file-like object using StringIO
            image = Image.open(StringIO(file.read()))
            image = image.resize((250,250))
            photo = ImageTk.PhotoImage(image)

            TweetLabel = Label(self,text=i['text'],image=photo, 
                                compound=BOTTOM,wraplength=400,justify='left',anchor='w')
            # Keep an index to avoid garbage collection mechanism in python
            TweetLabel.photo = photo
            TweetLabel.pack()

        # If there's no photo in the tweet
        except:
            photo = ''
            TweetLabel = Label(self,text=i['text'],wraplength=400,justify='left',
                                anchor='w',image = photo,compound=BOTTOM)
            TweetLabel.pack()

    def update(self):
        global j
        num = t.statuses.user_timeline(screen_name=self.nameInput.get())
        j = random.choice(list(range(0,len(num)))) 
        i = num[j]
        try:
            url = i['extended_entities']['media'][0]['media_url']
            file = urlopen(url)

            # convert to a file-like object using StringIO
            image = Image.open(StringIO(file.read()))
            image = image.resize((250,250))
            photo = ImageTk.PhotoImage(image)

            # update the text and image
            TweetLabel['text'] = i['text']
            TweetLabel['image'] = photo
            TweetLabel.photo = photo
            TweetLabel.pack()

        except:
            TweetLabel['text'] = i['text']
            TweetLabel['image'] = ''
            TweetLabel.pack()


if __name__ == '__main__':
	# for i in t.statuses.user_timeline(screen_name=user_name)[0:9]:
	# 	print i['text'].encode('utf-8')
	# 	print '--------------------'
    t = OAuth.Create_Apps()
    a = Application()
    a.mainloop()