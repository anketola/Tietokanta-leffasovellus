# Työn ja sovelluksen rajoitteet

Työ suurinpiirtein vastaa alunpitäen suunniteltua, mutta se on muovautunut työskenteltäessä. Tietokantaan liittyvin isoin poikkeavuus ja puuttuva ominaisuus on arvosteluiden kommentointimahdollisuuden puuttuminen. Asiasta on myös dokumentaation tietokannan rakennetta kuvaavaan kohdan lopussa. Pääsyynä arvosteluiden kommentointitoiminnallisuuden puuttumiseen - ja puuttuvaan tauluun - on kommentointitoiminnon arvioitu tarpeettomuus. Tämä implementoitiin hetkeksi, mutta sen toteuttaminen olisi edellyttänyt huomattavasti aikaa ulkonäön viilaamiselle, ja päätettiin poistaa. Käyttäjälle olisi pitänyt olla selkeää, milloin kyseessä on arvostelu ja milloin kommentti, miten niiden välillä navigoidaan jne. Lopulliseen versiosta siis puuttuu tämä kommentointimahdollisuus.

Ehkä merkittävin sovelluksen rajoite, jota ei ole ehditty nyt toteuttaa on hyvä skaalautuminen. Työ on mitoitettu niin, että se toimii kohtuullisen pienellä entry-määrällä. Sovellukseen ei ehditä toteuttaa esim. elokuvien hakutoimintoa. Näin jos tietokanta sisältäisi satoja elokuvia, olisi sovelluksen käyttö hieman hankalaa. Elokuvien selauksessa, arvostelujen listauksessa jne. ei ole toteutettu sivutustoimintoa. Samoin sovelluksen laajentuessa pitäisi ehkä tarkastella yleisesti sekä sivurakennetta että tietokantakyselyjä vielä kertaalleen.

Toivottuna toiminnallisuutena, joka sovelluksesta uupuu, on käyttäjien toiminnasta tehtävä statistiikka ja muut havainnot. Tämä olisi toki toteutettavissa myöhemmin. Eräänä toisena seikkana voisi vielä mainita kategorioiden hallinnan. Elokuvien kategorioiden osalta sovelluskeen lisättiin loppumeterillä lisäystoiminto admin-käyttäjälle. Tästä uupuu kuitenkin kategorioiden muokkaus ja poistomahdollisuus. Suunniteluvaiheessa kategoriat ajateltiin jokseenkin "pysyviksi", mutta myöhemmin niidenkin muokkaustarve ilmeni. Elokuvien kategorioita voi kyllä vapaasti vaihdella.

Viimeiseksi puutteista ja rajoitteista voisi mainita eräiden tietokohteiden attribuutit. Esimerkiksi elokuvan kuvauksen pituus on 1000 merkkiä. Vastaava rajoite on arvostelutekstin pituudella. Näiden kohdalta pitäisi varmaan tehdä jonkinlaista analyysiä siitä, ovatko ne laajuudeltaan tarkoituksenmukaisia. Jonkin käyttäjän kokemusta voisi ehkä merkittävstikkin häiritä se, että arvostelut ovat vain niin lyhyitä.

## Jatkokehitysideat

Sovellukselle löytyisi useita jatkokehitysideoita edellä mainittujen skaalautuvuuden parantamisen, kommentointimahdollisuuden, käyttäjästatistiikan ja kategoriden hallinnan parantamisen lisäksi. Yleisesti ottaen sovellus olisi ensinnäkin muokattavissa toiseen käyttötarkoituksen suhteellisen vähällä työllä. Eli elookuva-arvostelujen sijaan jonkin muun kohteen arvosteluihin. Sovellukssa kun on se, että elokuvien manuaalinen syöttö adminilta vaatisi melkoista työtä ja jokin toinen aihepiiri voisi olla soveltuvampi.

Muita jatkokehityskohteita voisivat olla yleisen visuaalisen ilmeen parantaminen. Etenkin CSS-tulisi ottaa käyttöön. Tähän liittyy myös tietokantaan ja attribuutteihin liittyen valokuvat. Elokuvien osalta kansikuva tai muut kuvat elokuvasta olisivat tervetulleita. Nämä jätettiin suunniteluvaiheessa tarkoituksella pois. Muutoinkin elokuvien attribuutteja voisi laajentaa, ja ottaa käyttöö esim. näyttelijälistaus.
 
Jatkokehitysideana mainittakoon vielä, että adminille voisi luoda hallintapaneelin myös käyttäjien hallinnointiin. Tätä varten account-tauluun jätettiin luomisaika ja muokkausaika attribuuteiksi. Adminille voisi olla hyödyllistä tarkastella eri käyttäjien aktiviteetteja kootusti jne.

Yksittäisiä käytettävyys ja saavutettavuusparannuksia olisi varmaan lukematon määrä.
