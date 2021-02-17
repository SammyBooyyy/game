import random
import time
pc = ['pedra', 'papel', 'tesoura']
escolhas_pc = (random.choice(pc))
escolhas_user = input('Escolhe um dos objetos: pedra, papel ou tesoura > ')

if escolhas_pc == "user":
	print('O pc está a pensar, por favor espera:')
	time.sleep(3)
	print(f'Tu escolheste {escolhas_user} e o pc também escolheu {escolhas_pc}, então é um impate')
elif escolhas_user == "pedra":
	print('O pc está a pensar, por favor espera:')
	time.sleep(3)
	if escolhas_pc == "tesoura":
		print(f'Tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} então torna-te a ti o vencedor')
	else:
		print(f'O PC ganhou de ti, tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} ')
elif escolhas_user == "tesoura":
	print('O pc está a pensar, por favor espera:')
	time.sleep(3)
	if escolhas_pc == "papel":
		print(f'Tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} então torna-te a ti o vencedor')
	else:
		print(f'O PC ganhou de ti, tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} ')
else:
	print('O pc está a pensar, por favor espera:')
	time.sleep(3)
	if escolhas_pc == "tesoura":
		print(f'Tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} então torna-te a ti o vencedor')
	else:
		print(f'O PC ganhou de ti, tu escolheste {escolhas_user} e o pc escolheu {escolhas_pc} ')