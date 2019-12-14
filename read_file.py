firstNameIndex = 0
lastNameIndex = 1
answersIndex = 2

positive_answers = ['y', 'yes','t','true']
negative_answers = ['n', 'no', 'f', 'false']

database_file = 'database.txt'

try:
    data_file = open(database_file, 'r')

    for each_data in data_file:
        each_data = each_data.split(',')

        firstName = each_data[firstNameIndex]
        lastName = each_data[lastNameIndex]
        user_answers = each_data[answersIndex:]

        for each_answer in user_answers:
            print(firstName + ' ' + lastName + ' said: ' + ('yes' if each_answer in positive_answers else 'no' if each_answer in negative_answers else each_answer) + '!')
        print()
except IOError as err:
    print('There was an error: ' + str(err))
finally:
    data_file.close()