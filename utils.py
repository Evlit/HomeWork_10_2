import json
from Classes import Applicant


def load_candidates(file):
    """
    Загрузка из jason файла
    """
    with open(file, 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text


def get_all():
    """
    Получение всего списка кандидатов
    """
    candidates = []
    data = load_candidates('candidates.json')
    for candidate in data:
        candidates.append(Applicant(candidate['pk'], candidate['name'], candidate['position'],
                                    candidate['skills'].lower(), candidate['picture']))
    return candidates


def get_by_pk(pk, candidates):
    """
    Получение кандидата по номеру
    """
    for candidate in candidates:
        if candidate.pk == pk:
            return candidate


def get_by_skill(skill_name, candidates):
    """
    Получение списка кандидатов по навыку
    """
    candidate_skills = []
    for candidate in candidates:
        if skill_name in candidate.skills:
            candidate_skills.append(candidate)
    return candidate_skills
