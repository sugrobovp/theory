## DFS (поиск в глубину)

Глубокий поиск (Depth-First Search, DFS) - это алгоритм обхода графа, который используется для исследования всех вершин и рёбер графа "вглубь" перед переходом к следующей вершине. Этот алгоритм начинает с начальной вершины, а затем идет так глубоко, как это возможно, прежде чем вернуться и исследовать другие ветви графа.

Вот как работает DFS:

1. Начните с заданной начальной вершины (обычно это корень дерева или стартовая точка для обхода графа).

2. Посетите начальную вершину и пометьте её как посещённую.

3. Рекурсивно или с использованием стека (или явной рекурсии) перейдите к следующей непосещённой смежной вершине.

4. Если не найдено больше непосещённых смежных вершин, вернитесь к предыдущей вершине и продолжите поиск в глубину оттуда.

5. Повторяйте шаги 3 и 4 до тех пор, пока не будут посещены все вершины графа.

DFS не гарантирует нахождение кратчайшего пути, но он может использоваться для различных задач, таких как поиск в глубину, топологическая сортировка, поиск компонент связности, и другие.

Пример кода на Python для DFS на графе, представленном в виде списка смежности:

```python
def dfs(graph, vertex, visited):
    # Посетить текущую вершину
    print(vertex)
    visited.add(vertex)

    # Рекурсивно посещать смежные вершины
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Пример графа в виде списка смежности
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()  # Для отслеживания посещённых вершин
dfs(graph, 'A', visited)  # Начать DFS с вершины 'A'
```
Этот код выполнит обход графа в глубину, начиная с вершины 'A' и выводя посещенные вершины в порядке обхода в глубину.

### Inorder traversal
```python
# Python3 program to for tree traversals


# A class that represents an individual node in a
# Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):

	if root:

		# First recur on left child
		printInorder(root.left)

		# Then print the data of node
		print(root.val, end=" "),

		# Now recur on right child
		printInorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Inorder traversal of binary tree is")
	printInorder(root)

```
### Preorder traversal
```python
# Python3 program to for tree traversals


# A class that represents an individual node
# in a Binary Tree
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val, end=" "),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)


# Driver code
if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	# Function call
	print("Preorder traversal of binary tree is")
	printPreorder(root)

```