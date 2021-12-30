# PAC/PEC 4

L'estructura bàsica del projecte està formada per un paquet, anomenat "trax",
i un seguit de scripts, cadascun executant una de les tasques de l'enunciat. És necessari
executar l'script task_1.py en primer lloc, ja que aquest script genera un fitxer sobre
el qual treballen la majoria de scripts subsegüents.

Descripció dels scripts:

**Task_1.py:**

Aquest script descomprimeix els datasets originals a partir del fitxer zip
i els emmagatzema en la seva forma inicial en un nou fitxer "csv_files". Realitza
les correccions necessàries i genera un dataframe desnormalitzat anomenat 
"all_merge". L'script posteriorment exporta aquest dataframe a csv amb el nom 
"tracks_csv", que emmagatzema en el mateix directori "data" que contenia el zip
original. L'script mostra per pantalla els criteris d'acceptació.


**Task_2.py:**
 
Aquest script crida les funcions definides al mòdul 'times' del paquet 'trax'.
Aquestes funcions retornen els temps d'execució i també les
columnes del fitxer csv en forma de llista. L'script en selecciona només els
temps d'execució i la llargada de la llista per tal de fer el gràfic requerit.
Malauradament, no he trobat una forma més ràpida de llegir el fitxer comparant 
amb Pandas, i veiem en el gràfic que, per una mida petita, les dues funcions
prenen temps similars, però per mides més grans el mètode pandas és més efectiu.    


**Task_3.py**

Aquest script executa totes les preguntes plantejades utilitzant el mòdul
subset del paquet trax, sempre partint del fitxer csv creat a la tasca 1.   

**Task_4.py**

Aquest script executa les tasques plantejades utilitzant el mòdul stats del paquet trax.

**Task_5.py**

Aquest script utilitza el mòdul stats del paquet trax i retorna un histograma de densitat.

**Task_6.py**

Aquest script utilitza exactament la mateixa funció que en la tasca 5. Hem adaptat la
funció per tal que pugui acceptar el nom d'un sol artista o de dos artistes.

**Task_7.py**

