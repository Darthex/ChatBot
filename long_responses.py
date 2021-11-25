import random

lr_Advice = 'I am not an expert at giving advices, maybe you should ask the internet'
lr_eat = 'You should check the map!, there are some yummy restaurants nearby'
lr_age = 'I am a bot, i do not age, but my owners are fairly young'
lr_who = 'I am your friendly neighbourhood CHATBOT!!, i am here to listen to all your ramblings'
lr_joke = 'I was playing chess with my friend and he said, “Let’s make this interesting." ' \
          '         So we stopped playing chess.'
lr_day = 'Its Thursday today'
lr_smart = 'I am not infused with Ai right now, but i am fairly confident about my intelligence'
lr_lang = 'I am fluent in English and sarcasm'


def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]
    return response

