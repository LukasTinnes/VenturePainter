**Name:** SVG-Image painten lassen

**Primary Actor:** Diggi oder Tobi Maqguire aus Spiderman 3

**Stakeholder:** Diggi oder Günther Jauch

**Vorbedingung:** Weder SVG Bild noch Metadaten sind korrupt oder fehlerhaft

**Nachbedingung:** Weder SVG Bild noch Metadaten sind verändert, neues Bild ist nicht korrupt und konsistent im Speicher abgelegt

**Trigger:** Ein Bild soll vom Painter umpainted werden

**Minimal Guarantees:** Das System bleibt trotz Fehler kohärent und korrupiert keine Daten

**Success Guarantees:** Das Bild soll eingelesen, umgepainted und das neue Bild auf der Festplatte abgespeichert worden sein

**Main Success Scenario:** 
                           
                           1. Nutzer legt eine SVG an und gibt sie zusammen mit Metadaten dem Programm mit.
                           
                           2. Das System wandelt das ursprüngliche SVG in ein neues Bild um
                           
                                2a. Das System liest die SVG aus und liest ihre Objekte ein
                           
                                2b. Das System interpretiert die Objekte anhand ihrer Positionen im Raum und stellt eine Zugehörigkeitshierarchie auf.
                           
                                2c. Das System interpretiert nacheinander alle Knoten in der Zugehörigkeitshierarchie und fasst sie zu angegebenen neuen Objekten um

                                2d. Das System zeichnet eine neues Bild abhängig der neuen Objekte
                           
                           3. Das System speichert das neu angelegte Bild konsistent im Speicher ab
**Extensions:** None
