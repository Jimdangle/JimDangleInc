import numpy as np 
import pandas as pd 


print("\nNEW RUN\n--------\n")



def testDFToArr(df_in):
	df_in = df_in.astype('str')
	mask = df_in.str.len()>1
	df_in = df_in.loc[mask]

	out_arr = df_in.flatten()
	
	return out_arr



#adjectives

url_adj = "https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html"
df_adj = pd.read_html(url_adj)

adj_col1 = df_adj[0][0]
adj_col2 = df_adj[0][1]
adj_col3 = df_adj[0][2]
adj_col4 = df_adj[0][3]

adj_test = df_adj[0].values

adj_test = testDFToArr(adj_test)

print(adj_test)

adjectives = []



for word in adj_col1:
	if len(word) < 3:
		continue
	else:
		adjectives.append(word)

for word in adj_col2:
	if len(word) < 3:
		continue
	else:
		adjectives.append(word)

for word in adj_col3:
	if len(word) < 3:
		continue
	else:
		adjectives.append(word)

for col in adj_col4:
	if len(col) < 3:
		continue
	else:
		adjectives.append(col)


print(len(adjectives))



# nouns

url_nouns = "https://eslgrammar.org/list-of-nouns/"
df_nouns = pd.read_html(url_nouns)
nouns = []

noun_col1 = df_nouns[0][0]
noun_col2 = df_nouns[0][1]
noun_col3 = df_nouns[0][2]

for noun in noun_col1:
	nouns.append(noun)

for noun in noun_col2:
	nouns.append(noun)

for noun in noun_col3:
	nouns.append(noun)

nouns.reverse()

nouns.remove(nouns[0])

print("\n\n")





intros = ["A", "The", "The Life of a", "Enter the", "After the", "The Most", "Becoming the", "The Tale of the", "A song of", "In Lieu of The", "Harry Potter and The", "I Shat out a"]



running = True

while running:
	print("1. Generate Title \n2. Exit")
	inp = input("\n")
	if inp == '1':
		intro = intros[np.random.randint(len(intros))]
		adj = adjectives[np.random.randint(len(adjectives))]
		noun = nouns[np.random.randint(len(nouns))]

		output_str = intro + " " + adj + " " + noun
		print("\n Generated Name: " + output_str)
	else:
		running = False







