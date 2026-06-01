from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import uvicorn
import os
app=FastAPI()
class Prompt(BaseModel):
    prompt:str
@app.get("/")
def rad_root():
    return{"Hello":"world"}
@app.post("/generate")
def generate_text(prompt:Prompt):
    try:
        ollama_host=os.getenv("OLLAMA_HOST","http://localhost:11434")
        ollama_model=os.getenv("OLLAMA_MODEL","gemma3:1b")
        print(ollama_host,ollama_model)
        response=requests.post(
            f"{ollama_host}/api/generate", #f-string for host
            json={"model":ollama_model,"prompt":prompt.prompt},
            stream=True,
            timeout=120 #give model time to respond
        )
        response.raise_for_status() #raise exception for http errors
        output=""
        for line in response.iter_lines():
            if line:
                data=line.decode("utf-8").strip()
                if data.startswith("data: "):
                    data=data[len("data: "):]
                if data=="[DONE]":
                    break
                try:
                    chunk=json.loads(data)
                    output +=chunk.get("response") or chunk.get("text") or ""
                except json.JSONDecodeError:
                    print(f"Warning:could not decode JSON from line: {data}") #for debugging
                    continue
        return {"response":output.strip() or "(Empty response from model)"}
    except requests.RequestException as e:
        return{"error":f"Olama request failed:{str(e)}"}
if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)