import random
from human import chat
# A Dictionary of queries with a list of choices for the bot to answer differently every time
responses={'hi':['Hello!','Hola!'],'how are you':['I am fine. Thank You',"I am doing well"],'who are you':['I am a very basic rule based chatbot designed to chat with you for a while.'],'what do you like':['You want to know about me. That is so sweet of you. Are you interested in me?'],'no':['Sad to hear that. Anyways I like to learn but I am unable to.'],'yes':['Very well. I like to learn but I am unable to.'],'why':['I am not designed to learn anything new. Anyways you want to ask something else?'],'suggest me some movies':['Do watch Endgame','I would recommend Shawshank Redemption','You can watch The Pulp Fiction'],'i have already watched it':['There are many more movies like The forrest Gump and Good Will Hunting to watch','You can also watch Interstellar','Then I would recommend The Shutter Island'],'who is your creator':['Wilson Patro created me. He should have made me more intelligent.'],'ok i will watch it':['It is nice to help you. Is there anything else you wanna ask me?'],'how is the weather today':['It is a sunny day','It might rain according to the weather report'],'bye':['It was nice talking to you. Bye!','Ok, come back soon. Bye!','See you later. Bye','All right then. Bye!!']}
common=['yes','no','why']
#List of queries we can ask to the bot
ques=["hi","how are you","who are you","what do you like?","yes","no","why","suggest me some movies","ok i will watch it","i have already watched it","how is the weather today","bye"]
# A dictionary to check whether any question is asked in a out of context way or not. If yes bot will have different answers.
counter={}
for i in responses:
	counter[i.lower().strip('?').strip('.')]=0
# Function for the human support to come and chat with the customer

# A Function for the chatbot
def bot():
	#Initial Instructions
	B="Hello!"
	print("These are the queries\n",ques)
	print("If you want to quit just press enter or type bye")
	print("Bot: " + B)
	while True:
		W=input('W: ').strip('?').strip('.')
		if W == '': # If nothing is entered it will exit 
			print("Bot: Bye!!")
			break
		if W.lower()=='bye': # You can even quit by typing bye
			print("Bot: " + random.choice(responses[W.lower().strip("?").strip(".")]))
			break
		if W=='1': # After confirming the query is correct press 1 for the customer support
			print("I think it is something which I cannot answer. Let me ask for help from someone")
			W=chat()
			if W=='':
				print("Bot: Hope your doubt is cleared. Bye!!")
				break
			else:
				print("Bot: Hey I am back. ")
		if W.lower().strip("?").strip(".") in responses:
			if counter["suggest me some movies"]==0 and (W.lower()=="i have already watched it" or W.lower()=="ok i will watch it"):
				print("Bot: " + "What have you already watched please give me some context")
			elif counter["what do you like"]==0 and (W.lower()=="yes" or W.lower()=="no"):
				print("Bot: " + "I didn't quite get you. What are you trying to say?")
			elif counter["yes"]==0 and counter["no"]==0 and W.lower()=="why":
				print("Bot: " + "It is not clear. Please Help me understand")
			elif counter[W.lower()]==0:
				print("Bot: " + random.choice(responses[W.lower()]))
				counter[W.lower()]=1
				if W.lower()=="yes" or W.lower()=="no":
					counter["what do you like"]=0
			elif W.lower() not in common and counter[W.lower()]>0:
				print("Bot: I think you have said this before. Anyways " + random.choice(responses[W.lower()]))
			elif counter[W.lower()]>0:
				print("Bot: I think you have said this earlier and you want to ask something else")
			
		
		if W.lower() not in responses: # Checking if the query doesn't contain any grammatical mistakes before going to the human support
			print("Bot: Kindly check for any error in your query. If it's perfectly fine please press 1")

bot()