import heapq  # [추가] 우선순위 큐를 위해 필요합니다.

def manhattan_distance(state, goal_state):
    # 맨해튼 거리: |x1 - x2| + |y1 - y2|
    # state는 (row, col) 튜플입니다.
    return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

class Node():
    def __init__(self, state, parent, action, cost, heuristic):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost          # 시작점부터 현재까지 온 비용 (g)
        self.heuristic = heuristic # 현재부터 목표까지 예상 비용 (h)
        self.total_cost = cost + heuristic # 총 비용 (f = g + h)

    # PriorityQueue에서 노드끼리 비교하기 위해 필요합니다. (총 비용이 낮은 것이 우선)
    def __lt__(self, other):
        return self.total_cost < other.total_cost

class PriorityQueueFrontier():
    def __init__(self):
        self.frontier = [] # 힙(heap) 리스트 생성

    def add(self, node):
        # 힙에 노드를 추가합니다. __lt__ 덕분에 total_cost 기준으로 자동 정렬됩니다.
        heapq.heappush(self.frontier, node)

    def contains_state(self, state):
        # 대기열에 해당 state(위치)가 있는지 확인
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # 가장 비용이 낮은(우선순위가 높은) 노드를 꺼냅니다.
            node = heapq.heappop(self.frontier)
            return node

class Maze():

    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one start point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)

        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        # 탐색한 노드 수 초기화
        self.num_explored = 0

        # 시작 노드 생성 (비용 0, 휴리스틱 계산)
        start = Node(state=self.start, parent=None, action=None, cost=0, 
                     heuristic=manhattan_distance(self.start, self.goal))

        # 우선순위 큐 생성 및 시작 노드 추가
        frontier = PriorityQueueFrontier()
        frontier.add(start)
        
        # 탐색 완료한 위치를 저장할 집합
        self.explored = set()

        # 프론티어가 빌 때까지 반복
        while True:
            # 프론티어가 비었는데 목표를 못 찾았다면 실패
            if frontier.empty():
                raise Exception("no solution")
            
            # 노드를 하나 꺼냄 (우선순위 큐이므로 가장 유망한 노드가 나옴)
            node = frontier.remove()
            self.num_explored += 1

            # 목표 지점 도착 확인
            if node.state == self.goal:
                # 경로 역추적 (Backtracking)
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # 현재 위치를 탐색 완료 목록에 추가
            self.explored.add(node.state)

            # 이웃 노드 탐색
            for action, state in self.neighbors(node.state):
                # 프론티어에도 없고 이미 탐색한 곳도 아니라면
                if not frontier.contains_state(state) and state not in self.explored:
                    # 자식 노드 생성 (이동 비용 1 증가)
                    child = Node(state=state, parent=node, action=action, 
                                 cost=node.cost + 1, 
                                 heuristic=manhattan_distance(state, self.goal))
                    frontier.add(child)
                # (심화: 이미 프론티어에 있지만 더 짧은 경로를 찾은 경우의 로직은 생략되었습니다)

    def output_image(self, filename, show_solution=True, show_explored=True):
        from PIL import Image, ImageDraw
        cell_size = 50
        cell_border = 2

        img = Image.new(
            "RGBA",
            (self.width * cell_size, self.height * cell_size),
            "black"
        )
        draw = ImageDraw.Draw(img)

        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                if col:
                    fill = (40, 40, 40)
                elif (i, j) == self.start:
                    fill = (255, 0, 0)
                elif (i, j) == self.goal:
                    fill = (0, 171, 28)
                elif solution is not None and show_solution and (i, j) in solution:
                    fill = (220, 235, 113)
                elif solution is not None and show_explored and (i, j) in self.explored:
                    fill = (212, 97, 85)
                else:
                    fill = (237, 240, 252)

                draw.rectangle(
                    ([(j * cell_size + cell_border, i * cell_size + cell_border),
                      ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                    fill=fill
                )

        img.save(filename)

if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.print()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.print()
m.output_image("maze.png", show_explored=True)