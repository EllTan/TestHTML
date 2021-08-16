from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import insta.svg
import vk.svg


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def handler():
    return 
        """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    