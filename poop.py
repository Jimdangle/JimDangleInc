import numpy as np 
import pandas as pd 


print("\nNEW RUN\n--------\n")


# takes in a single table, do not use this function
# just let URLtoArr do its thing if you can

def filterDftoArr(df_in):
	df_in = df_in.astype('str')

	og_arr = df_in.flatten()

	out_arr = []

	for word in og_arr:
		if len(word) > 1:
			out_arr.append(word)
		else:
			continue

	
	return out_arr


# @param: list of urls to sites with a table of words (will be converted to strings regardless)
# appends the overall array that is plugged in

def URLtoArr(urls, some_list):
	# checks to see if a table is on the page


	for links in urls:
		if len(pd.read_html(links)) < 0:
			print('Could not find a table on this link')
		else:
			print('Found link!')

			temp_df = pd.read_html(links)

			temp_df_first = temp_df[0].values

			out_arr = filterDftoArr(temp_df_first)

			some_list += out_arr

	








#adjectives array
adj_total = []

# first adj table
url_adj = "https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html"


# add links to this array and they will be added to the overall table)
adj_urls = [url_adj]

URLtoArr(adj_urls, adj_total)








# nouns


url_nouns = "https://eslgrammar.org/list-of-nouns/"
nouns = []

noun_urls = [url_nouns]

URLtoArr(noun_urls, nouns)





intros = ["A", "The", "The Life of a", "Enter the", "After the", "The Most", "Becoming the", "The Tale of the", "A song of", "In Lieu of The", "Harry Potter and The", "I Shat out a"]



running = True

while running:
	print("1. Generate Title \n2. Exit")
	inp = input("\n")
	if inp == '1':
		intro = intros[np.random.randint(len(intros))]
		adj = adj_total[np.random.randint(len(adj_total))]
		noun = nouns[np.random.randint(len(nouns))]

		output_str = intro + " " + adj + " " + noun
		print("\n Generated Name: " + output_str)
	else:
		running = False







