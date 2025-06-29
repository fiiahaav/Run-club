# Run-club
Run-club on kaikille juoksusta kiinostuneille suunnattu web-sovellus, jossa käyttäjät voivat luoda profiilin, tehdä ilmoituksia yhteislenkeistä sekä etsiä ja liittyä muiden järjestämille juoksulenkeille. Sovelluksen tarkoitus tukee yhteisöllisyyttä ja motivoida liikkumaan yhdessä.


## Sovelluksen tominnot

- Sovellukseen on mahdollista luoda käyttäjätunnus
- Käyttäjän on mahdollista kirjautua sisään ja sovelluksesta ulos
- Käyttäjä voi tehdä ilmoituksen lenkistä. Ilmoitukseen ilmoitetaan reittisuunnitelma, halutessaan muuta lisätietoa juoksusta, reitin pituus sekä päivämäärä, lenkin haastavuustaso sekä sen luokittelu
- Käyttäjäsivuilla näkyy montako ilmoitusta käyttäjän nimissä on ja mitä ilmoituksia ne ovat
- Käyttäjällä on mahdollisuus muokata tai poistaa itse luomansa ilmoitus
- Käyttäjä voi myös lisätä omiin ilmoituksiinsa kuvia sekä poistaa niitä
- Hakusanalla tai päivämäärällä voi etsiä ilmoituksia lenkeistä
- Käyttäjä voi ilmoittautua toisen käyttäjän ilmoittamalle lenkille lähettämällä kommentin

## Sovelluksen käynnistysohjeet:

### 1. Siirry projektikansioon, jossa `app.py` sijaitsee:

```
cd ~/Run-club
```

Luo virtuaaliympäristö ja aktivoi se:
```
python3 -m venv venv source venv/bin/activate)
```

Asenna `flask`kirjasto:
```
$ pip install flask
```

Luo tietokannan taulut, lisää alkutiedot:
```
$ sqlite3 database < schema.sql
$ sqlite3 database < init.sql
```

Aseta ympäristömuuttuja ja käynnistä sovellus:
```
export FLASK_APP=app.py
flask run
```

Sovellus on nyt käytettävissä osoitteessa:
```
http://127.0.0.1:5000
```
