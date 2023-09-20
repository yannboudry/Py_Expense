from PyInquirer import prompt

user_questions = [
    {
        "type": "input",
        "name": "name",
        "message": "New user - Name :"
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('./users.csv', 'r+') as f:
        urs = f.read().splitlines()
        if infos['name'] in urs:
            print("User already exists")
            return
        f.writelines("\n" + infos["name"])
    return

def get_user(results):
    with open('./users.csv', 'r') as f:
        return f.read().splitlines()

def get_involved(result):
    with open('./users.csv', 'r') as f:
        involved = []
        for u in f.read().splitlines():
            if u != result['spender']:
                involved.append({"name": u})
        #involved.remove(result['spender'])
    return involved
