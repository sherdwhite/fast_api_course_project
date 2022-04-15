import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from services import report_service

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
async def index(request: Request):
    events = await report_service.get_reports()
    data = {'request': request, 'events': events}

    return templates.TemplateResponse('home/index.html', data)


@router.get('/favicon.ico', include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')

# @api.get('/')
# def index():
#     body = "<html>" \
#            "<body style='padding: 10px;'>" \
#            "<h1>Welcome to the demo API</h1>" \
#            "<div>" \
#            "Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>" \
#            "</div>" \
#            "</body>" \
#            "</html>"
#
#     return fastapi.responses.HTMLResponse(content=body)
#
#
# @api.get('/api/calculate')
# def calculate(x: int, y: int, z: Optional[int] = None):
#     if z == 0:
#         return fastapi.responses.JSONResponse(
#             content={"error": "ERROR: Z cannot be zero."},
#             status_code=400)
#
#     value = x + y
#
#     if z is not None:
#         value /= z
#
#     return {
#         'x': x,
#         'y': y,
#         'z': z,
#         'value': value
#     }