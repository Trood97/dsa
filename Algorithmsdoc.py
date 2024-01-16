import collections

#1. Reverse integer:

def input(x):
	string = str(x)
	if string.startswith('-'):
		return '-'+string[:-len(string):-1]
	else:
		return string[::-1]
#print(input(-234))

######################

#2. Average word length

string1 = 'Anand is a guy'

def avgwordlen(str1:str):
	for p in ',.!':
		str1 = str1.replace(p,'')

	words = str1.split()           #returns a list
	return round((sum(len(word) for word in words)/len(words)),2)

#print(avgwordlen(string1))


############################

#3.Add two numbers in a string
def addstrings(num1:str,num2:str):
	n1, n2 = 0,0
	m1,m2= 10**(len(num1)-1),10**(len(num2)-1),        #places found, no.of digits in number

	for p in num1:
		n1 +=(ord(p)-ord('0'))*m1        #
		m1 = m1//10

	for q in num2:
		n2 +=(ord(q)-ord('0'))*m2
		m2 = m2//10

	return n1+n2

#print(addstrings('236','44'))

############################

#4.Returning first non-rep index of a string
class NonrepIndex:
	def nonrepindex(self,string1: str):
		dict_count = {}
		str1 = string1.lower()
		for i in str1.lower():
			if i not in dict_count:
				dict_count[i] = 1
			else:
				dict_count[i] += 1

		for i in range(len(str1)):
			if dict_count[str1[i]] == 1:
				return i
			else:
				pass

		return -1  # if there no unique character in a string.

	def nonrepindex2(self,string1: str):
		count = collections.Counter(string1.lower())

		for index, ch in enumerate(string1.lower()):
			if count[ch] == 1:
				return index
			else:
				pass
		return -1

############################

#5.Determining valid pallindrome or not,  by deleting one character of a string
def validpallindrome(a):
	for i in range(len(a)):
		comp_string = a[:i] + a[i+1:]         #[:i] will be ignored
		if comp_string == comp_string[::-1]:
			return True

	return False

#6.Determing whether the array is monotonic or not.
def monotonic_array(list1):
	return ((all(list1[i]>= list1[i+1] for i in range(len(list1)-1))) or
	        (all(list1[i] <= list1[i+1] for i in range(len(list1)-1))))

#7.Moving zeroes to the end in a list
def movezeroes(array:list):
	for i in array:
		if i==0:
			array.remove(i)
			array.append(i)
	return array

#8.Fill in the blanks with the most recent value (not None)
def fillin(array:list):
	valid = 0
	res = []
	for i in array:
		if i is not None:
			res.append(i)
			valid = i
		else:
			res.append(valid)

	return res

#9. Matched and Mismatched words

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def matchandmismatch(sentence1,sentence2):
	s1 = set(sentence1.split())
	s2 = set(sentence2.split())

	return sorted(list(s1^s2)),sorted(list(s1&s2))


#10. Prime numbers of the numbers n

def primenumbers(num:int):
	primelist = []
	for i in range(num):
		if i >1:
			for j in range(2,i):
				if (i%j)==0:
					break
			else:
				primelist.append(i)

	return (primelist)