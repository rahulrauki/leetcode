class Solution:
    def judgeCircle(self, moves: str) -> bool: #53ms 14.1mb
        if (moves.count("U") == moves.count("D")) and (moves.count("L") == moves.count("R")):
            return True
        return False