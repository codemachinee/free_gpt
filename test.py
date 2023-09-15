import g4f


from g4f.Provider import (
    Aichat,
    Aivvm,
    CodeLinkAva,
    Vitalentum,
    Ylokh,
)

response = g4f.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role": "user", "content": 'Какие сегодня день, месяц и год?'}],
    provider=Aivvm,
    stream=False)

print(response)