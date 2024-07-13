class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        stack = []
        robots = []
        for i in range(n):
            robots.append({'position': positions[i], 'health': healths[i], 'direction': directions[i], 'original_index': i})
        robots.sort(key=lambda x: x['position'])
        for i in range(n):
            if robots[i]['direction'] == 'L':
                # remove right-going robots with smaller health from the top of the stack while decreasing the current robot's health
                while stack and robots[stack[-1]]['direction'] == 'R' and robots[stack[-1]]['health'] < robots[i]['health']:
                    stack.pop()
                    robots[i]['health'] -= 1
                if not stack or robots[stack[-1]]['direction'] == 'L':
                    stack.append(i)  # no more collisions, add current robot to stack
                elif stack and robots[stack[-1]]['health'] == robots[i]['health']:
                    stack.pop()  # health is same, remove both
                elif stack and robots[stack[-1]]['health'] > robots[i]['health']:
                    robots[stack[-1]]['health'] -= 1  # right-going robot has greater health, remove current robot and decrease right-going robot's health
            else:
                stack.append(i)
        return [robots[i]['health'] for i in sorted(stack, key=lambda x: robots[x]['original_index'])]
