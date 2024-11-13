import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

with open("artykul.txt", mode="r", encoding="utf-8") as file:
    article = file.read()

client = OpenAI(api_key=OPENAI_API_KEY)

prompt = (
    f"Przeanalizuj treść oraz strukturę artykułu {article}."
    "Wyznacz miejsca w artykule, w których warto jest zamieścić zdjęcie"
    "i wymyśl co miałyby one przedstawiać."
    "Następnie stwórz kod html z podanego artykułu oraz zdjęć we wcześniej wyznaczonych przez"
    "siebie miejscach."
    "Korzystaj ze standardowych tagów dostepnych w html, wygenerowany kod docelowo znajdzie się"
    "między tagami <body> </body>, nie potrzebuje więc całej struktury pliku .html."
    "Zamieszczając obrazki użyj tagu <img> z atrybutami src='image_placeholder.jpg' oraz"
    "alt z dokładnym promptem do wygenerowania obrazków w odpowiedniej sekcji."
    "Zwróć uwagę, żeby prompt do generowania obrazów był jak najdokładniejszy."
    "Pod każdym obrazkiem dodaj podpis; skorzystaj w tym celu z tagów <figure> i <figcaption>."
    "W swojej odpowiedzi ogranicz się tylko do wypisania kodu html, żeby była gotowa do wpisania do pliku."
)


completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

html_code = completion.choices[0].message.content.replace("```", "").replace("html", "")

f = open("artykul.html", mode="w", encoding="utf-8")
f.write(html_code)
f.close()
