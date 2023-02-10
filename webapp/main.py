from fastapi import FastAPI, HTTPException, status

app = FastAPI()


def server_response() -> str:
    return {"field1": "same json", "field2": "for any ID passed"}


def validate_id(element_id) -> None:
    try:
        element_id_int = int(element_id)
    except:
        raise HTTPException(
            status_code=400,
            detail=f"Incorrect element ID: {element_id}. The value should be integer"
        )
    if element_id_int not in range(1, 100):
        raise HTTPException(
            status_code=404, detail=f"Record with ID {element_id_int} not found"
        )


@app.get("/people/{person_id}/", status_code=status.HTTP_200_OK)
def get_person(person_id):
    validate_id(person_id)
    return server_response()


@app.get("/planets/{planet_id}/", status_code=200)
def get_planet(planet_id):
    validate_id(planet_id)
    return server_response()


@app.get("/starships/{starship_id}/", status_code=200)
def get_starship(starship_id):
    validate_id(starship_id)
    return server_response()
