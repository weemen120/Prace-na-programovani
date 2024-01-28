-- Tabulka pro hráče
CREATE TABLE hrac (
    player_ID int NOT NULL PRIMARY KEY,
    nick CHAR(50) NOT NULL,
    profile_picture
    Country_name CHAR(64) NOT NULL,
    registation_date AUTO_INCREMENT
);

-- Tabulka pro skóre
CREATE TABLE skore (
    skore_id INT PRIMARY KEY,
    datum_zahajeni DATE
    skore INT,
    FOREIGN KEY (id_hrace) REFERENCES hrac(id_hrace),
    FOREIGN KEY (id_hry) REFERENCES hra(id_hry)
);

-- Tabulka pro hru
CREATE TABLE hra (
    id_hry INT PRIMARY KEY,
    nazev_hry VARCHAR(50),
    datum_zahajeni DATE
);
