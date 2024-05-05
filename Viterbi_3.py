from itertools import product

def viterbi_all_emissions(states, start_prob, trans_prob, emit_prob, hidden_states):
    emission_probs = {}

    # Iterate through all possible emission sequences
    for emission_seq in product(['heads', 'tails'], repeat=len(hidden_states)):
        prob = start_prob[hidden_states[0]] * emit_prob[hidden_states[0]][emission_seq[0]]
        for t in range(1, len(hidden_states)):
            prob *= trans_prob[hidden_states[t-1]][hidden_states[t]] * emit_prob[hidden_states[t]][emission_seq[t]]
        emission_probs[emission_seq] = prob

    return emission_probs

# Input data
states = ('Fair', 'Biased')
start_probability = {'Fair': 0.50, 'Biased': 0.50}
transition_probability = {'Fair': {'Fair': 0.90, 'Biased': 0.10}, 'Biased': {'Fair': 0.10, 'Biased': 0.90}}
emission_probability = {'Fair': {'heads': 0.50, 'tails': 0.50}, 'Biased': {'heads': 0.75, 'tails': 0.25}}
hidden_states = ('Fair', 'Fair', 'Fair', 'Biased', 'Biased')

# Calculate probabilities of all possible emission sequences
emission_probabilities = viterbi_all_emissions(states, start_probability, transition_probability, emission_probability, hidden_states)

# Display probabilities of all possible emission sequences
for emission_seq, prob in emission_probabilities.items():
    print("Emission Sequence:", emission_seq, "Probability:", prob)