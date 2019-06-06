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

***2. Käyttötapaus:** Pääkäyttäjä haluaa lisätä uuden elokuvan sovellukseen.*

Käyttäjä: Pääkäyttäjä.

Tavoite: Uuden elokuvan lisääminen, jotta muut käyttäjät voivat lisätä sille arvosteluita.

Esiehto: Käyttäjällä on nimenomaan pääkäyttäjän valtuudet.

Jälkiehto: Pääkäyttäjä saa lisättyä elokuvan osaksi listausta.

Käyttötapauksen kulku: Käyttäjä kirjautuu sisään tunnuksilla, jotka oikeuttavat pääkäyttäjän valtuuksiin. Käyttäjä navigoi itsensä elokuvien listaukseen. Pääkäyttäjä painaa hänelle näkyvää nappia, jolla voi lisätä uuden elokuvan. Käyttäjä täyttää hänelle annettavan lomakkeen. Lomakkeessa annettujen tietojen perusteella luodaan uusi elokuva osaksi listausta.

***3. Käyttötapaus:** Ulkopuolinen käyttäjä haluaa tarkastella tietyn kategorian parhaita arvosanoja saaneita elokuvia.*

Käyttäjä: Ulkopuolinen käyttäjä (ei rekisteröitynyt/kirjautunut).

Tavoite: Elokuvien arvosanojen tarkastelu tietyssä kategoriassa.

Esiehto: Ei erityisiä esiehtoja. Riittää, että käyttäjä löytää sivuston.

Jälkiehto: Käyttäjä pääsee tarkastelemaan ja selaamaan arvosanoja.

Käyttötapauksen kulku: Käyttäjä navigoi sivustolle. Hän ei kirjaudu sisään. Sen sijaan hän menee suoraan elokuvien listaukseen. Hän valitsee suodattimeksi haluamansa kategoriat (esimerkiksi komedia). Käyttäjälle näytetään kategorian sisältämät elokuvat. Käyttäjä painaa nappia järjestääkseen elokuvat arvosanajärjestyksessä. Seurauksena käyttäjälle näytetään tulokset paras arvosana korkeimana. Käyttäjä voi tästä halutessaan jatkaa esim. klikkaamalla tiettyä elokuvaa lukeakseen arvostelutekstejä.