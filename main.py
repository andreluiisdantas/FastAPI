from fastapi import FastAPI, HTTPException, status, Response
from models import PersonagemToyStory
from typing import Optional

app = FastAPI() #Variavel para instanciar o FastAPI() e não precisar escrever o FastAPI e sim apenas o app

personagens = {
    1 : {
        "nome": "Woody",
        "dono": "Andy",
        "tamanho": "Pequeno",
        "foto": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXWSeP51Sjci5BPAZH0mNRv05I69SgKX6i2qFP_Tl-hKWJ1f3Qkd-ACpnxTTsvJqq4h2Q&usqp=CAU"
    },

    2 : {
        "nome": "Buzz Lighter",
        "dono": "Bonnie",
        "tamanho": "Pequeno",
        "foto": "https://toysonejapan.com/cdn/shop/files/s-l1600_2_5e5bd360-d10b-40be-a1ce-2318e54b4147_700x700.webp?v=1736510757"
    }
}

@app.get("/")
async def raiz():
    return {"Mensagem": "Hello World!"}  

@app.get("/personagens")
async def get_personagens():
    return personagens

@app.get("/personagens/{personagem_id}")
async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
@app.post("/personagens", status_code=status.HTTP_201_CREATED)
async def post_personagem(personagem: Optional[PersonagemToyStory] = None):
    next_id = len(personagens) + 1
    personagens[next_id] = personagem
    del personagem.id
    return personagem

@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagemToyStory):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")
    
@app.delete("/personagens/{personagem_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)