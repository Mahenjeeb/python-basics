import uvicorn

def main():
    uvicorn.run("server:app", port=8080, host="localhost", reload=True)
    
if __name__ == "__main__":
    main()