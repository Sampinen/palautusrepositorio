class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
    def substract(self, score1,score2):
        return score1 -score2

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1
    def same_score(self):
            if self.m_score1 == 0:
                return "Love-All"
            elif self.m_score1 == 1:
                return "Fifteen-All"
            elif self.m_score1 == 2:
                return "Thirty-All"
            else:
                return "Deuce"
    def scoreadvantage(self, minus_result):
            if minus_result == 1:
                return "Advantage player1"
            elif minus_result == -1:
                return "Advantage player2"
            elif minus_result >= 2:
                return "Win for player1"
            else:
                return "Win for player2"
    def score_loop(self,score):
        for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2
                score = self.single_score(score,temp_score)
        return score



    def single_score(self,score,temp_score):
                if temp_score == 0:
                    return score + "Love"
                elif temp_score == 1:
                    return score + "Fifteen"
                elif temp_score == 2:
                    return score + "Thirty"
                elif temp_score == 3:
                    return score + "Forty"


    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.same_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.substract(self.m_score1,self.m_score2)
            score = self.scoreadvantage(minus_result)
        else:
            score = self.score_loop(score)

        return score
