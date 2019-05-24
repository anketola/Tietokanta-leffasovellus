# Käyttötapaukset

Seuraavassa on sovelluksen kannalta tällä hetkellä olennaisimmiksi arvioidut käyttötapaukset.

Käyttäjäryhmiä on kolme: ulkopuolinen käyttäjä, tavallinen käyttäjä (rekisteröitynyt) ja pääkäyttäjä

***1. Käyttötapaus:** Käyttäjä haluaa antaa elokuvalle arvostelun.*

Käyttäjä: Tavallinen käyttäjä (rekisteröitynyt).

Tavoite: Arvostelun lisääminen tietylle elokuvalle..

Esiehto: Käyttäjä on kirjautunut sisälle järjestelmään. 

Jälkiehto: käyttäjä saa lisättyä arvostelun haluamalleen elokuvalle.

Poikkeuksellinen toiminta: Elokuvaa ei ole listattuna. Tässä tilanteessa tavallinen käyttäjä ei lisätä arvostelua, koska elokuvia voi lisätä ainoastaan pääkäyttäjä. Vaihtoehtona voisi olla ehdottaa pääkäyttäjälle elokuvan lisäämistä.

Käyttötapauksen kulku: Käyttäjä kirjautuu sisälle omalla käyttäjätunnuksella ja salasanalla. Käyttäjä etsii haluamansa elokuvan niiden listaukseen/hakuun tarkoitetun tarkoitetun linkin kautta. Käyttäjä klikkaa haluamaansa elokuvaa ja sen jälkeen arvostelun lisäämiselle tarkoitettua nappia. Käyttäjälle näytetään lomake, jonka täyttämällä voi lisätä arvostelun. Käyttäjä painaa lähetä-nappia ja arvostelu lisätään osaksi elokuvan tietoja.

***2. Käyttötapaus:** Placeholder.*

