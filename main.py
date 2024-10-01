from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the raccoon facts API"}

v0_facts = [
    "President Coolidge had a pet raccoon named Rebecca",
    "Raccoons do not hibernate.",
    "Raccoons can make a variety of noises, even as babies: churr, growl, hiss, and snort",
    "Raccoons can live up to 16 years in the wild but most die before reaching five years.",
    "Sprinkling a layer of cayenne on the ground is one way to deter raccoons."
]

v1_facts = [
    "Raccoons have no known natural enemies or predators, but studies have found they have a slight fear of great white sharks, who, ironically, fear them even more.",
    "Raccoons are the cheapest mammals. A raccoon will use the same toothbrush for ten years rather than buy a new toothbrush.",
    "Racoons get their name from their habit of wearing tennis racquets on their feet during winter.",
    "raccoons are like goldfish in that they have no max size and will continue to grow throughout their lives",
    "German raccoons have a notably different scent from American raccoons, generally described as mustard-y.",
]

@app.get("/v0/fact/")
async def get_fact():
    return random.choice(v0_facts)

@app.get("/v1/fact/")
async def get_fact():
    return random.choice(v1_facts)