# Zadanie 5

## 1. Różnice między deweloperką a produkcją

* **Dane:** Podczas nauki używamy gotowych plików (np. CSV). W produkcji dane płyną na bieżąco od użytkowników i mogą zawierać błędy, braki lub mieć zupełnie inny format.
* **Błędy:** Jeśli na komputerze skrypt się wywali, po prostu go poprawiamy. Na produkcji błąd modelu może oznaczać, że cała aplikacja przestanie działać.
* **Środowisko:** Na serwerze może być inny system lub inna wersja Pythona, co może powodować błędy (tzw. problem "u mnie działa").

## 2. Wyzwania produkcyjne?

1. **Monitorowanie modelu:** Trzeba sprawdzać, czy model po miesiącu nadal dobrze przewiduje. Jeśli skuteczność spada, musimy o tym wiedzieć jak najszybciej.
2. **Ponowne trenowanie:** Co jakiś czas musimy douczyć model na nowych danych, które zebraliśmy od użytkowników, aby "był na bieżąco".
3. **Zarządzanie zależnościami:** Używamy plików typu `requirements.txt` lub narzędzi takich jak Docker, aby mieć pewność, że na serwerze zainstalują się dokładnie te same wersje bibliotek, na których trenowaliśmy model.

## 3. Wersjonowanie modelu

**Kiedy podnosimy wersję modelu?**
* Gdy nauczymy model na większej ilości danych.
* Gdy zmienimy algorytm na inny (np. z Regresji na Las Losowy), bo daje lepsze wyniki.
* Gdy zmienimy ustawienia modelu (hiperparametry), żeby poprawić jego celność.