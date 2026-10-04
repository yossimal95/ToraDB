from flask import Blueprint, request, jsonify
from infrastructure.data_access import DataAccess

api_bp = Blueprint('api', __name__)

# 1. sp_get_all_characters
@api_bp.route('/characters', methods=['GET'])
def get_all_characters():
    query = """
    SELECT 
        c.character_id, 
        c.main_name_he, 
        c.main_name_en, 
        c.father_id, 
        c.mother_id, 
        c.age_at_death,
        f.main_name_he AS father_name,
        m.main_name_he AS mother_name,
        (SELECT GROUP_CONCAT(a.alias_name_he, ', ') FROM character_aliases a WHERE a.character_id = c.character_id) AS aliases,
        (SELECT GROUP_CONCAT(child.main_name_he, ', ') FROM characters child WHERE child.father_id = c.character_id OR child.mother_id = c.character_id) AS children,
        (SELECT GROUP_CONCAT(spouse.main_name_he, ', ') 
         FROM marriages mar
         JOIN characters spouse ON (mar.husband_id = c.character_id AND spouse.character_id = mar.wife_id) 
                                OR (mar.wife_id = c.character_id AND spouse.character_id = mar.husband_id)
        ) AS spouses
    FROM characters c
    LEFT JOIN characters f ON c.father_id = f.character_id
    LEFT JOIN characters m ON c.mother_id = m.character_id;
    """
    result = DataAccess.execute_read(query)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify(result)

# 2. sp_add_character
@api_bp.route('/characters/add', methods=['POST'])
def add_character():
    data = request.json or {}
    query = """
    INSERT INTO characters (main_name_he, main_name_en, father_id, mother_id, age_at_death)
    VALUES (:main_name_he, :main_name_en, :father_id, :mother_id, :age_at_death);
    """
    params = {
        "main_name_he": data.get("main_name_he"),
        "main_name_en": data.get("main_name_en"),
        "father_id": data.get("father_id"),
        "mother_id": data.get("mother_id"),
        "age_at_death": data.get("age_at_death")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 3. sp_add_character_alias
@api_bp.route('/aliases/add', methods=['POST'])
def add_character_alias():
    data = request.json or {}
    query = """
    INSERT INTO character_aliases (character_id, alias_name_he, alias_name_en)
    VALUES (:character_id, :alias_name_he, :alias_name_en);
    """
    params = {
        "character_id": data.get("character_id"),
        "alias_name_he": data.get("alias_name_he"),
        "alias_name_en": data.get("alias_name_en")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 4. sp_update_character_alias
@api_bp.route('/aliases/update', methods=['POST'])
def update_character_alias():
    data = request.json or {}
    query = """
    UPDATE character_aliases
    SET alias_name_he = :alias_name_he,
        alias_name_en = :alias_name_en
    WHERE alias_id = :alias_id;
    """
    params = {
        "alias_id": data.get("alias_id"),
        "alias_name_he": data.get("alias_name_he"),
        "alias_name_en": data.get("alias_name_en")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 5. sp_update_character_details
@api_bp.route('/characters/update', methods=['POST'])
def update_character_details():
    data = request.json or {}
    query = """
    UPDATE characters
    SET main_name_he = :main_name_he,
        main_name_en = :main_name_en,
        father_id = :father_id,
        mother_id = :mother_id,
        age_at_death = :age_at_death
    WHERE character_id = :character_id;
    """
    params = {
        "character_id": data.get("character_id"),
        "main_name_he": data.get("main_name_he"),
        "main_name_en": data.get("main_name_en"),
        "father_id": data.get("father_id"),
        "mother_id": data.get("mother_id"),
        "age_at_death": data.get("age_at_death")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 6. sp_add_marriage
@api_bp.route('/marriages/add', methods=['POST'])
def add_marriage():
    data = request.json or {}
    query = """
    INSERT INTO marriages (husband_id, wife_id)
    VALUES (:husband_id, :wife_id);
    """
    params = {
        "husband_id": data.get("husband_id"),
        "wife_id": data.get("wife_id")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 7. sp_update_marriage
@api_bp.route('/marriages/update', methods=['POST'])
def update_marriage():
    data = request.json or {}
    query = """
    UPDATE marriages
    SET husband_id = :husband_id,
        wife_id = :wife_id
    WHERE marriage_id = :marriage_id;
    """
    params = {
        "marriage_id": data.get("marriage_id"),
        "husband_id": data.get("husband_id"),
        "wife_id": data.get("wife_id")
    }
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 8. sp_delete_character_alias
@api_bp.route('/aliases/delete', methods=['POST'])
def delete_character_alias():
    data = request.json or {}
    query = """
    DELETE FROM character_aliases
    WHERE alias_id = :alias_id;
    """
    params = {"alias_id": data.get("alias_id")}
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 9. sp_delete_marriage
@api_bp.route('/marriages/delete', methods=['POST'])
def delete_marriage():
    data = request.json or {}
    query = """
    DELETE FROM marriages
    WHERE marriage_id = :marriage_id;
    """
    params = {"marriage_id": data.get("marriage_id")}
    result = DataAccess.execute_write(query, params)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True, "rows_affected": result})

# 10. sp_delete_character
@api_bp.route('/characters/delete', methods=['POST'])
def delete_character():
    data = request.json or {}
    # 2 queries for complete deletion due to manual cascading for marriages
    queries = [
        (
            """
            DELETE FROM marriages 
            WHERE husband_id = :character_id OR wife_id = :character_id;
            """,
            {"character_id": data.get("character_id")}
        ),
        (
            """
            DELETE FROM characters 
            WHERE character_id = :character_id;
            """,
            {"character_id": data.get("character_id")}
        )
    ]
    result = DataAccess.execute_transaction(queries)
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify({"success": True})

# 11. sp_get_character_by_id
@api_bp.route('/characters/get', methods=['GET'])
def get_character_by_id():
    character_id = request.args.get('character_id')
    query = """
    SELECT character_id, main_name_he, main_name_en, father_id, mother_id, age_at_death 
    FROM characters
    WHERE character_id = :character_id;
    """
    result = DataAccess.execute_read(query, {"character_id": character_id})
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify(result)

# 12. sp_get_character_aliases
@api_bp.route('/characters/aliases', methods=['GET'])
def get_character_aliases():
    character_id = request.args.get('character_id')
    query = """
    SELECT alias_id, alias_name_he, alias_name_en
    FROM character_aliases
    WHERE character_id = :character_id;
    """
    result = DataAccess.execute_read(query, {"character_id": character_id})
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify(result)

# 13. sp_get_character_children
@api_bp.route('/characters/children', methods=['GET'])
def get_character_children():
    parent_id = request.args.get('parent_id')
    query = """
    SELECT character_id, main_name_he, main_name_en, father_id, mother_id, age_at_death 
    FROM characters
    WHERE father_id = :parent_id OR mother_id = :parent_id;
    """
    result = DataAccess.execute_read(query, {"parent_id": parent_id})
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify(result)

# 14. sp_get_character_spouses
@api_bp.route('/characters/spouses', methods=['GET'])
def get_character_spouses():
    character_id = request.args.get('character_id')
    query = """
    SELECT 
        m.marriage_id,
        CASE WHEN m.husband_id = :character_id THEN m.wife_id ELSE m.husband_id END AS spouse_id,
        c.main_name_he AS spouse_name_he,
        c.main_name_en AS spouse_name_en
    FROM marriages m
    JOIN characters c ON c.character_id = (CASE WHEN m.husband_id = :character_id THEN m.wife_id ELSE m.husband_id END)
    WHERE m.husband_id = :character_id OR m.wife_id = :character_id;
    """
    result = DataAccess.execute_read(query, {"character_id": character_id})
    if isinstance(result, dict) and "error" in result:
        return jsonify(result), 500
    return jsonify(result)
