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

ALTER TABLE [CharacterAliases] 
ALTER COLUMN AliasNameHe NVARCHAR(100) COLLATE Hebrew_CI_AS NOT NULL;
```

# Examples
### ⭐ Returns character (אדם) children count and names
```
SELECT 
    f.MainNameHe,
    COUNT(c.CharacterID) AS ChildrenCount,
    STRING_AGG(c.MainNameHe, ', ') AS ChildrenNames
FROM [TorahDB].[dbo].[Characters] AS c
INNER JOIN [TorahDB].[dbo].[Characters] AS f 
    ON f.CharacterID = c.FatherID
WHERE f.MainNameHe = N'אדם'
GROUP BY f.MainNameHe;
```
<img width="295" height="71" alt="image" src="https://github.com/user-attachments/assets/61365e9d-141f-43dd-b5ff-0e1d745b78e2" />

### ⭐ Returns characters with parents’ names
```
SELECT 
    c.CharacterID,
    c.MainNameHe AS ChildName,
    f.MainNameHe AS FatherName,
    m.MainNameHe AS MotherName
FROM [TorahDB].[dbo].[Characters] AS c
LEFT JOIN [TorahDB].[dbo].[Characters] AS f
    ON c.FatherID = f.CharacterID
LEFT JOIN [TorahDB].[dbo].[Characters] AS m
    ON c.MotherID = m.CharacterID;
```
<img width="332" height="142" alt="image" src="https://github.com/user-attachments/assets/3bd5ab1d-543a-45e9-af62-11b7ea3bd261" />

### ⭐ Returns husbands and wives names
```
SELECT 
    H.MainNameHe AS HusbandHe,
    H.MainNameEn AS HusbandEn,
    W.MainNameHe AS WifeHe,
    W.MainNameEn AS WifeEn
FROM [TorahDB].[dbo].[Marriages] AS M
JOIN [TorahDB].[dbo].[Characters] AS H 
    ON M.HusbandID = H.CharacterID 
JOIN [TorahDB].[dbo].[Characters] AS W 
    ON M.WifeID = W.CharacterID;
```
<img width="288" height="67" alt="image" src="https://github.com/user-attachments/assets/d98b05dc-1ad7-4f52-aefb-79a303ca5ec2" />







