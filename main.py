import fastapi as fa
import uvicorn

app = fa.FastAPI()

@app.get("/")
def main():
  return "Hello World!"

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8080)
