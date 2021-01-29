# idea
# python program gets 6 inputs to make N (must be 'large' > 100)
# generate 10 at the start
# each line either starts with a variable or return 'A = ' or 'return '
# remaining statements are either variables or numbers
import string
import subject
import random

GENERATIONS = 100
POP_COUNT = 50
TARGET = 991
MUTATION_RATE = 0.3

def _generate_start(count: int):
    return [subject.Subject() for i in range(POP_COUNT)]
def _eval_with_target(result: float):
    return abs(TARGET-result)
    
subjects = _generate_start(POP_COUNT)

for generation in range(GENERATIONS):
    print(f'running generation {generation}:')
    #aa: for s in subjects: print("  "+','.join(str(s) for s in s.args) + ' -> ' + str(s.evaluate()))

    weighted_subjects = []
    for s in subjects:
        result = s.evaluate()
        if result != None:
            value = _eval_with_target(result)
            weighted_subjects.append((s, value))

    # select the top 4 and mutate them
    best_value = sorted(weighted_subjects, key=lambda x: x[1])[:4] # find the closest to the target (i.e. 0)
    subjects_best = list(f[0] for f in best_value)
    
    print(f"Best value {best_value[0][1]} as {best_value[0][0]}")
    if best_value[0][1] == 0:
        print('target hit, finish.')
        break
    
    subjects = subjects_best[:]
    for _x in range(POP_COUNT - 4):
        a = random.choice(subjects_best)
        b = random.choice(subjects_best)
        while a == b: # prevent them from being the same
            b = random.choice(subjects_best)
        subjects.append(a.mutate(b, MUTATION_RATE))