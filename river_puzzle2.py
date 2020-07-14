import copy

#Number of entities in the puzzle; e.g. farmer plus wolf, goat and cabbage = 4
entities = 4

#Entities represented as binary numbers, where a 1 means entity is on the first bank
#and a zero means the entity is on the second bank. The order is farmer then the others.
#The list of states below stores all possibilities.
states = [[int(j) for j in str(bin(i))[2:]] for i in range(2**entities)]
states = [([0]*entities + i)[-entities:] for i in states]


base_inv_states = [[0,1,1,0],[0,0,1,1],[0,1,1,1]]
compl_inv_states = [[1-i for i in j] for j in base_inv_states]
inv_states = base_inv_states + compl_inv_states


def isValid (move):
    return move not in inv_states

def isNew (move):
    return move not in answer


start = [1] * entities
answer = [copy.copy(start)]
final_ans = []


def move (current_state):

    if current_state == [0]*entities:
        final_ans.append(copy.copy(answer))
    else:
        current_state[0] = 1 - current_state[0]
        for i in range(1,entities+1):

            if i < entities:
                current_state[i] = 1 - current_state[i]
                if isValid(current_state) and isNew(current_state):
                    answer.append(copy.copy(current_state))
                    move(current_state)
                    current_state[i] = 1 - current_state[i]
                    answer.pop()
                else:
                    current_state[i] = 1 - current_state[i]


            else:
                if isValid(current_state) and isNew(current_state):
                    answer.append(copy.copy(current_state))
                    move(current_state)
                    answer.pop()
                else:
                    continue
        current_state[0] = 1 - current_state[0]

move(start)
print('\n***********\nFinal list\n***********')
for i in final_ans:
    print(i)