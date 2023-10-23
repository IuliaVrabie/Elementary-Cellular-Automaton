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
        binary_pattern = str(left) + str(curr) + str(right)
        rule_index = int(binary_pattern, 2)     # Convert the binary string to an integer
        return listOfRules[7 - rule_index]

    def displayVector(v):
        return ''.join(map(str, v))
    # - str because it's easier to display datas
    # - maps convert each elems of a list in str then join concatenate them

    if steps % 2 == 0:
        before = int(steps/2)
        after = int(steps/2 - 1)
    else:
        before = after = int(steps // 2)
    print(f"steps {steps}: {before}, 1, {after}")

    generation = [0] * before + [1] + [0] * after
    print(generation)

    listOfRules = []
    if rule > 0:
        while rule > 0:
            if rule % 2 == 0:
                listOfRules.insert(0, 0) 
            else:
                listOfRules.insert(0, 1)
            rule = rule // 2
        while len(listOfRules) < 8:
            listOfRules.insert(0, 0)
    elif rule == 0:
        listOfRules = [0, 0, 0, 0, 0, 0, 0, 0]

    indexOfCurrGeneration = 0
    result = []

    while indexOfCurrGeneration < nr_gen:
        newGeneration = []
        i = 0
        result.append(displayVector(generation))
        for j in generation:
            if i == 0:
                newGeneration.append(functie(generation[-1], generation[i], generation[i + 1]))
            elif i == len(generation) - 1:
                newGeneration.append(functie(generation[i - 1], generation[i], generation[0]))
            else:
                newGeneration.append(functie(generation[i - 1], generation[i], generation[i + 1]))
            i = i + 1
        indexOfCurrGeneration = indexOfCurrGeneration + 1
        generation = newGeneration
        displayVector(generation)

    result.append(displayVector(generation))
    print(f"list of rules {listOfRules}")
    return render_template('new_result.html', result=result, steps=steps, listOfRules=listOfRules, rule=default_rule, indexOfCurrGeneration=indexOfCurrGeneration)


if __name__ == '__main__':
    app.run(debug=True)
