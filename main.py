# This is a sample Python script.
import json

import requests as rq

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
URL = 'https://camacholab.ee.byu.edu/qrng/decimal/50'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def consulta():
    resultado = rq.get(URL,verify=False,stream=True).text.split(" ")
    #headers=headers)
    print(resultado)
    resultado.pop()
    res = [chr(int(x))  for x in resultado if int(x) in range(48,122)]
    res = "".join(_ for _ in res)




    # Use a breakpoint in the code line below to debug your script.
    return res  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cadena = consulta()
    print(cadena[0:12])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
