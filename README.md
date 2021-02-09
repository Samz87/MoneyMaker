# MoneyMaker
>Installer Visual Studio Code
  https://code.visualstudio.com/

>Installer Python
  https://www.python.org/downloads/

>Télécharger MoneyMaker

>Effectuer le raccourci Windows+R et taper cmd

>Dans l'invite de commande taper 

>Ajouter au PATH 
 <code>appData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\Scripts</code>
  
>Ouvrir MoneyMaker avec VScode

>Dans VScode télécharger l'extension python

>Dupliquer le fichier config-template.py puis renommer le fichier dupliqué en config.py

>Completer le fichier config.py : <br />
  API_KEY et API_SECRET - Le duo de clés API généré sur Binance <br />
  RSI_PERIOD - Nombre d'itérations avant de calculer un RSI (14) <br />
  RSI_OVERBOUGHT - RSI auxquel le bot considère que la crypto est surachetée (70) <br />
  RSI_OVERSOLD - RSI auquel le bot considère que la crypto est survendue (30) <br />
  TRADE_SYMBOL - Symbole de la crypto tradée <br />
  TRADE_QUANTITY - Nombre de crypto achetées/vendues <br />

>Exécuter la commande CTRL+SHIFT+ù puis dans le terminal taper <code>pip install -r requirements.txt</code>
  
>Dans la console, taper <code>bot.py</code>
  Ouvrir avec python
  
