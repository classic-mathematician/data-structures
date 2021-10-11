from jovian.pythondsa import evaluate_test_case

def locate_card(cards, query):
    pass


cards = [13, 11, 10, 7, 4, 3, 2, 1, 0]
query = 7
output = 3


test = {
    'input' : {
        'cards' : [13, 11, 10, 7, 4, 3, 2, 1, 0],
        'query' : 7
    },
    'output' : 3

}

print(locate_card(**test['input']) == test['output'])


tests = []

tests.append(test)


#query occurs in the middle
tests.append({
    'input' : {
        'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 1
    },
    'output' : 6

})

#query occurs in the first element
tests.append({
    'input' : {
        'cards' : [4, 2, 1, -1],
        'query' : 4
    },
    'output' : 0

})


tests.append({
    'input' : {
        'cards' : [3, -1, -9, -127],
        'query' : -127
    },
    'output' : 3

})

tests.append({
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output' : 0

})


tests.append({
    'input' : {
        'cards' : [9, 7, 5, 2, -9],
        'query' : 4
    },
    'output' : -1

})


tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 0, 0, 0],
        'query' : 3
    },
    'output' : 7

})

tests.append({
    'input' : {
        'cards' : [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 0, 0, 0],
        'query' : 6
    },
    'output' : 2

})

    evaluate_test_case(locate_card, test)
