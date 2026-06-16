class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack= []

        for asteroid in asteroids:
            # filter the stack for each asteroid
            # you can always assume left asteroid is going right and right asteroid is going left
            while stack and stack[-1] > 0 and asteroid < 0:
                diff = stack[-1] + asteroid
                if diff == 0:
                    asteroid = 0
                    stack.pop()
                elif diff < 0:
                    stack.pop()
                else:
                    asteroid = 0

            if asteroid:
                stack.append(asteroid)
        return stack

        