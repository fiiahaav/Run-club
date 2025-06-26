# Run-club


## Sovelluksen tominnot

- Sovellukseen on mahdollista luoda käyttäjätunnus
- Käyttäjän on mahdollista kirjautua sisään ja sovelluksesta ulos
- Käyttäjä voi tehdä ilmoituksen lenkistä. Ilmoitukseen ilmoitetaan reittisuunnitelma, halutessaan muuta lisätietoa juoksusta, reitin pituus sekä päivämäärä
- Käyttäjäsivuilla näkyy montako ilmoitusta käyttäjän nimissä on ja mitä ilmoituksia ne ovat
- Käyttäjällä on mahdollisuus muokata tai poistaa itse luomansa ilmoitus
- Hakusanalla voi etsiä ilmoituksia lenkeistä
- Käyttäjä voi ilmoittautua toisen käyttäjän ilmoittamalle lenkille lähettämällä kommentin

## Sovelluksen käynnistysohjeet:

Asenna `flask`kirjasto:

```
$ pip install flask
```


Luo tietokannan taulut, lisää alkutiedot:
```
$ sqlite3 database < schema.sql
$ sqlite3 database < init.sql
```
Käynnistä sovellus näin:

```

$ flask run
```


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
