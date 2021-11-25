import re
import streamlit as st
import long_responses as long

st.title('ChatBot')


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # calculates the percentage of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses-----------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye', 'cya', 'later'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)

    # Long Responses-------------------------------------------------------------
    response(long.lr_eat, ['where', 'should', 'i', 'eat'], required_words=['eat', 'where'])
    response(long.lr_Advice, ['can', 'you', 'give', 'advice'], required_words=['give', 'advice'])
    response(long.lr_age, ['what', 'is', 'your', 'age'], required_words=['age', 'your'])
    response(long.lr_who, ['who', 'are', 'you'], required_words=['who'])
    response(long.lr_joke, ['tell', 'me', 'a', 'joke'], required_words=['joke'])
    response(long.lr_day, ['what', 'day', 'is', 'it', 'today'], required_words=['day'])
    response(long.lr_smart, ['do', 'you', 'get', 'smarter'], required_words=['smarter'])
    response(long.lr_lang, ['which', 'language', 'do', 'you', 'speak'], required_words=['language'])
    response(long.lr_date, ['what', 'date', 'is', 'it', 'today'], required_words=['date'])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
name = st.text_input('Enter your name')
while name:
    st.text('Welcome ' + name)
    name = False

ip = st.text_input('you: ')
record = []

while ip:
    chat = get_response(ip)
    st.write('bot: ' + chat)
    record.append(chat)
    ip = False

