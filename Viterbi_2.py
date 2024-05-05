from itertools import product

def viterbi_all_states(states, start_prob, trans_prob, emit_prob, emit_seq):
    all_hidden_states = list(product(states, repeat=len(emit_seq)))
    probabilities = {}

    for hidden_states in all_hidden_states:
        prob = start_prob[hidden_states[0]] * emit_prob[hidden_states[0]][emit_seq[0]]
        for t in range(1, len(emit_seq)):
            prob *= trans_prob[hidden_states[t-1]][hidden_states[t]] * emit_prob[hidden_states[t]][emit_seq[t]]
        probabilities[hidden_states] = prob

    return probabilities

# Input data
states = ('Fair', 'Biased')
start_probability = {'Fair': 0.50, 'Biased': 0.50}
transition_probability = {'Fair': {'Fair': 0.90, 'Biased': 0.10}, 'Biased': {'Fair': 0.10, 'Biased': 0.90}}
emission_probability = {'Fair': {'heads': 0.50, 'tails': 0.50}, 'Biased': {'heads': 0.75, 'tails': 0.25}}
emission_sequence = ('tails', 'tails', 'heads', 'tails', 'tails')

# Calculate probabilities of all possible hidden state sequences
probabilities = viterbi_all_states(states, start_probability, transition_probability, emission_probability, emission_sequence)

# Display probabilities of all possible hidden state sequences
for hidden_states, prob in probabilities.items():
    print("Hidden States:", hidden_states, "Probability:", prob)