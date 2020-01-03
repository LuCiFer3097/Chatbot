import sys
responses={'hi':['Hello!','Hola!'],'how are you':['I am fine. Thank You',"I am doing well"],'who are you':['I am a very basic rule based chatbot designed to chat with you for a while.'],'what do you like':['You want to know about me. That is so sweet of you. Are you interested in me?'],'no':['Sad to hear that. Anyways I like to learn but I am unable to.'],'yes':['Very well. I like to learn but I am unable to.'],'why':['I am not designed to learn anything new. Anyways you want to ask something else?'],'suggest me some movies':['Do watch Endgame','I would recommend Shawshank Redemption','You can watch The Pulp Fiction'],'i have already watched it':['There are many more movies like The forrest Gump and Good Will Hunting to watch','You can also watch Interstellar','Then I would recommend The Shutter Island'],'who is your creator':['Wilson Patro created me. He should have made me more intelligent.'],'ok i will watch it':['It is nice to help you. Is there anything else you wanna ask me?'],'how is the weather today':['It is a sunny day','It might rain according to the weather report'],'bye':['It was nice talking to you. Bye!','Ok, come back soon. Bye!','See you later. Bye','All right then. Bye!!']}
common=['yes','no','why']
#List of queries we can ask to the bot
ques=["hi","how are you","who are you","what do you like?","yes","no","why","suggest me some movies","ok i will watch it","i have already watched it","how is the weather today","bye"]
# A dictionary to check whether any question is asked in a out of context way or not. If yes bot will have different answers.
counter={}
for i in responses:
	counter[i.lower().strip('?').strip('.')]=0

def chat():
	print("Support: Hello Sir, How may I help you?")
	W=input('W: ').strip('?').strip('.')
	while W not in responses:
		if W == '':
			break
		support=input('support: ').strip()
		W=input('W: ').strip('?').strip('.')
	return W