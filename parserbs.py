from bs4 import BeautifulSoup

def soupy(html, convertion, crypto):

    soup = BeautifulSoup(html, 'html.parser')

    try:
        price = soup.find('span', {'subscription': f'5~CCCAGG~{crypto}~{convertion}~PRICE'}).text.strip()
        difference = soup.find('span', {'subscription': f'5~CCCAGG~{crypto}~{convertion}~CHANGE24HOUR'}).span.text.strip()
        prcnt = soup.find('span', {'subscription': f'5~CCCAGG~{crypto}~{convertion}~CHANGEPCT24HOUR'}).span.text.strip()

        float_diff = difference.replace('.', '').replace(',', '.').replace('$', '').replace('€', '')

        if float(float_diff) > 0:
            print("\033[0;32m"+f'{crypto}: {price}    {difference}     {prcnt}')
        elif float(float_diff) < 0:
            print("\033[0;31m"+f'{crypto}: {price}    {difference}     {prcnt}')
        else:
            print("\033[0;33m"+f'{crypto}: {price}    {difference}     {prcnt}')

    except:
        print('No se pudo encontrar los datos en la pagina')
    
