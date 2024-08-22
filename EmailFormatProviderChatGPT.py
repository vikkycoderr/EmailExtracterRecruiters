import openai

openai.api_key="your API key"
def getChatResponse(company):
    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": "In Jane Doe format please provide me most common email format for "+company+". Please only provide email format with no extra content."}
        ],
    )

    answer = response.choices[0].message.content
    return answer