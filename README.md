# flash-cards

1. "python -m venv venv"
2. connect to the venv ("source venv/bin/activate" for linux distros)
3. "pip install -r requirements.txt"
4. "flask run"
5. navigate to localhost:5000

![Login](/images/login.png)
![Front of Card](/images/learnfront.png)
![Back of Card](/images/learnback.png)


complete:
* registration/login system
  * bcrypt hashing, werkzeug_security, flask UserMixin
* custom json encoder to pass list of objects over to js
  * models.py line 58-94
* async function to update status of card -- boolean field in sqlite db "known" -- on button press.
  * app.js lines 60-74
 
to do:
* registration/login system
  * email validation
* cacheing
* bucketing algorithm
* frontend all pages
  * start with add card/edit/view page (cards.html)

