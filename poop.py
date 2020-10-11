import numpy as np 
import pandas as pd 


print("\nNEW RUN\n--------\n")

tolerance = 3


# takes in a single table, do not use this function
# If you want to change the minimum length requirement change the 'tolerance' variable


def filterDftoArr(df_in):
	df_in = df_in.astype('str')

	og_arr = df_in.flatten()

	out_arr = []

	for word in og_arr:
		if len(word) > tolerance:
			out_arr.append(word)
		else:
			continue

	
	return out_arr


# @param: list of urls, array for words to be added to
# appends the overall array that is plugged in
# @return void

def URLtoArr(urls, some_list):
	# checks to see if a table is on the page


	for links in urls:
		if len(pd.read_html(links)) < 0:
			print('Could not find a table on this link')
		else:
			print('Found link! : (' + links+") \n")

			temp_df = pd.read_html(links)

			temp_df_first = temp_df[0].values

			out_arr = filterDftoArr(temp_df_first)

			some_list += out_arr

	








#adjectives

adj_total = []

# first adj link
url_adj = "https://grammar.yourdictionary.com/parts-of-speech/adjectives/list-of-adjective-words.html"


# add links to this array and they will be added to the overall table)
adj_urls = [url_adj,"https://www.enchantedlearning.com/wordlist/adjectives.shtml"]
URLtoArr(adj_urls, adj_total)








# nouns
#link stored as variable
url_nouns = "https://eslgrammar.org/list-of-nouns/"

# general nouns array 
nouns = []

# put links to websites with <table> elements you want in the general array
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







