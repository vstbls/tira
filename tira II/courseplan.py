class CoursePlan:
    def __init__(self):
        self.courses = {}
        self.n = 0

    def add_course(self,course):
        self.courses[course] = []
        self.n += 1

    def add_requisite(self,course1,course2):
        self.courses[course1].append(course2)

    def dfs(self,x):
        if self.color[x] == 1:
            self.found = True
            return
        if self.color[x] == 2:
            return
        self.color[x] = 1
        for y in self.courses[x]:
            self.dfs(y)
        self.color[x] = 2
        self.topo.append(x)
 
    def find(self):
        self.color = {k: 0 for k in self.courses.keys()}
        self.found = False
        self.topo = []
        for x in self.courses.keys():
            if self.color[x] == 0:
                self.dfs(x)
        if self.found:
            return None
        self.topo.reverse()
        return self.topo