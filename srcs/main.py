import uvicorn
import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)