import g4f
import random

provider_list = [g4f.Provider.Aichat, g4f.Provider.Aivvm, g4f.Provider.CodeLinkAva, g4f.Provider.Vitalentum,
                 g4f.Provider.Ylokh]


# Automatic selection of provider

# streamed completion
def gpt():
    global provider_list
    try:

        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo,
            messages=[{"role": "user", "content": "Hello world"}],
            provider=random.choice(provider_list),
            stream=False
        )
        print(response)
    except Exception:
        gpt()


gpt()


