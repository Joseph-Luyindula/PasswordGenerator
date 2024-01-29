from string import ascii_letters, digits, punctuation
from random import randint

# tout les caractères utilisable (crts = caractères)
crts = ascii_letters+digits+punctuation

#gestion du  nombre de caractère du mot de passe 
print("Combien de caractère voulez-vous pour voutre mot de passe ? ")
correct = False
while correct == False:
	print("N.B : inscrivez en caractère compris entre 6 et 15 !!! """)
	try :
		nb = int(input(">>> "))
		if 6 <= nb <= 15:
			print("VALIDÉ ☑️")
			correct = True
	except :
		print("Entrez un nombre entier S.V.P")
	
	
# génération du mot de passe 
password = ""
for n in range(nb):
	 i = randint(0,len(crts))
	 crt = crts[i]
	 password += str(crt)

# affichage du mot de passe 
print(f"""-----------MOT DE PASSE-----------

mot de passe : {password}""")

	 
