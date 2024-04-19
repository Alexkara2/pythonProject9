import sqlite3
import requests
from bs4 import BeautifulSoup

connection = sqlite3.connect("links.sl3", 5)#Спроба входа у ДБ
cursor = connection.cursor()#через цю змінну встановлюється дія

#cursor.execute("CREATE TABLE models (links TEXT);") - створити тблицю models з колонмками links
#cursor.execute("INSERT INTO models (links) VALUES ('https://tsk.ua/ua/katalog-avtomobiliv/tesla-model-s-plaid/');")-добавити до колонки значення
#cursor.execute("INSERT INTO models (links) VALUES ('https://tsk.ua/ua/katalog-avtomobiliv/tesla-model-3-eu-new!/');")-добавити до колонки значення
#cursor.execute("INSERT INTO models (links) VALUES ('https://tsk.ua/ua/katalog-avtomobiliv/tesla-model-x-longrange-dualmotor-eu-new!/');") -добавити до колонки значення

cursor.execute("SELECT links FROM models;")#вибрати всі значіння з колнки
result = cursor.fetchall()#забрати всі значіння з колнки

choice_model = int(input("Choice model [models=0, model3=1, modelx=2]:"))
model=list(result[choice_model])#перетворення Tuple у list
model=model[0]#це потбіно для прибирання лапок, бо перше значення знаходится в них

try:#спробувати виконати код
    request = requests.get(model)#запрос до сайту
    if request.status_code==200:#підтведження відкриття сайту
        soup = BeautifulSoup(request.text, features="html.parser")#задається значення яку ми функцію хочимо
        soup1 = soup.find_all(class_="autotesla__item__cena__end")#виділити код з такою позначкою
        print(f"Price:{soup1}")#Виводиться цінник
    else:
        raise NameError
except:#якщо не спрацбвав код то
    print("Error with site")
connection.commit()#підтвердити дії в БД
connection.close()#закрити зв'язок з БД