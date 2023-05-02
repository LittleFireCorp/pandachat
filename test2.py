import openai
openai.api_key = "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"


def list_engines():
    engines = openai.Engine.list()
    for engine in engines['data']:
        print(engine)
    return

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt, 
        max_tokens=100, 
        n=1, 
        stop=None, 
        temperature=0.7,
    )
    text = response.choices[0].text
    return text.strip()


# list_engines()
prompt = "Can you describe a Panda Bear? Write a children story about Pandas. 5 pages minimum"
print(prompt)
response = generate_text(prompt)
print("ZORGLUB")
print(response)
