questions = ["Do you like dogs?", "Do you like cats?", "Do you like cars?"]
user_answers = []
# positive_answers = ['y', 'yes','t','true']

firstName = input("What is your first name?\n>")
lastName = input("What is your last name?\n>")

user_answers.append(firstName.capitalize())
user_answers.append(lastName.capitalize())

for each_question in questions:
    user_answer = input(each_question + ' ')
    user_answer = user_answer.lower()

    user_answers.append(user_answer)

database_file = 'database.txt'

with open(database_file, 'a') as f:
    f.write(','.join(user_answers) + '\n')