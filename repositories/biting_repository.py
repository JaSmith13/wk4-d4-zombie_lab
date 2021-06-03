from db.run_sql import run_sql
from models.biting import Biting

from repositories import zombie_repository, human_repository

def save(biting):
    sql = "INSERT INTO  bitings (zombie_id, human_id) VALUES (%s, %s) RETURNING id"
    values =[biting.zombie.id, biting.human.id]
    results = run_sql(sql, values)
    biting.id = results[0]['id']
    return biting

def select_all():
    bitings = []

    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for row in results:
        zombie = zombie_repository.select(row['zombie_id'])
        human = human_repository.select(row['human_id'])
        bite = Biting(zombie, human, row['id'])
        bitings.append(bite)
    return bitings

def select(id):
    bite = None

    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        zombie = zombie_repository.select(result['zombie_id'])
        human = human_repository.select(result['human_id'])
        bite = Biting(zombie, human, result['id'])
    return bite


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

#def delete(id):

