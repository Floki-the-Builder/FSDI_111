from app.database import get_db


def output_formatter(results):
    out = []
    for result in results:
        user = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "hobbies": result[3],
            "active": result[4]
        }
        out.append(user)
    return out


def scan():
    cursor = get_db().execute(
        "SELECT * FROM user WHERE active=1", ()
    )
    result = cursor.fetchall()
    cursor.close()
    return output_formatter(result)


def select_by_id(pk):
    cursor = get_db().execute(
        "SELECT * FROM user WHERE id=? AND active=1",
        (pk, )
    )
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def insert(user_dict):
    value_tuple = (
        user_dict.get("fisrt_name"),
        user_dict.get("last_name"),
        user_dict.get("hobbies")
    )
    statement = """
            INSERT INTO user (
                first_name,
                last_name,
                hobbies
            ) VALUES (?,?, ?)
    """

    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close


def update(pk, user_data):
    value_tuple = (
        user_data.get("fisrt_name"),
        user_data.get("last_name"),
        user_data.get("hobbies"),
        pk
    )
    statement = """
            UPDATE user 
            SET first_name=?,
            last_name=?,
            hobbies=?
            WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close


def deactivate(pk):
    cursor = get_db()
    cursor.execute("UPDATE user SET active=0 WHERE id=?", (pk,))
    cursor.commit()
    cursor.close()
