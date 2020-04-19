#import bibliotek
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
#import matplotlib.pyplot as plt

#wyświetlenie zawartości katalogu opinions_json
input_directory = "ceneoscraper/opinions_json"
print(*os.listdir(input_directory))

#wczytanie identyfikatora produktu, którego opinie będą analizowane
product_id = input("Podaj identyfikator produktu: ")

#wczytanie do ramki danych opini o pojedynczym produkcie
opinions = pd.read_json(input_directory+"/"+product_id+".json")
opinions = opinions.set_index("opinion_id")

average_score = round(opinions.stars.mean(),2)
pros = opinions.pros.count()
cons = opinions.cons.count()

stars = opinions.stars.value_counts()


print(pros,cons,stars)

