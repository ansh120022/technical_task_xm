from fastapi import FastAPI, HTTPException

app = FastAPI()


def server_response() -> str:
    return {"field1": "same json", "field2": "for any ID passed"}


@app.get("/people/{person_id}/", status_code=200)
def get_person(person_id: int):
    if person_id not in range(1, 100):
        raise HTTPException(
            status_code=404, detail=f"Person with ID {person_id} not found"
        )
    return server_response()


@app.get("/planets/{planet_id}/", status_code=200)
def get_planet(planet_id: int):
    if planet_id not in range(1, 100):
        raise HTTPException(
            status_code=404, detail=f"Planet with ID {planet_id} not found"
        )
    return server_response()


@app.get("/starships/{starship_id}/", status_code=200)
def get_starship(starship_id: int):
    if starship_id not in range(1, 100):
        raise HTTPException(
            status_code=404, detail=f"Starship with ID {starship_id} not found"
        )
    return server_response()
