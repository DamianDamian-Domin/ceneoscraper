# ceneoscraper
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://www.ceneo.pl)

 |Składowa                |Selektor                                        |Nazwa zmiennej|
 |------------------------|------------------------------------------------|--------------|
 |opinia                  |li.js_product-reviev                            |
 |identyfikator opinii    |["data-entry-id"]                               |
 |autor                   |div-reviewer-name-line                          |
 |rekomendacja            |div.product-reviev-summary > em                 |
 |ocena                   |span.review-score-count                         |
 |treść opini             |p.product-review-body                           |
 |lista wad               |div.cons-cell > ul                              |
 |lista zalat             |div.pros - cell > ul                            |
 |przydatna               |button.vote-yes > ul                            |
 |nieprzydatna            |button.vote-no > ul                             |
 |data zakupu             |span.review-time > time:first-child["datatime"] |
 |data wystawienia        |span.review-time > time:nth-child(2)["datatime"]|
 ## Etap 2 - pobranie składowych pojedyńczej opinii
 - pobranie kodu strony z opiniami o konkrtneym produkcie
 - wyciągnięcie z kodu strony fragmentów odpowiadających poszczególbym opiniom
 - zapisanie do pojedyńczych zmiennych wartości poszczególnych składowych opinii