class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        damage = sorted(damage, reverse=True)
        if damage[0] >= armor:
            damage[0]-=armor
        else:
            damage[0] = 0
            
        return sum(damage)+1