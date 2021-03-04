# Moduł z algorytmami rozwiązującymi równania różniczkowe

W repozytorium znajdują się pliki:
* numericalODE - główny plik modułu
* main - plik w którym jest przykładowe użycie modułu
* functions - plik przechowujący funkcje używane do pracy z modułem
* Tests - plik z przykładowymi testami 

numericalODE:
--------------
Składa się z klasy głównej RR i klas pchodnych Euler oraz RK4. Euler implementuje algorytm do rozwiązywania równań różniczkowych metodą Eulera. RK4 implementuje algorytm Rungego-Kutty czwartego rzędu rozwiązywania równań różniczkowych. Dodatkowo w module znajduj się klasa Blad.

Klasy składają sie z trzech metod:
* licz - służy do rozwiązywania równań różniczkowych, zwraca listę z wynikami oraz listę z punktami czasowymi
* licz_czas - służy do rozwiązywaia równań różniczkowych, zwraca ostatni wynik i czas potrzebny na obliczenia. Wyniki nie są zapisywane, więc liczony jest tylko czas potrzebny na obliczenia wyniku w danym punkcie.
* licz_uklad_rownan - słuzy do rozwiązywania układu równań różniczkowych. Zwaraca listę z wektorami oraz listę z punkami czasowymi.

Blad:
* licz_bezwzg - służy do obliczania błędu bezwzględnego
* licz_wzg - służy do obliczania błędu względngo
