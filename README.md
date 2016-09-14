Jeu du démineur - Python3

Problème :Pas de lien clair entre ma GUI et mon tableau de mines
solution = classe héritant de button, avec en plus des attributs is_bomb, revealed... ?


marche => problème pour accéder aux attributs de la grille : les mettre en attribut de classe, sachant qu'on ne créera qu'une Grid ? Mais c'est pas générique pour 3 ronds
If left click:
	- if bomb
		print bomb image and lose
	- else
		print number
		if zero:
			discover neighbours

If right click:
	- if nothing
		add flag image
	- else
		remove flag image






- intégration à l'OS pour en faire une app ?
- grilles non rectangulaires ?
- indice de mesure de difficulté : 3BV


