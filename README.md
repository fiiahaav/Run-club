# Run-club
Run-club
- Sovellukseen on mahdollista tehdä käyttäjätunnus
- Käyttäjäsivuilla näkyy montako ilmoitusta käyttäjän nimissä on ja mitä ilmoituksia ne ovat
- Käyttäjä pystyy kirjautua sisään ja sovelluksesta ulos
- Käyttäjä voi tehdä ilmoituksen lenkistä. Ilmoitukseen ilmoitetaan reittisuunnitelma, halutessaan muuta lisätietoa juoksusta, reitin pituus sekä päivämäärä (tämä toiminto ei vielä toimi)
- Käyttäjällä on mahdollisuus muokata tai poistaa itse luomansa ilmoitus
- Hakusanalla voi etsiä ilmoituksia lenkeistä

Sovelluksen käynistysohjeet:
 työkalut: 
 pip
 python

- Siirry kansioon, jossa `app.py` sijaitsee:

   ```bash
   cd Run-club
-Luo virtuaaliympäristö ja aktivoi se:
  (python3 -m venv venv source venv/bin/activate)
- Aseta ympäristömuuttuja ja käynnistä sovellus:
   export FLASK_APP=app.py flask run
-sovellus on nyt käytettävissä osoitteessa:
  http://127.0.0.1:5000
