# Run-club
Run-club
- Sovellukseen on mahdollista tehdä käyttäjätunnus
- Käyttäjäsivuilla näkyy montako ilmoitusta käyttäjän nimissä on ja mitä ilmoituksia ne ovat
- Käyttäjä pystyy kirjautua sisään ja sovelluksesta ulos
- Käyttäjä voi tehdä ilmoituksen lenkistä. Ilmoitukseen ilmoitetaan reittisuunnitelma, halutessaan muuta lisätietoa juoksusta, reitin pituus sekä päivämäärä (tämä toiminto ei vielä toimi)
- Käyttäjällä on mahdollisuus muokata tai poistaa itse luomansa ilmoitus
- Hakusanalla voi etsiä ilmoituksia lenkeistä

Sovelluksen käynnistysohjeet:
- työkalut: pip, python
  

- Siirry kansioon, jossa `app.py` sijaitsee:

   ```bash
   cd Run-club
- Luo virtuaaliympäristö ja aktivoi se:

  ```bash
  python3 -m venv venv source venv/bin/activate)
- Asenna tarvittaessa:
    ```bash
    pip install flask
- Aseta ympäristömuuttuja ja käynnistä sovellus:
   ```bash
   export FLASK_APP=app.py flask run
- Sovellus on nyt käytettävissä osoitteessa:
  http://127.0.0.1:5000
