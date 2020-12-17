from fastapi import FastAPI, File

from models import Counter

app = FastAPI(title="Word Counter as a Service",
              description="Count number of words in texts",
              version="0.1.0")


def count_words(text):
    counter = 0
    prev_char = ''
    spaces = [' ', '\t', '\n']

    # increment counter between words
    for char in text:
        if char in spaces and prev_char not in spaces:
            counter += 1
        prev_char = char

    # if text ends without space, the last thing is a word
    if prev_char not in spaces:
        counter +=1

    return counter


@app.get("/words", response_model=Counter)
async def words_in_string(text: str):
    return {"words": count_words(text)}


@app.post("/words", response_model=Counter)
async def words_in_file(aFile: bytes = File(...)):
    return {"words": count_words(aFile.decode())}
