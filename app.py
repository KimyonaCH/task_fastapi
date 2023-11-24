from fastapi import FastAPI, Query
from fastapi.routing import APIRouter
from func.aio_eval import evaluate
from fastapi.responses import HTMLResponse, RedirectResponse
from templates.status import get_page
from fastapi.staticfiles import StaticFiles

router = APIRouter()
db = {}

app = FastAPI()


@router.post("/create")
async def create_task(x: int,
                      y: int,
                      operator: str = Query(..., description="Оператор (+, -, *, /)", regex="[-+*/]")):
    task_id = len(db) + 1
    db[task_id] = {"task": evaluate(x, y, operator),
                   "details": " ".join(map(str, [x, operator, y])),
                   "status": "Pending"}

    return "[DONE] Task completely create"


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs", status_code=301)


@router.post("/execute")
async def execute_task(task_id: int):
    if task_id not in db:
        return {"msg": "Error while executing", "details": f"task ({task_id}) doesn't exists"}
    elif db[task_id]["status"] == "Complete":
        return {"msg": "Error while executing", "details": f"task ({task_id}) already completed"}

    res = await db[task_id]["task"]
    db[task_id]["status"] = "Complete"
    return {"result": res,
            "details": db[task_id]["details"]}


@router.get("/status", response_class=HTMLResponse)
async def show_status_tasks():
    return get_page(db)


app.mount("/images", StaticFiles(directory="images"), name="images")
app.include_router(router, prefix="/v1")
