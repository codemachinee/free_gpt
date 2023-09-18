import g4f
import random

provider_list = [g4f.Provider.CodeLinkAva, g4f.Provider.Ails, g4f.Provider.Bing, g4f.Provider.ChatBase,
                 g4f.Provider.ChatgptAi, g4f.Provider.DeepAi, g4f.Provider.H2o, g4f.Provider.Wewordle]


# Automatic selection of provider

# streamed completion
def gpt():
    global provider_list
    try:
        response = g4f.ChatCompletion.create(
            model=g4f.models.default,
            messages=[{"role": "user", "content": "Hello, How are you?"}],
            provider=random.choice(provider_list),
            stream=False
            )
        print(response)
    except Exception:
        gpt()


gpt()


