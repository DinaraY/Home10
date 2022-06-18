import json


def load_candidates():
    """ Загружает студентов из файла в список """
    with open("candidates.json", 'r', encoding="utf-8") as f:
        candidates = json.load(f)

    return candidates


load_candidates = load_candidates()


def load_name_candidates():
    """ Выводит список кандидатов"""
    spisok = []
    for i in load_candidates:
        spisok.append(
            f"""<pre>Имя кандидата - {i['name']}\nПозиция кандидата {i['position']}\nНавыки {i['skills']}</pre>""")

    return f"{' '.join(spisok)}"


def page_profile(id: int):
    """Выводит информацию о кандидате по id"""
    for i in load_candidates:
        if id == i["id"]:
            return f"""
            <pre>
            <img src="{i["picture"]}">
            Имя кандидата - {i['name']}
            Позиция кандидата {i['position']}
            Навыки {i['skills'].lower()}
            </pre>"""


def page_skills(skill):
    """Выводит кандидатов по навыку"""
    skills = []
    for i in load_candidates:
        if skill.lower() in i["skills"].lower().split(", "):
            skills.append(
                f"""Имя кандидата - {i['name']}\nПозиция кандидата {i['position']}\nНавыки {i['skills']}""")
    return ''.join(skills)



