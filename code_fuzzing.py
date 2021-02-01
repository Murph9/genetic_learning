# idea
# python program gets 6 inputs to make N (must be 'large' > 100)
# generate 10 at the start
# each line either starts with a variable or return 'A = ' or 'return '
# remaining statements are either variables or numbers
import string
import subject
import random
import itertools

GENERATIONS = 600
POP_COUNT = 50
MUTATION_RATE = 0.3
TARGET = 3.14159 # PI

def _generate_start(count: int):
    return [subject.Subject() for i in range(POP_COUNT)]
def _eval_with_target(result: float):
    return abs(TARGET-result)
    
subjects = _generate_start(POP_COUNT)

for generation in range(GENERATIONS):
    print(f'running generation {generation}:')
    #[print(x) for x in subjects]

    weighted_subjects = []
    for s in subjects:
        result = s.evaluate()
        if result != None:
            value = _eval_with_target(result)
            weighted_subjects.append((s, value))

    # select the top 4 and mutate them
    best_value = sorted(weighted_subjects, key=lambda x: x[1])[:4] # find the closest N to the target (i.e. 0)
    subjects_best = list(f[0] for f in best_value)
    
    print(f"Best value {best_value[0][1]} as {best_value[0][0]}")
    if best_value[0][1] == 0:
        print('target hit, finish.')
        break
    
    # add combinations of the best N
    subjects = subjects_best[:]
    for _y in itertools.combinations(subjects_best, 2):
        subjects.append(_y[0].mutate(_y[1], MUTATION_RATE))

    
    # add some 'mutations'
    for x in range(POP_COUNT - len(subjects)):
        s = random.choice(subjects)
        subjects.append(s.mutate(s, MUTATION_RATE))
        

[print(x) for x in subjects]
