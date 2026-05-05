# ToraDB
The Torah Characters &amp; Genealogy Database

# Tables
```
CREATE TABLE Characters (
    CharacterID INT PRIMARY KEY IDENTITY(1,1),
	MainNameHe NVARCHAR(100) NOT NULL,
    MainNameEn NVARCHAR(100) NULL,  
    FatherID INT NULL,
    MotherID INT NULL,
	AgeAtDeath INT NULL,

    CONSTRAINT FK_Father FOREIGN KEY (FatherID) REFERENCES Characters(CharacterID),
    CONSTRAINT FK_Mother FOREIGN KEY (MotherID) REFERENCES Characters(CharacterID)
);

CREATE TABLE CharacterAliases (
    AliasID INT PRIMARY KEY IDENTITY(1,1),
    CharacterID INT NOT NULL,
    AliasNameHe NVARCHAR(100) NOT NULL, 
    AliasNameEn NVARCHAR(100) NULL, 
     
    CONSTRAINT FK_CharacterAlias FOREIGN KEY (CharacterID) 
    REFERENCES Characters(CharacterID) ON DELETE CASCADE
);

CREATE TABLE Marriages (
    MarriageID INT PRIMARY KEY IDENTITY(1,1),
    HusbandID INT NOT NULL, 
    WifeID INT NOT NULL,    

    CONSTRAINT FK_Husband FOREIGN KEY (HusbandID) 
    REFERENCES Characters(CharacterID) ON DELETE NO ACTION,
    
    CONSTRAINT FK_Wife FOREIGN KEY (WifeID) 
    REFERENCES Characters(CharacterID) ON DELETE NO ACTION
);
```

# Fix Hebrew issues
```
ALTER TABLE [Characters] 
ALTER COLUMN MainNameHe NVARCHAR(100) COLLATE Hebrew_CI_AS NOT NULL;
דגכדגכדגכ#
נרנררנררנרנ#
נרנרנ

ALTER TABLE [CharacterAliases] 
ALTER COLUMN AliasNameHe NVARCHAR(100) COLLATE Hebrew_CI_AS NOT NULL;
```
