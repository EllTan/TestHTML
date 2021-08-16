from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import insta.svg
import vk.svg


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def read_items():
    return  """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Дмитрий Жарков - разработчик</title>
            <link
            href="https://fonts.googleapis.com/css?family=Roboto:400,700&display=swap&subset=cyrillic"
            rel="stylesheet"
            />
            <link rel="stylesheet" href="css/style.css" />
            <link rel="stylesheet" href="/css/animate.css" />
            <link rel="stylesheet" href="css/swiper-bundle.min.css" />
        </head>
        <body>
        <header class="hero">
      <div class="container">
        <div class="hero-header">          
          <div class="social-links">            
            <a
              href="https://www.instagram.com/angelina_kalinovskaya_/"
              target="_blank"
              class="social-link"
              ><img src="social/insta.svg" alt="instagram"
            /></a>
            <a href="https://vk.com/angel.kalina" target="_blank" class="social-link"
              ><img src="social/vk.svg" alt="vk"
            /></a>
          </div>
          <!-- /.social-links -->
        </div>
        <!-- /.hero-header -->
        <!-- /.hero-text -->
        <div class="hero-avatar"></div>
          <!-- /.hero-avatar -->
        </div>
        <!-- /.hero-content -->
      </div>
      <!-- /.container -->
    </header>   
  </body>
</html>
        """
    