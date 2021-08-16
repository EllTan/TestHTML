from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import insta.svg
import vk.svg


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def read_items():
    return  """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <a
              href="https://www.instagram.com/angelina_kalinovskaya_/"
              target="_blank"
              class="social-link"
              ><img src="social/insta.svg" alt="instagram"
            /></a>
            <a href="https://vk.com/angel.kalina" target="_blank" class="social-link"
              ><img src="social/vk.svg" alt="vk"
            /></a>
        </body>
    </html>
    """