#Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module holding a function that asks the user how they are feeling today and responds with a custom message based on the mood entered. This function should then be imported and used in another file "main.py".

import mood_responses

mood = input("How are you feeling today?\n")
print(mood_responses.mood_response(mood))

print("Mood upliftment in progress::::")
print(mood_responses.mood_uplift(mood))


