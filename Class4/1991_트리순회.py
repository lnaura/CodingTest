import sys
input = sys.stdin.readline

n = int(input())

graph = dict()
for _ in range(n):
    parent, left, right = input().split()
    graph[parent] = [left, right]

def preorder(node):
    if node == '.':
        return
    print(node, end= '')
    preorder(graph[node][0])
    preorder(graph[node][1])
        

def inorder(node):
    if node == '.':
        return
    inorder(graph[node][0])
    print(node, end= '')
    inorder(graph[node][1])
        
def postorder(node):
    if node == '.':
        return
    postorder(graph[node][0])
    postorder(graph[node][1])
    print(node, end= '')
       
preorder('A') 
print()
inorder('A')
print()
postorder('A')