import uvicorn

from fastapi import FastAPI

from core.api.v1.handlers.task_handlers import router as task_router


app = FastAPI()

app.include_router(task_router)

@app.get('/')
async def main():
    return {'message': 'Hello World'}



if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)