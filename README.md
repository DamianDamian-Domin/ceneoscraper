# ceneoscraper
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)

 |Składowa                |Selektor                                        |Nazwa zmiennej|
 |------------------------|------------------------------------------------|--------------|
 |opinia                  |li.js_product-reviev                            |opinion       |
 |identyfikator opinii    |["data-entry-id"]                               |opinion_id    |
 |autor                   |div-reviewer-name-line                          |author        |
 |rekomendacja            |div.product-reviev-summary > em                 |recommendation|
 |ocena                   |span.review-score-count                         |stars         |
 |treść opini             |p.product-review-body                           |content       |
 |lista wad               |div.cons-cell > ul                              |cons          |
 |lista zalat             |div.pros - cell > ul                            |pros          |
 |przydatna               |button.vote-yes > ul                            |usefull       |
 |nieprzydatna            |button.vote-no > ul                             |useless       |
 |data zakupu             |span.review-time > time:first-child["datatime"] |purchase_date |
 |data wystawienia        |span.review-time > time:nth-child(2)["datatime"]|opinion_date  |
 ## Etap 2 - pobranie składowych pojedyńczej opinii
 - pobranie kodu strony z opiniami o konkrtneym produkcie
 - wyciągnięcie z kodu strony fragmentów odpowiadających poszczególbym opiniom
 - zapisanie do pojedyńczych zmiennych wartości poszczególnych składowych opinii
 ## Etap 3 - pobranie wszystkich opini o pojedynczym produkcie
 - zapisanie do złożonej struktury danych składowych wszystkich opini z pojedynczej strony
 - przechodzenie po kolejnych stronach
 - zapis wszystkich opinii o pojedynczym produkcie do pliku
 ## Etap 4
 - transformacja i wyczyszczenie danych
 - refaktorin kodu
 - parametryzacja