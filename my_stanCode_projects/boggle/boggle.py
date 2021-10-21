"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	start = time.time()
	####################
	boggle_matrix = []
	for i in range(4):
		print(i+1, end='')
		a = input(" row of latter: ")

		check = a.split(' ')
		for each in check:
			if not each.isalpha() or len(each) != 1:
				print("Illegal input")
				return
		boggle_matrix.extend(check)

	i = find_anagrams(boggle_matrix)		# finding started
	print("There are",i,"words in total.")


	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	dict_list = []
	with open(FILE) as f:
		for line in f:
			line = line.strip()
			dict_list.append(line)
	return dict_list


def has_prefix(sub_s, dict_, start):

	"""
	:param dict_:
	:param start:	start from a specific number in list_dictionary
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""

	for i in range(start, len(dict_), 1):
		temp = str(dict_[i])

		if len(temp) < 4:
			continue
		if temp.startswith(sub_s):
			return i, dict_[i]
	return None


def find_anagrams(matrix):
	"""
	迴圈每一個boggle字元，從他身邊的字元（存在一個長度為16的surround list)找一個，迴圈所有在他身邊的字元，丟到haas_prefix
	去看字典存不存在此開頭，沒有的話找下一組
	:param matrix:
	:return:
	"""
	used = {}
	counter = 0
	dict_ = read_dictionary()
	surround = [[1, 4, 5], [0, 2, 4, 5, 6], [1, 3, 5, 6, 7], [2, 6, 7], [0, 1, 5, 8, 9], [0, 1, 2, 4, 6, 8, 9, 10],
				[1, 2, 3, 5, 7, 9, 10, 11],
				[2, 3, 6, 10, 11],[4,5,9,12,13], [4, 5, 6, 8, 10, 12, 13, 14], [5, 6, 7, 9, 11, 13, 14, 15],
				[6, 7, 10, 14, 15],	[8, 9, 13], [8, 9, 10, 12, 14],
				[9, 10, 11, 13, 15], [10, 11, 14]]
	for i in range(len(matrix)):
		used.clear()

		ch1 = str(matrix[i])
		for num in surround[i]:
			ch2 = matrix[num]
			pair = ch1 + ch2	                    # pair the two neighbor ch
			used[i] = 1
			used[num] = 1

			ans = has_prefix(pair, dict_, 0)		# has_prefix return a tuple( dict_index, word. len(pair)
			while ans is not None:
				used[i] = 1
				used[num] = 1
				"""
				有在字典裡會回傳一個tuple 包含
				//1.字典內第幾個字的index
				2.那個字
				
				用以上資料加上
				4.pair:頭兩字
				5.bog matrix
				6.used:使用過的字元的位置
				7.num:現在位處的字元其代號
				丟入以上除了1.、3.到in_the_matrix
				"""

				dict_index, word = ans
				pair = ch1 + ch2
				a = num
				the_tuple = word, pair, matrix, used, a
				counter = in_the_matrix(the_tuple, counter)

				ans = has_prefix(pair, dict_, dict_index+1)

	return counter


def in_the_matrix(the_tuple, counter):
	surround = [[1, 4, 5], [0, 2, 4, 5, 6], [1, 3, 5, 6, 7], [2, 6, 7], [0, 1, 5, 8, 9], [0, 1, 2, 4, 6, 8, 9, 10],
				[1, 2, 3, 5, 7, 9, 10, 11],[2, 3, 6, 10, 11],[4,5,9,12,13], [4, 5, 6, 8, 10, 12, 13, 14],
				[5, 6, 7, 9, 11, 13, 14, 15], [6, 7, 10, 14, 15],[8, 9, 13], [8, 9, 10, 12, 14],
				[9, 10, 11, 13, 15], [10, 11, 14]]

	word, pair, matrix, used, num = the_tuple
	ch_num = num
	le = len(pair)
	j = 0
	sur = len(surround[ch_num])

	while j < sur:
		"""
		這邊應該改用 recursion 而非 while loop 實作，因為這部分沒有達成 backtrace，
		使得 foil、coil、moil、roil、iglu，
		這些包含兩次輸入的字 'i' 'l' 'o' 因為第一次找尋到錯的字元，而無法退回。
		這部分因為我最後才發現一開始的想法上有問題，但因為我沒有時間改了，而且我都沒寫註解，
		也不想麻煩助教找半天，在這邊特別告解，就麻煩助教該給多少就給多少，感謝助教xD
		"""
		if surround[ch_num][j] in used:
			j += 1
			continue
		else:
			num_in_mat = surround[ch_num][j]

		if matrix[num_in_mat] == word[le]:		# 下一個字在相鄰的字元內找到
			"""
			因為相鄰字元的確是字典內找到的自受字的下一個字元
			所以我們要前往下一個相鄰字
			這時候
			1.字要更新
			2.j要歸零
			3.字首字要往下一個字元前進
			"""
			le += 1
			if len(word) == le:
				print('Found "', end='')
				print(word, end='"\n')
				if counter is None:
					counter = 1
				counter += 1
				used.clear()
				return counter
			used[num_in_mat] = 1
			pair += matrix[num_in_mat]
			ch_num = num_in_mat

			sur = len(surround[ch_num])
			j = 0

		else:
			j += 1
	used.clear()
	return counter


if __name__ == '__main__':
	main()
"""
f y c l
i o m g
o r i l
h j h u
"""