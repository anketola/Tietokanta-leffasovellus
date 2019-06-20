# Tietokannan rakenne

## Tietokantakaavio

![Tietokantakaavio](https://github.com/anketola/Tietokanta-leffasovellus/blob/master/documentation/pictures/tietokanta_paivitetty.jpg)

## CREATE TABLE -lauseet

```
CREATE TABLE movie (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  name VARCHAR(144) NOT NULL,
  released INTEGER NOT NULL,
  description VARCHAR(1000) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE category (
  id INTEGER NOT NULL,
  name VARCHAR(144) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE account (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  username VARCHAR(144) NOT NULL,
  password VARCHAR(144) NOT NULL,
  admin BOOLEAN NOT NULL,
  PRIMARY KEY (id),
  CHECK (admin IN (0, 1))
);

CREATE TABLE moviescategories (
  movie_id INTEGER,
  category_id INTEGER,
  FOREIGN KEY(movie_id) REFERENCES movie (id),
  FOREIGN KEY(category_id) REFERENCES category (id)
);

CREATE TABLE review (
  id INTEGER NOT NULL,
  date_created DATETIME,
  date_modified DATETIME,
  rating INTEGER NOT NULL,
  reviewtext VARCHAR(1000) NOT NULL,
  account_id INTEGER NOT NULL,
  movie_id INTEGER NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (account_id) REFERENCES account (id),
  FOREIGN KEY (movie_id) REFERENCES movie (id)
);
```
## Rakenteen vastaavuus suunnitelmaan

Rakenne vastaa pääasiallisesti alkuperäistä suunnitelmaa. Sovelluksen kehitysvaiheessa attribuutit ovat kuitenkin täsmentyneet, ja ne on pääpiirteittäin sovitettu harjoitustyön järkeväksi rajaamiseksi. Account taulun date_created ja date_modified eivät ole aktiivisessa käytössä, mutta ne on sisällytetty rakenteeseen sitä varten, että admin-toimintoja voidaan halutessaan myöhemmin laajentaa käyttäjien hallintaan.

Isoin muutos alkuperäiseen suunnitelmaan verrattuna on comments-taulun poissaolo. Taulun oli tarkoitus käyttää käyttäjien arvosteluille antamien kommenttien tallentamiseen. Taulu sisälsi yhteyden sekä käyttäjään että arvosteluun. Attribuutteina olisivat ollet esim. kommenttiteksti että aikatiedot. Toiminto osoittautui kehitysvaiheessa tarkoituksettomaksi (sekavoitti yleisesti sovelluksen käyttöä, pelkkä yleinen arvostelutoiminto vaikutti selkeämmältä). Mikään ei kuitenkaan estäisi taulun ottamista myöhemmin osaksi sovellusta, jos toiminnallisuuksia lisättiin. Tästä aihepiiristä katso tarkemmin [työn ja sovelluksen rajoitteet](https://github.com/anketola/Tietokanta-leffasovellus/blob/master/documentation/rajoitteet.md).


