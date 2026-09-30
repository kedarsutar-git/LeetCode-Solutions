class Solution:
    def matchPlayersAndTrainers(self, player: list[int], trainer: list[int]) -> int:
        left = 0
        right = 0
        players = sorted(player)
        trainers = sorted(trainer)
        while(left<len(players) and right<len(trainers)):
            if(players[left]<=trainers[right]):
                
                left += 1

            right += 1

        return left 

        