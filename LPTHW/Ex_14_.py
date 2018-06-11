<<<<<<< HEAD
from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
18 Alright, so you said {likes} about liking me.
19 You live in {lives}. Not sure where that is.
20 And you have a {computer} computer. Nice.
21 """)
=======
from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)
print(f"Where do you live {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)
print(f"""
18 Alright, so you said {likes} about liking me.
19 You live in {lives}. Not sure where that is.
20 And you have a {computer} computer. Nice.
21 """)
>>>>>>> e098262d7bc0c5023aab1e18d9bedf7f221006de
