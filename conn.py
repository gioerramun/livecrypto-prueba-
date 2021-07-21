import requests

def connection(url):

    try:
        page_conn = requests.get(url)
    except:
        print('No se pudo conectar con la pagina')
        exit()

    html = page_conn.text

    return html