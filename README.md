# SFS-RP-Bot
Discord Bot for SFS 

Architecture MVC

Test unitaire requis, à choisir la méthode que vous préferez : 

Avec DOCTEST :
https://docs.python.org/3/library/doctest.html
Ecrit directement les tests dans la méthode que l'on souhaite tester
 
Avantage :
  - Plus facile à écrire, tout est dans le même .py

Inconvenients : 
  - Le code est plus long
  - Code moins lisible
  - Lors de la MEP (Mise en prod) sur la branche main, faut les suppr, on fait pas tourner ça chez le client mdr


Avec UNITTEST :
https://docs.python.org/3/library/unittest.html
Ecrit les tests dans un .py séparé
    
Avantages : 
  - Le code métier du bot n'est pas alourdi, ni rallongé, meilleure visibilité
  - Lors de la MEP, pas de modif à faire, juste les scripts à ignorer 
  - Permets des tests plus poussés (enchainement d'appel de methodes, simulation d'éxécution)
  
Inconvenients : 
  - Liaison entre le test et le code plus difficile (utilisation d'un using, et appel de méthode, pas plus)
  - Demande quelques lignes de plus à écrire (voir doc)
