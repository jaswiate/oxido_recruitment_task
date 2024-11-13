import os
from dotenv import load_dotenv
from openai import OpenAI

# by Jakub Świątek

def read_file(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return file.read()


def generate_html(file_name, prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": model_affirmation
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    html_code = completion.choices[0].message.content.replace("```", "").replace("html", "", 1)

    f = open(f"{file_name}.html", mode="w", encoding="utf-8")
    f.write(html_code)
    f.close()

    return html_code


if __name__=="__main__":
    load_dotenv()

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI(api_key=OPENAI_API_KEY)

    article = read_file("artykul.txt")

    model_affirmation = (
        "Jesteś specjalistą w tworzeniu artykułów z grafikami w HTML. "
        "W swojej odpowiedzi ogranicz się tylko do wypisania kodu html, "
        "żeby była gotowa do wpisania do pliku."
    )

    prompt_article = (
        f"Przeanalizuj treść oraz strukturę artykułu {article}."
        "Wyznacz miejsca w artykule, w których warto jest zamieścić zdjęcie i wymyśl co miałyby one przedstawiać."
        "Następnie stwórz kod html z podanego artykułu oraz zdjęć we wcześniej wyznaczonych przez"
        "siebie miejscach."
        "Korzystaj ze standardowych tagów dostepnych w html, wygenerowany kod docelowo znajdzie się"
        "między tagami <body> </body>, nie potrzebuje więc całej struktury pliku .html."
        "Zamieszczając obrazki użyj tagu <img> z atrybutami src='image_placeholder.jpg' oraz"
        "alt z dokładnym promptem do wygenerowania obrazków w odpowiedniej sekcji."
        "Zwróć uwagę, żeby prompt do generowania obrazów był jak najdokładniejszy."
        "Pod każdym obrazkiem dodaj podpis; skorzystaj w tym celu z tagów <figure> i <figcaption>."
        "Podpisy jak i prompty do generowania obrazów powinny być w języku polskim."
    )

    article_html_code = generate_html("artykul", prompt_article)

    prompt_template = (
        f"Na podstawie tego kodu html {article_html_code}"
        "Stwórz kod html szablonu do wklejenia wygenerowanego wcześniej artykułu."
        "Zadbaj o styl; nagłówki sekcji powinny być pogrubione i ciemno-fioletowe, oraz wyśrodkowane"
        "Zdjęcia powinny być lekko zaokrąglone na rogach i posiadać delikatną ciemno-fioletową obwódkę."
        "Podpisy pod zdjęciami powinny mieć mniejszy rozmiar czcionki niż tekst akapitu."
        "Przeskaluj wielkość obrazów do wysokości około 300px i wyśrodkuj je względem swoich podpisów."
        "Skorzystaj z czcionki Consolas."
        "Zastosuj na całej stronie jasno-fioletowe tło i zaaplikuj lekki boczny padding."
        "Między tagi <body></body> daj komentarz: 'Miejsce na wklejenie artykułu'"
    )

    template_html_code = generate_html("szablon", prompt_template)

    full_html = template_html_code.replace("<!-- Miejsce na wklejenie artykułu -->", article_html_code)

    f = open("podglad.html", mode="w", encoding="utf-8")
    f.write(full_html)
    f.close()
