# Asennusohje

Nämä ohjeet on jaettu kaahteen osaan. Ensimmäisessä osassa käsitelemme sovelluksen asennusta lokaalisti. Toisessa osassa tarkastelemme sovelluksen asentamista toimimaan Herokussa.

Tässä oletetaan, että tietokoneelle on asennettu jo Python3 sekä tuet kirjastojen laataamiselle että virtuaaliympäistöille.

## Sovellus paikallisesti

### Tarvittavien tiedostojen lataaminen

Aloittaaksesi asennuksen, kopioi itsellesi ensi soellukseen liittyvät tiedostot. Voit kopioida tiedostot joko menemällä sovelluksen sisältämään repositiorioon ja painamalla vihreää "Clone or download" linkkiä ja purkamalla ZIP-paketti. Toinen vaihtoehto on käyttää gitin clone -komentoa.

Siirry kansioon, johon haluat sovelluksen asennettavan. Anne sitten seuraava komento:
```
git clone git@github.com:anketola/Tietokanta-leffasovellus.git
```
Sinulla pitäisi ollan nyt paikallinen kopio sovelluksesta. Samassa kansiossa sovelluksen kanssa ollessasi anna seuraava komento:
```
python3 -m venv venv
```
Tämä luo sovellusta varten virtuaaliympäristön. Käynnistämme sen antamalla seuraavan käskyn:
```
source venv/bin/activate
```
Voimme nyt hyödyntää tiedostojen mukana tullutta requirements.txt -tiedostoa ja ottaa käyttöön kaikki tarvittavat riippuvuudet. Anna seuraava komento, jotta riipuuvdet asentuvat osaksi virtuaaliympäristöä:
```
pip install -r requirements.txt
```
Lopulta käynnistämme sovelluksen paikallisesti antamalla seuraavan käskyn:
```
python3 run.py
```
Sovellus luo tietokantatalutut, mutta joudumme muokkaamaan niiden sisältöä ennen sovelluksen varsinaista käyttöönottoa.

Paina Ctrl+C keskeyttääksei sovelluksen suorituksen. Siirry sen jälkeen seuraavaan osaan, jossa käsitellään käyttäjätunnusten luomista.

### Admin-tunnusten luominen paikallisesti

Tässä käsitellään admin-tunnusten luomista paikallisesti. Huomaathan, että normaalikäyttäjien rekisteröinti onnistuu suoraan sovelluksen toiminnallisuuksia käyttämällä.

Ladattu ZIP-paketti ei sisällä tietokantaa, vaan se luodaan sovelluksen käynnistyksen yhdeysessä. Näin ollen sovellus ei sisällä admin-tason ylläpitäjätunnuksia. Admin-tunnukset ovat välttämättömiä mm. uusien elokuvien lisäämiseksi. Tämän vuoksi joudut luomaan ne erikseen esim. SQLite-ohjelmalla. Sovellus on saatavilla seuraavasta linkistä: https://www.sqlite.org/download.html

Asenna ohjelma ja suorita seuraava komento kansiossa, johon sovellus on asennettu:
```
sqlite3 application/movies.db
```
Tämä avaa sinulle konsolin tietokantaan. Kirjoita seuraava koodipätkä konsoliin.
```
INSERT INTO account (username, password, admin) VALUES ('admin','admin', 1);
```
Komento lisää uuden käyttäjän, jonka käyttäjänimi on admin (ensimmäinen parametri) ja salasana admin (toinen parametri). Muuta nämä mieleisiksi. Viimeisen parametrin tulee kuitenkin olla aina 1 uutta adminia luotaessa.

Voit sulkea SQLiten kirjoittamalla konsoliin
```
.exit
```

### Lopputoimet

Paikallisen asennuksen tulisi olla nyt valmis. Suljimme aiemmin sovelluksen suorituksen. Käynnistetään se uudestaan käskyllä

```
python3 run.py
```
Avaa selain ja siirry osoitteeseen localhost:5000. Jos sovellus on käynnissä, sinun pitäisi päästä käyttämään sovellusta normaalisti sisäisessä verkossa.

Seuraava kokonaisuus käsittelee tilannetta, jossa sovellus halutaan paikallisen asennuksen jälkeen viedä Herokuun myös muitten käytettäväksi.

## Sovelluksen asennus Herokuun

### Tarvittavat esitoimet

Kun olet toteuttanut paikallisen asennuksen (voit jättää välistä käyttäjätunnusten luomisen - teemme ne erikseen Herokuun), voit siirtää sovelluksen Herokuun.

Tässä oletetaan, että käyttäjä on asentanut itselleen Herokun, hankkinut siihen käyttäjätunnuksen ja koneella on 
PostgreSQL-tietokannanhallintajärjestelmä.

Aloitamme siirtymällä sovelluksen kansioon ja luomalla Heroku sovelluksne komennolla
```
heroku create sovelluksennimi
```
Voit vaihtaa yllä olevan "sovelluksennimi" mieleiseksesi.

Nyt yhdistämme paikallisen versionhallinnan Herokuun. Tehdäksesi tämän anna komento
```
git remote add heroku
```
Siirrämme nyt gitin avulla version herokuun. Anna seuraavat käskyt.
```
git add .
git commit -m "initial commit"
git push heroku master
```
Teemme nyt PostgreSQL-tietokannan vaatimia toimenpiteitä. Anna seruaavat kommennot
```
heroku config:set HEROKU=1
heroku addons:add heroku-postgresql:hobby-dev
```
Herokulla on nyt tietokanta käytössään.

### Admin-tunnusten luominen PostgreSQL-tietokantaan

Samoin kuin paikallisen version kanssa, joudumme lisäämään admin-tunnukset tietokantaan. Aloitamme tämän antamalla komennon
```
heroku pg:psql
```
Avautuvaan konsoliin kirjoita jälleen seuraavat tiedot:
```
INSERT INTO account (username, password, admin) VALUES ('admin','admin', TRUE);
```
Voit jälleen vaihtaa kahta ensimmäistä parametriä.

Lopulta sulje yhteys tietokantaan antamalla komento

```
\q
```

Ohjelman pitäisi olla nyt toiminnassa "heroku create" -käskyn suorittamisen yhteydessä ilmoitetussa verkko-osoitteessa.

## Muuta tietoa asennuksesta

Sovelluksen käyttönotto edellyttää, että aiemmin kuvattujen admin-tunnusten avulla luodaan sisältöä sovellukseen. Uusien elokuvien lisäämiseksi admin-tunnuksilla on ensimmäiseksi luotava halutun nimisiä elokuvakategorioita. Elokuvakategorioiden olemassaolo on edellytys uusien elokuvien lisäämiseksi sovellukseen. 

Haluttaessa kategorioita on mahdollista luoda suoraan tietokantaan asennuksen yhteydessä. Seuraavalla komennolla lisättäisiin uusi kategoria nimeltään "Komedia".

```
INSERT INTO category (name) VALUES ('Komedia');
```

Sovellus sisältää kuitenkin lomakkeen kategoriden lisäämisen admin-tunnuksilla. Ohjeet sekä uusien kategorioiden että elokuvien lisäämiseen sovellukseen saat [käyttöohjeesta](https://github.com/anketola/Tietokanta-leffasovellus/blob/master/documentation/kayttoohje.md).





