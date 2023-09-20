from PyInquirer import prompt
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
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },

]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('./expense_report.csv', 'r+') as f:
        try:
            expenses = json.load(f)
            print(expenses)
            expenses['data'].append(
                {
                    "amount": infos['amount'],
                    "label": infos['label'],
                    "spender": infos['spender']
                })
            f.seek(0)
            json.dump(expenses, f, indent=4)
        except json.decoder.JSONDecodeError:
            expenses = {'data': [
                {
                    "amount": infos['amount'],
                    "label": infos['label'],
                    "spender": infos['spender']
                }]}
            json.dump(expenses, f, indent=4)
    print("Expense Added !")
    return True


