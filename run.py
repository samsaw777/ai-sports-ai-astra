# Entry point for application

import uvicorn

if __name__ =="__main__":
    uvicorn.run(
        "src.main:app",
        host="localhost",
        port= 5000,
        reload= True
    )