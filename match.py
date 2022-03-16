import numpy as np

   
def conform_strings(string):
    return string.lower()

def matrix(string_a, string_b):
    rows = len(string_a) + 1
    cols = len(string_b) + 1

    mx = np.zeros(
        (rows, cols), 
        dtype = int
        )
    for i in range(1, rows):
        for k in range(1, cols):
            mx[i][0] = i
            mx[0][k] = k
    return [mx, rows, cols]


class Levenshtein:
    # this will calc the Levenshtein ratio
    def __init__(self, string_a, string_b):
        self.string_a = conform_strings(string_a)
        self.string_b = conform_strings(string_b)
        self.distance = None

    def get_distance(self, ratio_cost=1):

        self.distance, rows, cols = matrix(self.string_a, self.string_b)
        for col in range(1, cols):
            for row in range(1, rows):
                cost = ratio_cost
                if self.string_a[row-1] == self.string_b[col-1]:
                    cost = 0 

                self.distance[row][col] = min(self.distance[row-1][col] + 1,      # Cost of deletions
                                    self.distance[row][col-1] + 1,          # Cost of insertions
                                    self.distance[row-1][col-1] + cost)
        

        return self.distance[row][col]
    
    def ratio(self):
        distance = self.get_distance(ratio_cost=2)
        Ratio = (
            (
                len(self.string_a)+len(self.string_b)
            ) - distance) / (len(self.string_a)+len(self.string_b))

        return Ratio


class Score():
    """ this class scores the andidates
        with the words from the input sentence 
    parameter: 
        all_candidates: list of sentences.
        sentence: full search pattern
        words: list of tokens
    return:
        list object, integer: 
    """

    def __init__(self, candidate, input, words):
        self.candidate = candidate
        self.input = input
        self.tokens = words
        self.scores_tokens = []
        self.score_input = 0

    def string_score(self):
        self.score_input = Levenshtein(
            self.candidate, 
            self.input
            ).ratio()
        return self.score_input

    def words_score(self):
        for a_word in self.tokens:
            best_ratio = []
            for b_word in self.candidate.split():
                ratio = Levenshtein(a_word, b_word).ratio()
                best_ratio.append(ratio)
            self.scores_tokens.append(max(best_ratio))
        return [sum(self.scores_tokens)/ len(self.scores_tokens), self.scores_tokens]
                
    def multy_score(self):
        return (self.string_score() + self.words_score()[0]) / 2

