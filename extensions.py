from config import APIKEY,keys

import requests

class ConvertionException(Exception):
    pass

class Convertion:
    @staticmethod
    def convert(quote:str, base:str, amount:str):


        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты:{base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'http://apilayer.net/api/live?access_key={APIKEY}&currencies={quote_ticker}&source={base_ticker}&format=1')
        key = base_ticker+quote_ticker
        total_base = str(r.json()['quotes'][key]*amount)


        return total_base
