import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

img = client.images.generate(
    model="gpt-image-1",
    prompt="Um homem com uma camiseta escrita 'JUNIN' e um cachorro com uma camiseta escrita 'IMG'",
    n=1,
    #size="1024x1024"
    size="1536x1024"
)

image_bytes = base64.b64decode(img.data[0].b64_json)
with open("minha_foto.png", "wb") as f:
    f.write(image_bytes)
