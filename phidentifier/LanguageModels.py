import os
from encodings.aliases import aliases
from . import Markov
import importlib.resources

model_cebuano = Markov.MarkovChain(importlib.resources.open_text('phidentifier.data.processed', 'cebuano.txt', encoding='utf8'), 'Cebuano')
model_kapampangan = Markov.MarkovChain(importlib.resources.open_text('phidentifier.data.processed', 'kapampangan.txt', encoding='utf8'),'Kapampangan')
model_pangasinan = Markov.MarkovChain(importlib.resources.open_text('phidentifier.data.processed', 'pangasinense.txt', encoding='utf8'), 'Pangasinan')




models = []
models.append(model_cebuano)
models.append(model_kapampangan)
models.append(model_pangasinan)