import json
import copy

def show_status():
    users = []
    with open('./users.csv', 'r') as f:
        for u in f.read().splitlines():
            users.append({u: []})
    print(users)
    with open('./expense_report.csv', 'r') as f:
        exp = json.load(f)

        for transaction in exp['data']:
            amount = transaction['amount']
            per_involved = amount / (len(transaction['involved']) + 1)