# ToraDB
The Torah Characters & Genealogy Database

## About
This project is a relational database for Torah characters, their family trees, and aliases, implemented using **SQLite**.

### Naming Conventions & Best Practices
- **Tables and Columns**: We use `snake_case` (e.g., `characters`, `main_name_he`), which is the universally accepted standard and best practice for SQL databases. It improves readability and prevents syntax issues across different database engines.
- **Hebrew Support**: SQLite natively stores text in UTF-8 encoding. Unlike SQL Server, there is no need for `NVARCHAR` or special collations (like `Hebrew_CI_AS`). You can store Hebrew characters directly in standard `TEXT` columns seamlessly.

---

## Getting Started: Creating the Database

To create the SQLite database and enable foreign key constraints, run the following in your terminal:

```bash
# Create a new SQLite database file
sqlite3 torah.db
```

Once inside the SQLite prompt, ensure foreign keys are enabled (SQLite disables them by default for backward compatibility):
```sql
PRAGMA foreign_keys = ON;
```

---

## Tables Creation

```sql
CREATE TABLE characters (
    character_id INTEGER PRIMARY KEY AUTOINCREMENT,
    main_name_he TEXT NOT NULL,
    main_name_en TEXT,  
    father_id INTEGER,
    mother_id INTEGER,
    age_at_death INTEGER,

    CONSTRAINT fk_father FOREIGN KEY (father_id) REFERENCES characters(character_id),
    CONSTRAINT fk_mother FOREIGN KEY (mother_id) REFERENCES characters(character_id)
);

CREATE TABLE character_aliases (
    alias_id INTEGER PRIMARY KEY AUTOINCREMENT,
    character_id INTEGER NOT NULL,
    alias_name_he TEXT NOT NULL, 
    alias_name_en TEXT, 
     
    CONSTRAINT fk_character_alias FOREIGN KEY (character_id) 
    REFERENCES characters(character_id) ON DELETE CASCADE
);

CREATE TABLE marriages (
    marriage_id INTEGER PRIMARY KEY AUTOINCREMENT,
    husband_id INTEGER NOT NULL, 
    wife_id INTEGER NOT NULL,    

    CONSTRAINT fk_husband FOREIGN KEY (husband_id) 
    REFERENCES characters(character_id) ON DELETE NO ACTION,
    
    CONSTRAINT fk_wife FOREIGN KEY (wife_id) 
    REFERENCES characters(character_id) ON DELETE NO ACTION
);
```

---

## Examples

### ⭐ Returns character (אדם) children count and names
*Note: We use `GROUP_CONCAT` in SQLite instead of SQL Server's `STRING_AGG`.*

```sql
SELECT 
    f.main_name_he,
    COUNT(c.character_id) AS children_count,
    GROUP_CONCAT(c.main_name_he, ', ') AS children_names
FROM characters AS c
INNER JOIN characters AS f 
    ON f.character_id = c.father_id
WHERE f.main_name_he = 'אדם'
GROUP BY f.main_name_he;
```
<img width="295" height="71" alt="image" src="https://github.com/user-attachments/assets/61365e9d-141f-43dd-b5ff-0e1d745b78e2" />

### ⭐ Returns characters with parents’ names

```sql
SELECT 
    c.character_id,
    c.main_name_he AS child_name,
    f.main_name_he AS father_name,
    m.main_name_he AS mother_name
FROM characters AS c
LEFT JOIN characters AS f
    ON c.father_id = f.character_id
LEFT JOIN characters AS m
    ON c.mother_id = m.character_id;
```
<img width="332" height="142" alt="image" src="https://github.com/user-attachments/assets/3bd5ab1d-543a-45e9-af62-11b7ea3bd261" />

### ⭐ Returns husbands and wives names

```sql
SELECT 
    h.main_name_he AS husband_he,
    h.main_name_en AS husband_en,
    w.main_name_he AS wife_he,
    w.main_name_en AS wife_en
FROM marriages AS m
JOIN characters AS h 
    ON m.husband_id = h.character_id 
JOIN characters AS w 
    ON m.wife_id = w.character_id;
```
<img width="288" height="67" alt="image" src="https://github.com/user-attachments/assets/d98b05dc-1ad7-4f52-aefb-79a303ca5ec2" />
