class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        total = 1
        maxDamage = 0
        for i in range(len(damage)):
            maxDamage = max(maxDamage, damage[i])
            total += damage[i]

        
        return total - (armor if maxDamage >= armor else maxDamage)