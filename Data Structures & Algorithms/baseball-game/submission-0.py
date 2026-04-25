class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        sumScore = 0
        for op in operations:
            if op == '+':
                score.append(score[-1] + score[-2])
            elif op == 'D':
                score.append(2 * score[-1])
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))
        for i in score:
            sumScore += i
        return sumScore
        