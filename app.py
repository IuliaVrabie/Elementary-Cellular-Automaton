from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_code', methods=['POST'])
def run_code():
    rule = int(request.form['rule'])
    steps = int(request.form['steps'])
    nr_gen = int(request.form["nr_gen"])
    default_rule = rule
    print(f"rule {rule}")
    print(f"nr gen {nr_gen}")

    def functie(left, curr, right):
        if(left == "@" and curr=="@" and right =="@"):
            return listOfRules[0]
        elif(left == "@" and curr=="@" and right ==" "):
            return listOfRules[1]
        elif (left == "@" and curr == " " and right == "@"):
            return listOfRules[2]
        elif (left == "@" and curr == " " and right == " "):
            return listOfRules[3]
        elif (left == " " and curr == "@" and right == "@"):
            return listOfRules[4]
        elif (left == " " and curr == "@" and right == " "):
            return listOfRules[5]
        elif (left == " " and curr == " " and right == "@"):
            return listOfRules[6]
        else:
            return listOfRules[7]

    def afisareVector(v):
        linie = ""
        for i in v:
            linie = linie + i
        print(linie)
        return linie

    if steps % 2 == 0:
        spaces_before = int(steps/2)
        spaces_after = int(steps/2 - 1)
    else:
        spaces_before = spaces_after = int(steps // 2)

    print(f"steps {steps}: {spaces_before}, @, {spaces_after}")

    generatie = [" "] * spaces_before + ["@"] + [" "] * spaces_after
    print(generatie)

    listOfRules = []

    if rule > 0:
        while rule > 0:
            if rule % 2 == 0:
                listOfRules.insert(0, " ")  # add " " to the 0 pos
            else:
                listOfRules.insert(0, "@")
            rule = rule // 2
        while len(listOfRules) < 8:
            listOfRules.insert(0, " ")
    elif rule == 0:
        listOfRules = [" ", " ", " ", " ", " ", " ", " ", " "]

    nr_generatie = 0
    afisareVector(generatie)
    result = []

    while nr_generatie < nr_gen:
        generatieNoua = []
        i = 0
        result.append(afisareVector(generatie))
        for j in generatie:
            if i == 0:
                generatieNoua.append(functie(generatie[-1], generatie[i], generatie[i + 1]))
            elif i == len(generatie) - 1:
                generatieNoua.append(functie(generatie[i - 1], generatie[i], generatie[0]))
            else:
                generatieNoua.append(functie(generatie[i - 1], generatie[i], generatie[i + 1]))
            i = i + 1
        nr_generatie = nr_generatie + 1
        generatie = generatieNoua
        afisareVector(generatie)

    result.append(afisareVector(generatie))
    print(f"list of rules {listOfRules}")
    return render_template('results.html', result=result, steps=steps, listOfRules=listOfRules, rule=default_rule, nr_gen=nr_gen)


if __name__ == '__main__':
    app.run(debug=True)
