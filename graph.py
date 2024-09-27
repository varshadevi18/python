class Graph:
    def __init__(self):
      self.graph={}
      self.directed=False
    def addvertex(self,vertex):
       if vertex not in self.graph:
          self.graph[vertex]=[]
             
    def addedge(self,src,des):
        self.addvertex(src)
        self.addvertex(des)
        self.graph[src].append(des)
        if not  self.directed:
           self.graph[des].append(src)

    def display(self):
        for vertex in self.graph:
           print(f"{vertex}->{self.graph[vertex]}")
    
    def bfs(self,startvertex):
       queue=[startvertex]
       visited={startvertex:True}
       while queue:
          currentvertex=queue.pop(0)
          print(currentvertex,end='')
          for neighbor in self.graph[currentvertex]:
             if neighbor not in visited:
                
                visited[neighbor]=True
                queue.append(neighbor)

    def dfs(self,vertex,visited):
       if vertex not in visited:
          print(vertex,end='')
          visited[vertex]=True

       for neighbor in self.graph[vertex]:
          if neighbor not in visited:
             self.dfs(neighbor,visited)


G= Graph()
G.addedge('A','B')
G.addedge('A','D')
G.addedge('B','C')
G.addedge('C','D')
G.addedge('B','F')
G.addedge('D','E')

G.display()
print("The order after traversing by breadth")
G.bfs('A')
visited={}
print("\nThe order after traversing by depth")
G.dfs('A',visited)
    

          
    
       
