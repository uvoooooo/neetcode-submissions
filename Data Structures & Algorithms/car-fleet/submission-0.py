class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = [(p,s) for (p,s) in zip(position,speed)]

        stack = []

        fleet = sorted(fleet, reverse = True)

        for i in fleet:
            duration = (target - i[0]) / i[1]
            stack.append(duration)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        