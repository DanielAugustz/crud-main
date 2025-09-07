from fastapi import APIRouter
from app.database import get_db 

router = APIRouter(prefix="/alunos", tags=["alunos"])

@router.post("/")
def criar_aluno(aluno: dict):
    db = get_db()
    result = db.alunos.insert_one(aluno)
    return {"id": str(result.inserted_id)}


@router.get("/")
def listar_alunos():
    db = get_db()
    alunos = list(db.alunos.find())
    for a in alunos:
        a["_id"] = str(a["_id"])
    return alunos


@router.put("/{nome}")
def atualizar_aluno(nome: str, aluno: dict):
    db = get_db()
    result = db.alunos.update_one({"nome": nome}, {"$set": aluno})
    return {"modificados": result.modified_count}


@router.delete("/{nome}")
def deletar_aluno(nome: str):
    db = get_db()
    result = db.alunos.delete_one({"nome": nome})
    return {"deletados": result.deleted_count}
