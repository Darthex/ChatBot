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
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

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
