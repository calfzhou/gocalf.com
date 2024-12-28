class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        teams = list(sorted(votes[0]))
        n = len(teams)
        team_scores = {t: [0] * n for t in teams}
        for vote in votes:
            for i, t in enumerate(vote):
                team_scores[t][i] += 1

        teams.sort(key=lambda t: team_scores[t], reverse=True)
        return ''.join(teams)
