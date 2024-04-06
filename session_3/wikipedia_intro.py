import wikipedia as wk

london = wk.page("London")
#print(london.content)

split_sentences = london.content.split(".")
sentences_with_population_substring=[]

for sentence in split_sentences:
    if("population" in sentence):
        sentences_with_population_substring.append(sentence)

print(sentences_with_population_substring)
