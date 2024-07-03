import random

# Define the syllable groups and subgroups
syllables = {
    'Ci': {
        'Ci1': ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l'],
        'Ci2': ['g', 'k', 'h', 'm', 'n', 's', 'r'],
        'Ci3': ['v', 'w', 'z'],
        'Ci4': ['dr', 'tr', 'br', 'pr'],
        'Ci5': ['bl', 'pl', 'kl', 'sl'],
        'Ci6': ['sm', 'sn', 'sp', 'st', 'sk', 'str']
    },
    'V': {
        'V1': ['a', 'e', 'i', 'o', 'u'],
        'V2': ['_a_e', '_e_e', '_i_e', '_o_e', '_u_e'],
        'V3': ['ay', 'ai', 'ea', 'ee', 'oa'],
        'V4': ['ar', 'er', 'ir', 'or', 'ur'],
        'V5': ['ou', 'ow', 'oi']
    },
    'C': {
        'C1': ['s', 'ss'],
        'C2': ['b', 'p'],
        'C3': ['d', 't'],
        'C4': ['g', 'k'],
        'C5': ['st', 'sp', 'sk'],
        'C6': ['m', 'n'],
        'C7': ['m', 'mb', 'mp'],
        'C8': ['n', 'nd', 'nt'],
        'C9': ['ph', 'ch', 'sh', 'ths']
    }
}

# Function to generate words
def generate_words(ci_groups, v_groups, c_groups, num_words):
    words = []
    v_flag = False
    # ci_choices = [item for group in ci_groups for item in syllables['Ci'][group]] # [[item for group in ci_groups] for item in syllables['Ci'][group]]
    # print("1: ", ci_choices)
    # v_choices = [item for group in v_groups for item in syllables['V'][group]]
    # c_choices = [item for group in c_groups for item in syllables['C'][group]]
    ci_choices = sum([syllables["Ci"][group] for group in ci_groups], [])
    v_choices = sum([syllables["V"][group] for group in v_groups], [])
    c_choices = sum([syllables["C"][group] for group in c_groups], [])
    print("1: ", ci_choices)

    for _ in range(num_words):
        ci = random.choice(ci_choices)
        v = random.choice(v_choices)
        c = random.choice(c_choices)
        
        # if 'V2' in v_groups:
            # Replace underscores in V2 elements
        if '_' in v:
            v_flag = True
            v = v.replace('_', ci, 1).replace('_', c, 1)
        else:
            v_flag = False
        # word = ci + v + c if 'V2' not in v_groups else v
        word = ci + v + c if not v_flag else v
        words.append(word)
    return words

# User input
ci_groups = input("Enter the Ci groups (e.g., Ci1, Ci2, Ci3, ...): ").split(',')
v_groups = input("Enter the V groups (e.g., V1, V2, V3, ...): ").split(',')
c_groups = input("Enter the C groups (e.g., C1, C2, C3, ...): ").split(',')
num_words = int(input("Enter the number of words to generate: "))

# Generate words
generated_words = generate_words(ci_groups, v_groups, c_groups, num_words)

# Display the generated words
print("Generated words:")
for word in generated_words:
    print(word)
