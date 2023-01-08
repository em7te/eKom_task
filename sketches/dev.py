from datetime import datetime
from pprint import pprint

POST_request = 'f_name1=11.11.2011&f_name2=2011-11-11&f_name3=+7 999 999 99 99&f_name4=test@test.ru&' \
               'f_name5=test@test.com&f_name6=abrakadabra1&f_name7=abrakadabra@1&f_name8=2011-11-1s'

# f_name1=11.11.2011&f_name2=2011-11-11&f_name3=+7 999 999 99 99&f_name4=test@test.ru&f_name5=test@test.com
# f_name6=abrakadabra1&f_name7=abrakadabra@1&f_name8=2011-11-1s

types = ['email', 'телефон', 'дата', 'текст']

data = ['DD.MM.YYYY', 'YYYY-MM-DD']
phone = ['+7 xxx xxx xx xx', '+7', 'len = 12', 'split(" ")', 'str(i).isdigit()']
email = ['@', '.ru', '.com']
text = 'str'


request_split = POST_request.split('&')
request_dict = {i.split('=')[0]: i.split('=')[1] for i in request_split}

result_dict = {}
for key in request_dict:
    value = ''.join(request_dict.get(key).split(" "))
    if len(value) == 10:
        try:
            if value.count('.') == 2 and bool(datetime.strptime(value, '%d.%m.%Y')):
                result_dict[key] = 'date'
            elif value.count('-') == 2 and bool(datetime.strptime(value, '%Y-%m-%d')):
                result_dict[key] = 'date'
        except:
            result_dict[key] = 'text'
    elif False not in [el.isdigit() for el in value][1:] and value[0] == '+' and len(value) == 12:
        result_dict[key] = 'phone'
    elif value.count('@') == 1:
        if (value[-3:] == '.ru' and value.count('.ru') == 1) or (value[-4:] == '.com' and value.count('.com') == 1):
            result_dict[key] = 'email'
        else:
            result_dict[key] = 'text'
    else:
        result_dict[key] = 'text'

# for i in result_dict:
#     print(i, result_dict.get(i))
pprint(result_dict)
