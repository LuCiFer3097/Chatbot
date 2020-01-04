# Chatbot
A simple rule based chat bot using python. It can also be switched to human support if the bot is not able to answer the queries.
## Dependencies
  - This program can be run on Windows and Linux.
  - Programming language used is Python 3.8
## Steps to install gnome terminal
  sudo apt-get install --reinstall gnome-terminal
## Steps to install python3.8 on Linux
  - sudo apt-get install build-essential checkinstall
  - sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
  - cd /opt
  - sudo wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
  - sudo tar xzf Python-3.8.0.tgz
  - cd Python-3.8.0
  - sudo ./configure --enable-optimizations
  - sudo make altinstall
  - _As you have not overwritten the default Python version on the system, So you have to use Python 3.8 as follows:_
  - python3.8 -V
## Instructions
  - Kindly make sure you have the latest python version i.e. 3.8 as the format in which the split function is used will throw                   an error in previous verisons.
  - To execute run the following command 
    - **python3.8 chatbot.py**
  - Here is the list of the queries you can ask the chatbot
    - hi
    - how are you
    - who are you
    - what do you like
    - suggest me some movies
    - I have already watched it
    - ok I will watch it
    - how is the weather today
    - who is your creator
    - bye
   - Here are some responses which you can give if the bot asks you something
      - yes
      - no
      - why
   - If you have entered something which is not in the list of queries the bot will first confirm with you whether it is a right query or not if it is right it will ask you to press 1 to go to the human support. 
   - The bot is designed to answer differently for different sequences in which the questions will be asked
   - For example if you query I have watched it without asking suggest me some movies, it will have a different answer.
   - If some query is asked outside from these queries the bot will first confirm then it will shift the control to a human support who        will then interact with the customer.
   - As soon as the customer asks something from within the queries the controls will be shifted autromatically to the bot.
   
 ## Two points worth mentioning.
    - If you run Chatbot1.py you will get human support and the bot in different terminals but as soon as the terminals are switched the prev data is lost. In short, it will be like talking to a new chatbot every time. But you can switch between the chatbot and human support as many times as you want. You will get it when you run the code.
    - If you run chatbot.py you can all the prev tasks and human support will be in a different terminal and the prev data will not be lost. It is like going back to the same bot. Please ignore the error which comes after everything is executed and you close the program. It will not affect the program. It is because of the fact I am forcefully keeping the terminal open. Keeping the terminal open is a tedious process and the next time it switches back to the original bot terminal it doesn't have the address of the process and that's why the error is thrown. I am searching for a way to fix it but it will not affect the program.

