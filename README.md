# SFS-RP-Bot
Discord Bot for SFS 

Architecture MVC

Test unitaire requis, a choisir la methode que vous préferez : 

Avec DOCTEST :
https://docs.python.org/3/library/doctest.html
Ecrit directement les test dans la methode que l'on souhaite tester
 
Avantage :
  - Plus facile a ecrire, tout est dans le meme .py

Inconveniant : 
  - Le code est plus long
  - Code moin lisible 
  - Lors de la MEP (Mise ne prod) sur la branche main, faut les suppr, on fait pas tourner ca chez le client mdr


Avec UNITTEST :
https://docs.python.org/3/library/unittest.html
  Ecrit les test dans un .py séparé
    
 Avantage : 
  - Le code metier du bot n'est pas alourdis, ni rallongé, meilleur visibilité 
  - lors de la MEP, pas de modif a faire, juste les script a ignorer 
  - Permets des test plus poussé (enchainement d'appel de methodes, simulation dexecution)
  
Inconveniant : 
  - Liaison entre le test et le code plus dificile (utilisation d'un using, et appel de methode, pas plus)
  - demande queleques ligne de plus a ecrire (voir doc )
