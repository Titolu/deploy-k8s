from fastapi import FastAPI
import random

app = FastAPI()


@app.get('/')
async def root():
    return {'Dear': 'Hello World war!, This is Tito first API'}