from collections import deque

//使用散列表（字典）实现图
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny" ,"sss"]
graph["anuj"] = ["ccc"]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
graph["sss"] = []

//判断这人是不是要找的？
//判断条件：名字的最后一个字母是s
def person_is_seller(name):
    return name[-1] == 's'

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " 是要找的？")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")