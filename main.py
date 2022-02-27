# Tratamento de dados
def process_data(current_data):
	clear_data = []
	for i in txtOpenDocument: #lines
		current_line = i.split(' ')
		for j in current_line:
			if j != '\n':
				clear_data.append(j)#words
	
	return clear_data
			
# Variáveis de controle
current_token_list = [] 
words_accepted_char = ['IF', 'FOR', 'THEN', 'ELSE']
txtOpenDocument = open("testText.txt")
txtOpenDocument = txtOpenDocument.readlines()
current_data = process_data(txtOpenDocument)

# Definição da classe Token
class Token:
	def __init__(self, identifier, value):
		self.identifier = 	identifier
		self.value =		value

# Exercicio 2

def verify_letter_index(current_inputed_char_to_compare):
	for i in words_accepted_char:
		if current_inputed_char_to_compare.lower() == i.lower():
			return i
	return ''

def getToken(current_inputed_char):
	current_token = verify_letter_index(current_inputed_char)
	
	if current_token:
		return Token(current_token, current_inputed_char.lower())

	return ''
	
while True:
	if len(current_data):
		for current_word in current_data:
			token = getToken(current_word)
			if token != '':
				current_token_list.append(token)
	
	for token in current_token_list:
		print(token.identifier, token.value)
	break