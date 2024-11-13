# Oxido_recruitment_task
Aplikacja generująca stronę z treści artykułu za pomocą OpenAI api. 

## Część obowiązkowa
Na początek ładowane jest API_KEY ze zmiennej znajdującej się w pliku .env.
Potem aplikacja wczytuje klienta, treść arykułu i za pomocą modelu **gpt-4o** generuje plik *artykul.html* za pomocą podanego wcześniej promptu.

## Część dla chętnych
Na podstawie drugiego prompta, model generuje plik *szablon.html*, który zawiera wystylizowany szablon do wrzucenia tam treści pliku *artykuł.html*.
Oba pliki są łączone w całość zapisaną jako *podglad.html*. Podglad ładuje sobie obraz *image_placeholder.jpg*, natomiast w kodzie znajdują się atrybuty alt,
które zawierają szczegółowe prompty do generowania adekwatnych obrazów do akapitu.

### Jak uruchomić
Aplikacja korzysta z dwóch modułów *dotenv* oraz *openai*.
W celu zainstalowania zależności należy wykonać: 
```
pip install python-dotenv
```
```
pip install openai
```
Wywołanie programu:
```
python zadanie.py
```
Przed wywołaniem programy należy również stworzyć w folderze głównym plik **.env** i ustawić tam zmienną *OPENAI_API_KEY* na swój własny api key
