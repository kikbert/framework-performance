from fastapi import Depends, FastAPI, HTTPException



app = FastAPI()


@app.get("/")
def root():
    return {'root': 'ok'}

@app.get("/test/")
def test():
    return {'test': 'ok'}

@app.get("/test2/")
def test():
    return {'test2': 'ok'}
