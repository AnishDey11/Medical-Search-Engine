from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend import (
    search,
    get_page_content,
    get_page_rank_data,
    get_graph
)


app = FastAPI(
    title="Medical Research Search Engine"
)

templates = Jinja2Templates(
    directory="templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/search")
async def search_api(q: str):

    if not q.strip():
        return []

    return search(q)


@app.get("/page/{page}", response_class=HTMLResponse)
async def page_view(request: Request, page: str):

    content = get_page_content(page)

    return templates.TemplateResponse(
        request=request,
        name="page.html",
        context={
            "request": request,
            "page": page,
            "content": content
        }
    )


@app.get("/analysis", response_class=HTMLResponse)
async def analysis_view(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="analysis.html",
        context={
            "request": request
        }
    )


@app.get("/analysis-data")
async def analysis_data():

    return {
        "page_rank": get_page_rank_data(),
        "graph": get_graph()
    }



