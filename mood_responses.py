 # mood_responses.py
def mood_response(mood):
    # Implement your response logic here
    return mood_display(mood)

#just extra display method called internally from mood display method
def mood_display(mood_inp):
    if mood_inp == 'happy':
        return("Yaay,That's great to hear!")
    elif mood_inp == 'sad':
        return("I hope your daygets better! Good luck!!")
    elif mood_inp == 'excited':
        return("I am soo excited, Looking forward to an eventful day!!")
    else: 
        #for all other inputs
        return("Stay Blessed Always and Enjoy your life")

# simple extra method - functionality
def mood_uplift(mood_info):
    if mood_info == 'happy':
        return("Awesome you are all good!!")
    elif mood_info == 'sad':
        return("Cheer up,your day wwill get better!")
    elif mood_info == 'excited':
        return("Looking forward to the exciting day!!")
    else: 
        #for all other inputs
        return("You are capable of achieving everyting in life!! Go ahead!!")
    pass
