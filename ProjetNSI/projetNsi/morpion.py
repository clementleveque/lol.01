def init ()  -> list :
	L1 = [0, 0, 0]
	L2 = [0, 0, 0]
	L3 = [0, 0, 0]
	return [L1, L2, L3]
	
def affichage (tableau : list ) -> list :
	n = len (tableau)
	for i in range (n) :
		print(tableau[i])
	
def demande (numeroJoueur : int ) -> list :
	if numeroJoueur == 1 :
		print ('Au tout du joueur 1 ! ')
	else :
		print ('Au tout du joueur 2 ! ')
	
	ligne, colonne = input ('ligne, colonne').split(',')
	return [int(ligne), int(colonne)]

def verif (tableau : list) ->  int  :
	n = len(tableau)
	S = []
	Sdiago_1 = tableau[0][0] + tableau[1][1] + tableau[2][2]
	Sdiago_2 = tableau[2][0] + tableau[1][1] + tableau[0][2]  
	for i in range (n) :
		Slocal_ligne = 0
		Slocal_colonne = 0
		for j in range (n) :
			Slocal_ligne = Slocal_ligne +  int(tableau[i][j])
			Slocal_colonne = Slocal_colonne + int(tableau[j][i])
		S.append(Slocal_ligne, Slocal_colonne, Sdiago_1, Sdiago_2)
	for n in S :
		if n == '3' :
			return 1
		elif n == '-3' :
			return 2
	return 0

def play () :		
	grille = init()
	joueur = 1
	gagner = 0
	while gagner == 0 :
		ligne, colonne = demande(joueur)
		while grille[ligne][colonne] != 0 :
			print( 'il est interdit de joer dans la même case ! ;)')
			ligne, colonne = demande(joueur)
		grille[ligne][colonne] = joueur
		gagner = verif(grille)
		affichage(grille)
		if gagner ==1:
			return "joueur 1 a gagné"
		elif gagner == 2 :
			return "joueur 2 a gagné"
		joueur = (-1)*joueur
		
play()
	
