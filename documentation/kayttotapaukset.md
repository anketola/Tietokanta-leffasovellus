# Käyttötapaukset

Seuraavassa on sovelluksen kannalta tällä hetkellä olennaisimmiksi arvioidut käyttötapaukset.

Käyttäjäryhmiä on kolme: ulkopuolinen käyttäjä, tavallinen käyttäjä (rekisteröitynyt) ja pääkäyttäjä

***1. Käyttötapaus:** Käyttäjä haluaa antaa elokuvalle arvostelun.*

Käyttäjä: Tavallinen käyttäjä (rekisteröitynyt).

Tavoite: Arvostelun lisääminen tietylle elokuvalle.

Esiehto: Käyttäjä on kirjautunut sisälle järjestelmään. 

Jälkiehto: käyttäjä saa lisättyä arvostelun haluamalleen elokuvalle.

Poikkeuksellinen toiminta: Elokuvaa ei ole listattuna. Tässä tilanteessa tavallinen käyttäjä ei lisätä arvostelua, koska elokuvia voi lisätä ainoastaan pääkäyttäjä. Vaihtoehtona voisi olla ehdottaa pääkäyttäjälle elokuvan lisäämistä.

Käyttötapauksen kulku: Käyttäjä kirjautuu sisälle omalla käyttäjätunnuksella ja salasanalla. Käyttäjä etsii haluamansa elokuvan niiden listaukseen/hakuun tarkoitetun tarkoitetun linkin kautta. Käyttäjä klikkaa haluamaansa elokuvaa ja sen jälkeen arvostelun lisäämiselle tarkoitettua nappia. Käyttäjälle näytetään lomake, jonka täyttämällä voi lisätä arvostelun. Käyttäjä painaa lähetä-nappia ja arvostelu lisätään osaksi elokuvan tietoja.

```
INSERT INTO review (rating, reviewtext, account_id, movie_id) VALUES (?, ?, ?, ?);

Jossa account_id on aktiivisen käyttäjän id ja movie_id arvosteltavan elokuvan id.
```

***2. Käyttötapaus:** Pääkäyttäjä haluaa lisätä uuden elokuvan sovellukseen.*

Käyttäjä: Pääkäyttäjä.

Tavoite: Uuden elokuvan lisääminen, jotta muut käyttäjät voivat lisätä sille arvosteluita.

Esiehto: Käyttäjällä on nimenomaan pääkäyttäjän valtuudet.

Jälkiehto: Pääkäyttäjä saa lisättyä elokuvan osaksi listausta.

Käyttötapauksen kulku: Käyttäjä kirjautuu sisään tunnuksilla, jotka oikeuttavat pääkäyttäjän valtuuksiin. Pääkäyttäjällä on näkyvissä erillinen admin-työkalupalkki. Pääkäyttäjä painaa hänelle siinä näkyvää nappia, jolla voi lisätä uuden elokuvan. Käyttäjä täyttää hänelle annettavan lomakkeen. Lomakkeessa annettujen tietojen perusteella luodaan uusi elokuva osaksi listausta. Listattu elokuva näkyy nyt kaikille muille sovlluksen käyttäjille (myös ei rekisteröityneille).

```
INSERT INTO movie (name, released, description) VALUES (?, ?, ?);
```

***3. Käyttötapaus:** Ulkopuolinen käyttäjä haluaa tarkastella tietyn kategorian parhaita arvosanoja saaneita elokuvia.*

Käyttäjä: Ulkopuolinen käyttäjä (ei rekisteröitynyt/kirjautunut).

Tavoite: Elokuvien arvosanojen tarkastelu tietyssä kategoriassa.

Esiehto: Ei erityisiä esiehtoja. Riittää, että käyttäjä löytää sivuston.

Jälkiehto: Käyttäjä pääsee tarkastelemaan ja selaamaan arvosanoja.

Käyttötapauksen kulku: Käyttäjä navigoi sivustolle. Hän ei kirjaudu sisään. Sen sijaan navigoi selaamaan elokuvia. Hän valitsee lomakkeella kategorian, jonka suosituimmat elokuvat hän haluaa nähdä. Käyttäjälle näytetään kategorian sisältämät elokuvat koreimman arvosanan saanut ensin. Käyttäjä voi tästä halutessaan jatkaa esim. klikkaamalla tiettyä elokuvaa lukeakseen arvostelutekstejä.

```
Kategorian perusteella esitetään tiedon esittämiseksi seuraava kysely. Category.id vastaa haetun kategorian ID:tä.

SELECT Movie.id, Movie.name, Movie.released, AVG(Review.rating) FROM Movie
INNER JOIN Review ON Review.movie_id = Movie.id
INNER JOIN Moviescategories ON Moviescategories.movie_id = Movie.id
INNER JOIN Category ON Category.id = Moviescategories.category_id
WHERE Category.id = "?"
GROUP BY Movie.id
ORDER BY AVG(Review.rating) DESC;
```

