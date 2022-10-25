class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # initial, color = 0
        colors = [0] * len(graph)

        """
            node: cur coloring node
            color: cur node should be
        """
        def dfs(node, color):
            """
                if color[node] != 0, means it was traversed,
                find if its color is same to the color it should be
            """
            if colors[node] != 0:
                return colors[node] == color

            colors[node] = color

            """
                continue traverse its adjacent nodes with the other color, `-color`
            """
            for i in graph[node]:
                if not dfs(i, -color):
                    return False
            return True

        # traverse all color=0 nodes
        for v in range(len(graph)):
            if colors[v] == 0 and not dfs(v, 1):
                return False
        return True
