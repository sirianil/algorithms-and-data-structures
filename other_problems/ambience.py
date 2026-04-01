class Ambience:
    def calculate_for_triplets(self, harmful_drugs, current_drugs, proposed_drug):
        risk_scores = {}
        for harmful_drug in harmful_drugs:
            risk_scores[frozenset([harmful_drug[0], harmful_drug[1]])] = harmful_drug[2]

        if len(current_drugs) < 2:
            return None
        
        i, j = 0, 1
        while j < len(current_drugs):
            pair1 = risk_scores.get(frozenset([current_drugs[i], current_drugs[j]]), 0)
            pair2 = risk_scores.get(frozenset([current_drugs[j], proposed_drug]), 0)
            pair3 = risk_scores.get(frozenset([current_drugs[i], proposed_drug]), 0)

            if ((pair1 + pair2 > 0.7 ) or (pair2 + pair3 > 0.7 ) or (pair3 + pair1 > 0.7 )):
                return True
            i += 1
            j += 1
        return False

if __name__ == '__main__':
    a = Ambience()
    print(a.calculate_for_triplets(
        [ [1, 3, 0.5], [2, 3, 0.3], [1, 4, 0.9] ],
        [1, 2],
        3
    ))
