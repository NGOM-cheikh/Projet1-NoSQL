from fastapi import APIRouter
from service import eleve_service
from schema.eleve_schema import EleveUpdateSchema, EleveInsertSchema

# Initailisation du router
router = APIRouter(
    prefix="/eleve",
    tags=["Eleve"]
)

# Ajout d'une fonction permettant d'afficher un element de la BDD
@router.get("/{id}")
def get_one_eleve(id):
    return eleve_service.get_one(id)

# Ajout d'une fonction permettant d'afficher les eleves selon le choix d'une classe
@router.get("/q3_eleve_choose_classe/{idclasse}")
def get_eleve_choose_classe(idclasse):
    return eleve_service.get_eleve_choose_classe(idclasse)

# Ajout d'une fonction permettant d'afficher plusieurs elements de la BDD
@router.get("/")
def get_all_eleve():
    return eleve_service.get_all()

# Ajout d'une fonction permettant d'inserer un element de la BDD
@router.post("/one", response_model=dict)
def create_one_eleve(item: EleveInsertSchema):
    item_dict = item.dict(exclude_unset=True)  # On exclut les donnees de type None (= donnees non renseignees)
    results = eleve_service.create_one(item_dict)
    return {"acknowledged": str(results.acknowledged)}

# Ajout d'une fonction permettant d'inserer plusieurs elements de la BDD
@router.post("/many")
def create_many_eleve(item):
    return eleve_service.create_many(item)

# Ajout d'une fonction permettant de mettre a jour la classe d'un eleve de la BDD
@router.patch("/one/{id_eleve}", response_model=dict)
def update_one_eleve(id_eleve, update: EleveUpdateSchema):
    update_dict = update.dict(exclude_unset=True)   # On exclut les donnees de type None (= donnees non renseignees)
    results = eleve_service.update_one(id_eleve, update_dict)
    return {"modified_count": results.modified_count}


"""
# Ajout d'une fonction permettant de mettre a jour plusieurs elements de la BDD
@router.patch("/many")
def update_many_eleve(filter, newValue):
    return eleve_service.update_many(filter, newValue)
"""
# Ajout d'une fonction permettant de supprimer un element de la BDD
@router.delete("/one/{id}")
def delete_one_eleve(id):
    return eleve_service.delete_one(id)

# Ajout d'une fonction permettant de supprimer plusieurs elements de la BDD
@router.delete("/many/{item}")
def delete_many_eleve(item):
    return eleve_service.delete_many(item)

