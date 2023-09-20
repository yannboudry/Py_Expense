from PyInquirer import prompt
from user import get_user, get_involved
import json

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_user
    },
    {
        "type": "checkbox",
        "qmark": "-",
        "name": "involved",
        "message": "New Expense - Involved",
        "choices": get_involved
    }
]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('./users.csv', 'r') as f:
        users = f.read().splitlines()
        if infos['spender'] not in users:
            print('User does not exist')
            return False

    with open('./expense_report.csv', 'r+') as f:
        try:
            expenses = json.load(f)
            expenses['data'].append(
                {
                    "amount": infos['amount'],
                    "label": infos['label'],
                    "spender": infos['spender'],
                    "involved": infos['involved']
                })
            f.seek(0)
            json.dump(expenses, f, indent=4)
        except json.decoder.JSONDecodeError:
            expenses = {'data': [
                {
                    "amount": infos['amount'],
                    "label": infos['label'],
                    "spender": infos['spender'],
                    "involved": infos['involved']
                }]}
            json.dump(expenses, f, indent=4)
    print("Expense Added !")
    return True


