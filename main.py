from parserbs import soupy
from conn import connection
import os, time, threading, datetime

def starter():

    start_input = input('Ingrese moneda: ')

    if start_input.lower() == 'usd':
        return 'USD'
    elif start_input.lower() == 'eur':
        return 'EUR'
    else:
        print('Error leyendo la moneda.')
        time.sleep(4)
        os.system('clear')
        program()

def data(crypto, conversion):
    return soupy(connection(f'https://www.bolsamania.com/criptodivisa/{crypto}-{conversion}'), conversion, crypto)

def program():

    conversion = starter()
    cryptos = {
        'BTC':'BTC',
        'ETH':'ETH',
        'LTC':'LTC',
        'XRP':'XRP'
    }
    threads = list()

    counter = 0

    if conversion != None:
        os.system('clear')
        while True:
            for items in cryptos:
                t = threading.Thread(target=data, args=(cryptos[items], conversion), daemon=True)
                t.start()
                threads.append(t)
                time.sleep(0.5)

            for thread in threads:
                thread.join()
            
            counter += 1
            time.sleep(5)
            print()

            if counter == 10 : os.system('clear')
            

    else:
        print('Error')
        time.sleep(4)
        os.system('clear')
        program()

try:
    program()
except KeyboardInterrupt:
    print("\b\bEl programa finalizo")
    os.system('clear')
    exit()
    