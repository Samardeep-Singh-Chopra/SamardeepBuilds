from openai import OpenAI

# Paste your NVIDIA API key here
API_KEY = "your_nvidia_api_key_here"

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)

# Paste any text you want summarized here
text = """
NASA's Artemis program aims to return humans to the Moon by 2026. 
The program includes the Space Launch System rocket, the Orion spacecraft, 
and the Lunar Gateway space station. NASA is working with commercial partners 
including SpaceX and Blue Origin for lunar landers. The total estimated cost 
of the program is over $90 billion. The first crewed lunar landing since Apollo 17 
in 1972 will include the first woman and first person of color on the Moon. 
International partners including ESA, JAXA, and CSA are contributing modules 
and astronauts to the mission. The program faces technical and budget challenges 
but remains a central priority for NASA through the end of the decade..
"""

print("\n⏳ Sending to AI...\n")

response = client.chat.completions.create(
    model="meta/llama-3.1-8b-instruct",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant that summarizes text clearly and concisely."
        },
        {
            "role": "user",
            "content": f"Summarize the following text in 5 clear bullet points:\n\n{text}"
        }
    ],
    temperature=0.5,
    max_tokens=500
)

print("✅ SUMMARY:\n")
print(response.choices[0].message.content)
print("\n--- Powered by NVIDIA NIM + Llama 3 ---")