# Aineopintojen harjoitustyö: Tietokantasovellus

## Aihekuvaus: Leffa-arvostelut

Harjoitustyön aiheena on elokuva-arvosteluja sisältävä järjestelmä. Elokuvien järjestelmän listalle voi lisätä tai poistaa ainoastaan ylläpitäjä. Elokuvalle annetaan lisäämisen yhteydessä tyypillisiä tietoja kuten nimi, julkaisuvuosi, kuvaus ja pituus. Elokuvat luokitellaan kuulumaan yhteen tai useampaan kategoriaan. Ylläpitäjä voi tarvittaessa muokata elokuvien tietoja myöhemmin.

Sivulle voi rekisteröityä käyttäjäksi. Kirjautuneet käyttäjät voivat kirjoittaa arvosteluja ja antaa arvosanan listatuille elokuville. Käyttäjät voivat halutessaan muokata tai poistaa jälkikäteen tekemänsä arvostelun. Käyttäjät voivat katsella myös kootusti kaikkia tekemiään arvosteluja. Käyttäjät voivat kommentoida muiden tekemiä arvosteluja.

Kirjautumattomat käyttäjät pääsevät ainoastaan selaamaan elokuvia ja katselemaan annettuja arvosteluja, mutta eivät lisäämään omia arvosteluita.

Keskeisiä toimintoja:

* Elokuvien lisääminen / poistaminen
* Elokuvien tietojen muuttaminen
* Käyttäjän rekisteröityminen
* Kirjautuminen (ylläpitäjä / käyttäjä)
* Kirjautuneen käyttäjän mahdollisuus jättää arvostelu ja muokata/poistaa se
* Kirjautuneen käyttäjän mahdollisuus kommentoida arvostelua
* Uusimpien arvosteluiden listaaminen etusivulla
* Arvosteluiden lukeminen ja muu tarkastelu
* Elokuvien haku nimellä, suodattaminen kategorialla
* (mahdollisesti jotain yleistä statistiikkaa)

## Sovellus Herokussa

https://limitless-chamber-60577.herokuapp.com/

### Testitunnukset

Admin-tunnukset:

```
Käyttäjänimi: admin
Salasana: admin
```

Sovellus sisältää rekisteröitymismahdollisuuden normaaleille käyttäjille. Halutessaan voi käyttää myös seuraavia testitunnuksia. 

```
Käyttäjänimi: testitunnus
Salasana: testitunnus
```


## Dokumentaatio

[Käyttötapaukset](https://github.com/anketola/Tietokanta-leffasovellus/blob/master/documentation/kayttotapaukset.md)

[Hahmotelma tietokantakaaviosta](https://github.com/anketola/Tietokanta-leffasovellus/blob/master/documentation/tietokantakaavio.md)
