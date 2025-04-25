import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """
Mude o texto da camiseta do cachorro para 'CACHORRUS' e do homem para 'MANUS'"
"""

result = client.images.edit(
    model="gpt-image-1",
    image=[
        open("minha_foto.png", "rb"),
    ],
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

# Save the image to a file
with open("minha_foto_alterada.png", "wb") as f:
    f.write(image_bytes)
