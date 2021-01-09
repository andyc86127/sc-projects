"""
File: boggle.py
Name: Andy Chen
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
SIZE = 4

vocab = {}


def main():
	global vocab
	read_dictionary()
	while True:
		data = {}
		word_lst = []
		for y in range(SIZE):
			row = input(f'{y+1} row of letters: ').lower()
			row = row.split()
			if len(row) != SIZE or not valid_input(row):
				print('Illegal input')
				return
			# store every single letter in each row as dictionary {position coordinate: letter}
			for x in range(len(row)):
				data[(x, y)] = row[x]
		for key, value in data.items():
			vocab_lst = vocab[value]
			cur = []
			boggle(data, cur, word_lst, key, vocab_lst)
		print(f'There are {len(word_lst)} words in total.')


def boggle(data, cur, word_lst, start, vocab_lst):
	global vocab
	# to avoid choosing the position previous has chosen.
	if start in cur:
		return

	cur.append(start)
	sub_s = ''
	for ele in cur:
		sub_s += data[ele]  # current string based on the position coordinate.
	if not has_prefix(sub_s, vocab_lst):
		# Un-Chosen
		cur.pop()
		return
	else:
		# found a word
		if sub_s in vocab_lst and sub_s not in word_lst:
			word_lst.append(sub_s)
			print(f'Found: {sub_s}')
		# DFS
		if start[0] == 0:
			if start[1] == 0:
				boggle(data, cur, word_lst, (start[0]+1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0], start[1]+1), vocab_lst)	 # (x, y+1)
				boggle(data, cur, word_lst, (start[0]+1, start[1]+1), vocab_lst)  # (x+1, y+1)
			elif start[1] == SIZE-1:
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] - 1), vocab_lst)  # (x+1, y-1)
			else:
				boggle(data, cur, word_lst, (start[0] + 1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0], start[1] + 1), vocab_lst)  # (x, y+1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] + 1), vocab_lst)  # (x+1, y+1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] - 1), vocab_lst)  # (x+1, y-1)
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
		elif start[0] == SIZE-1:
			if start[1] == 0:
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0], start[1] + 1), vocab_lst)  # (x, y+1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] + 1), vocab_lst)  # (x-1, y+1)
			elif start[1] == SIZE-1:
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] - 1), vocab_lst)  # (x-1, y-1)
			else:
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0], start[1] + 1), vocab_lst)  # (x, y+1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] + 1), vocab_lst)  # (x-1, y+1)
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] - 1), vocab_lst)  # (x-1, y-1)
		else:
			if start[1] == 0:
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0], start[1] + 1), vocab_lst)  # (x, y+1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] + 1), vocab_lst)  # (x-1, y+1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] + 1), vocab_lst)  # (x+1, y+1)
			elif start[1] == SIZE-1:
				boggle(data, cur, word_lst, (start[0] + 1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] - 1), vocab_lst)  # (x-1, y-1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] - 1), vocab_lst)  # (x+1, y-1)
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
			else:
				boggle(data, cur, word_lst, (start[0] + 1, start[1]), vocab_lst)  # (x+1, y)
				boggle(data, cur, word_lst, (start[0] - 1, start[1]), vocab_lst)  # (x-1, y)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] - 1), vocab_lst)  # (x-1, y-1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] + 1), vocab_lst)  # (x+1, y+1)
				boggle(data, cur, word_lst, (start[0] + 1, start[1] - 1), vocab_lst)  # (x+1, y-1)
				boggle(data, cur, word_lst, (start[0] - 1, start[1] + 1), vocab_lst)  # (x-1, y+1)
				boggle(data, cur, word_lst, (start[0], start[1] - 1), vocab_lst)  # (x, y-1)
				boggle(data, cur, word_lst, (start[0], start[1] + 1), vocab_lst)  # (x, y+1)
		# Un-Chosen
		cur.pop()


def valid_input(row: list) -> bool:
	special_char = '@_!#$%^&*()<>?/\\|}{~:"\';:'
	for ele in row:
		if ele in special_char or ele.isnumeric():
			return False
	return True


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a dictionary (key = first letter
	and value = all the vocabularies start with key)
	"""
	global vocab
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			# Only the word whose length is larger that SIZE will be added in vocab.
			if len(line) >= SIZE:
				if line[0] in vocab:
					vocab[line[0]].append(line)
				else:
					vocab[line[0]] = [line]


def has_prefix(sub_s, vocab_lst):
	global vocab
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param vocab_lst: (lst) A list that contains all the vocabularies start with the first letter of sub_s
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ele in vocab_lst:
		if ele.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
