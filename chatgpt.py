import openai


openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

def ask_chatgpt(question):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        n=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant with exciting, interesting things to say."},
            {"role": "user", "content": question},
        ])

    message = response.choices[0]['message']
    return message['content']


exit_chatgpt = 1

while(exit_chatgpt):

    user_input = input("\n\nAsk ChatGPT:\n\n")

    if user_input == "exit":
        exit_chatgpt = 0

    print(ask_chatgpt(user_input))

