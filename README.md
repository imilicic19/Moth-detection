# Moths-detection
Detection of moth species using YOLO
Problem u ovom zadatku predstavlja detekcija i brojanje Stenoma catenifer vrste moljca. Postoji par referentnih slika kako ovaj moljac izgleda, ali znanicna baza podataka sa labelama i dalje ne. Treba da se napravi sistem koji ce ovu vrstu moljca moci da detektuje u feromonskoj zamci. Stoga je predlog resenja sledeci:
  1. izabrani prstup: detekcija, sa dodatnom da se omoguci i brojanje moljaca na slici
  2. kako slike sa labelama ne postoje, ideja je sledeca. Uzece se EU moths dataset koji sadrzi slike 200 klasa moljaca. Vecina klasa ima po 11 slika moljca u folderu izuzev dve: lobophora_halterate (14) i sphinx_ligustru(13). Zasto sam krenula ovako? Pa, krajnji zahtev je sistem koji ce moci da detektuje Stenoma catenifer, sto je zapravo moljac. Stoga, prvo je neophodno da prilagodimo model detekciji moljca, da zna kako izgleda taj insekt, pa bi kasnija nadogradnja bila prilagodjavanje na vrstu od interesa uz dodatak novih slika tog moljca.
  3. bice omogucena i augmentacija jer je pozicija kamere koja snima moljce u feromonskoj zamci moze biti pod razlicitim uglom, takodje ambijentalna svetlost moze da varira u spoljasnjoj sredini, sam polozaj moljca moze biti razlicit (kako se zalepi za traku)


Koraci:
  1. skinuti EU moths bazu podataka, proanalizirati je (broj klasa, rezolucija slika, balansiranost baze podataka)
  2. labeliranje (automatsko), GroundingDino
  3. konverzija labela iz .JSON formata u .TXT kako bismo mogli da primenimo YOLO model
  4. primenicemo augmentaciju tokom treninga (online) kako bismo obezbedili prilagodjenje modela na moguce varijabilnosti u realnim situacijama
  5. nakon treniranja testiracemo na par slika moljaca iz test grupe, kao i na par referentnih primera Stenoma catenifer da vidimo da li je lokalizacija uspesna. Prepoznavanje sigurno nece biti jer takvu klasu model nije video.

