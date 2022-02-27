# Graph Traversing #
from tkinter import *
import time

global mode, startNode, goalNode, goalCity, ovalLabel
mode = False
startNode = 0
goalNode = 0
goalCity = "Bucharest"
ovalLabel = {}


class GraphTraversal:
    def clicked(self, *args):
        global startNode, goalNode
        event = args[0]
        startBtnStatus = self.start_btn.cget("relief")
        goalBtnStatus = self.goal_btn.cget("relief")
        # print(event
        # print(f"wow you're at index: {event.__dict__}, {event.y}")
        print('lol nub:', event)
        if startBtnStatus == "sunken":
            print()
            startNode = (event.widget.find_closest(event.x, event.y))[0]
            print(event.widget.find_closest(event.x, event.y))
            self.make_canvas.itemconfig(startNode, fill="red")
            # self.make_canvas.itemconfig(self.total_cities[startNode-1]._name, bg="red")
            # self.make_canvas.itemcget(self.total_cities[startNode-1]._name,"text")
            print(self.total_cities[startNode - 1]._name)
            self.start_btn.config(bg="black", fg="white", relief=RAISED)
            print('startNode: ', startNode)
            print('goalNode: ', goalNode)
        if goalBtnStatus == "sunken":
            goalNode = (event.widget.find_closest(event.x, event.y))[0]
            self.make_canvas.itemconfig(goalNode, fill="green")
            self.goal_btn.config(bg="black", fg="white", relief=RAISED)
            print('startNode: ', startNode)
            print('goalNode: ', goalNode)

    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window, bg="gray", relief=RAISED, bd=7, width=800, height=800)
        self.make_canvas.pack()
        # Status label initialization
        self.status = None
        self.start_btn = None
        self.goal_btn = None
        # Some list initialization bt default
        self.vertex_store = []
        self.total_circle = []
        self.queue_bfs = []
        self.stack_dfs = []
        self.total_cities = []

        # Some default function call
        self.basic_set_up()
        self.make_vertex()

    def basic_set_up(self):
        heading = Label(self.make_canvas, text="Graph Traversing Visualization", bg="gray", fg="black",
                        font=("Arial", 20, "bold", "italic"))
        heading.place(x=200, y=10)

        bfs_btn = Button(self.window, text="BFS", font=("Arial", 15, "bold"), bg="black", fg="white", relief=RAISED,
                         bd=8, command=self.bfs_traversing)
        bfs_btn.place(x=245, y=660)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="white", relief=RAISED,
                         bd=8, command=self.dfs_traversing)
        dfs_btn.place(x=325, y=660)

        self.start_btn = Button(self.window, text="START", font=("Arial", 15, "bold"), bg="black", fg="white",
                                relief=RAISED,
                                bd=8, command=self.mode_start)
        self.start_btn.place(x=20, y=660)

        self.goal_btn = Button(self.window, text="GOAL", font=("Arial", 15, "bold"), bg="black", fg="white",
                               relief=RAISED,
                               bd=8, command=self.mode_goal)
        self.goal_btn.place(x=135, y=660)

        self.status = Label(self.make_canvas, text="Not Visited", bg="gray", fg="black",
                            font=("Arial", 20, "bold", "italic"))
        self.status.place(x=20, y=590)

    def make_vertex(self):  # Vertex with connection make
        for i in range(31):
            self.total_circle.append(i)
            self.total_cities.append(i)

            # LEVEL 0

        self.total_circle[0] = self.make_canvas.create_oval(40, 330, 110, 370, width=3, tags=("nodeBtn",))  # Arad
        print(self.make_canvas.itemcget(self.total_circle[0], "tags"))
        self.make_canvas.tag_bind("nodeBtn", "<Button-1>", self.clicked)

        self.total_cities[0] = Label(self.make_canvas, text="Arad", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        # self.total_cities[0].bind("<Button-1>", clicked)

        self.total_cities[0].place(x=60, y=340)
        # LEVEL 1

        self.total_circle[1] = self.make_canvas.create_oval(120, 260, 190, 300, width=3, tags=("nodeBtn",))  # Zerind
        self.total_cities[1] = Label(self.make_canvas, text="Zerind", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[1].place(x=135, y=270)
        lbl = StringVar()
        lbl.set(".!canvas.!label3")
        #print('city1: ', lbl.cget("bg"))

        self.total_circle[2] = self.make_canvas.create_oval(120, 330, 190, 370, width=3, tags=("nodeBtn",))  # Sibiu
        self.total_cities[2] = Label(self.make_canvas, text="Sibiu", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[2].place(x=138, y=340)

        self.total_circle[3] = self.make_canvas.create_oval(120, 400, 190, 440, width=3,
                                                            tags=("nodeBtn",))  # Temisora
        # self.make_canvas.tag_bind("temisoraBtn", "<Button-1>", self.clicked)
        self.total_cities[3] = Label(self.make_canvas, text="Temisora", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[3].place(x=130, y=410)

        # LEVEL 2

        self.total_circle[4] = self.make_canvas.create_oval(200, 210, 270, 250, width=3, tags=("nodeBtn",))  # Zerind -> Oradia
        self.total_cities[4] = Label(self.make_canvas, text="Oradea", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[4].place(x=215, y=220)

        self.total_circle[5] = self.make_canvas.create_oval(200, 290, 270, 330, width=3, tags=("nodeBtn",))  # Sibiu -> Rimnicu
        self.total_cities[5] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[5].place(x=210, y=300)

        self.total_circle[6] = self.make_canvas.create_oval(200, 370, 270, 410, width=3, tags=("nodeBtn",))  # Sibiu -> Fagaras
        self.total_cities[6] = Label(self.make_canvas, text="Fagaras", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[6].place(x=210, y=380)

        self.total_circle[7] = self.make_canvas.create_oval(200, 450, 270, 490, width=3, tags=("nodeBtn",))  # Temisora -> Lugoj
        self.total_cities[7] = Label(self.make_canvas, text="Lugoj", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[7].place(x=215, y=460)
        # LEVEL 3

        self.total_circle[8] = self.make_canvas.create_oval(280, 160, 350, 200, width=3, tags=("nodeBtn",))  # Oradia -> Sibiu
        self.total_cities[8] = Label(self.make_canvas, text="Sibiu", bg="gray", fg="white", font=("Arial", 8, "italic"))
        self.total_cities[8].place(x=300, y=170)

        self.total_circle[9] = self.make_canvas.create_oval(280, 260, 350, 300, width=3, tags=("nodeBtn",))  # Rimnicu -> Craiova
        self.total_cities[9] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                     font=("Arial", 8, "italic"))
        self.total_cities[9].place(x=293, y=270)

        self.total_circle[10] = self.make_canvas.create_oval(280, 330, 350, 370, width=3, tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[10] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[10].place(x=295, y=340)

        self.total_circle[11] = self.make_canvas.create_oval(280, 400, 350, 440, width=3, tags=("nodeBtn",))  # Fagaras -> Bucharest***
        self.total_cities[11] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[11].place(x=288, y=410)

        self.total_circle[12] = self.make_canvas.create_oval(280, 500, 350, 540, width=3, tags=("nodeBtn",))  # Lugoj -> Mehadia
        self.total_cities[12] = Label(self.make_canvas, text="Mehadia", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[12].place(x=290, y=510)

        # LEVEL 4

        self.total_circle[13] = self.make_canvas.create_oval(360, 120, 430, 160, width=3, tags=("nodeBtn",))  # Sibiu -> Fagaras
        self.total_cities[13] = Label(self.make_canvas, text="Fagaras", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[13].place(x=372, y=130)

        self.total_circle[14] = self.make_canvas.create_oval(360, 190, 430, 230, width=3, tags=("nodeBtn",))  # sibiu -> Rimnicu
        self.total_cities[14] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[14].place(x=372, y=200)

        self.total_circle[15] = self.make_canvas.create_oval(360, 260, 430, 300, width=3, tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[15] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[15].place(x=375, y=270)

        self.total_circle[16] = self.make_canvas.create_oval(360, 330, 430, 370, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[16] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[16].place(x=367, y=340)

        self.total_circle[17] = self.make_canvas.create_oval(360, 500, 430, 540, width=3, tags=("nodeBtn",))  # Mehadia -> Dobreta
        self.total_cities[17] = Label(self.make_canvas, text="Dobreta", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[17].place(x=370, y=510)

        # LEVEL 5

        self.total_circle[18] = self.make_canvas.create_oval(440, 80, 510, 120, width=3, tags=("nodeBtn",))  # Fagaras -> Bucharest***
        self.total_cities[18] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[18].place(x=447, y=90)

        self.total_circle[19] = self.make_canvas.create_oval(440, 150, 510, 190, width=3, tags=("nodeBtn",))  # Rimnicu -> Craiova
        self.total_cities[19] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[19].place(x=453, y=160)

        self.total_circle[20] = self.make_canvas.create_oval(440, 210, 510, 250, width=3, tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[20] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[20].place(x=455, y=220)

        self.total_circle[21] = self.make_canvas.create_oval(440, 280, 510, 320, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[21] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[21].place(x=447, y=290)

        self.total_circle[22] = self.make_canvas.create_oval(440, 500, 510, 540, width=3, tags=("nodeBtn",))  # Dobreta -> Craiova
        self.total_cities[22] = Label(self.make_canvas, text="Craiova", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[22].place(x=450, y=510)

        # LEVEL 6

        self.total_circle[23] = self.make_canvas.create_oval(520, 150, 590, 190, width=3, tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[23] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[23].place(x=535, y=160)

        self.total_circle[24] = self.make_canvas.create_oval(520, 210, 590, 250, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[24] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[24].place(x=527, y=220)

        self.total_circle[25] = self.make_canvas.create_oval(520, 440, 590, 480, width=3, tags=("nodeBtn",))  # Craiova -> Rimnicu
        self.total_cities[25] = Label(self.make_canvas, text="Rimnicu", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[25].place(x=530, y=450)

        self.total_circle[26] = self.make_canvas.create_oval(520, 500, 590, 540, width=3, tags=("nodeBtn",))  # Craiova -> Pitesti
        self.total_cities[26] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[26].place(x=535, y=510)

        # LEVEL 7

        self.total_circle[27] = self.make_canvas.create_oval(600, 150, 670, 190, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[27] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[27].place(x=607, y=160)

        self.total_circle[28] = self.make_canvas.create_oval(600, 440, 670, 480, width=3, tags=("nodeBtn",))  # Rimnicu -> Pitesti
        self.total_cities[28] = Label(self.make_canvas, text="Pitesti", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[28].place(x=615, y=450)

        self.total_circle[29] = self.make_canvas.create_oval(600, 500, 670, 540, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[29] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[29].place(x=607, y=510)

        # LEVEL 8

        self.total_circle[30] = self.make_canvas.create_oval(680, 440, 750, 480, width=3, tags=("nodeBtn",))  # Pitesti -> Bucharest***
        self.total_cities[30] = Label(self.make_canvas, text="Bucharest", bg="gray", fg="white",
                                      font=("Arial", 8, "italic"))
        self.total_cities[30].place(x=688, y=450)

        ############################################################################################
        # LEVEL 1
        self.make_connector_down(0, 1)
        self.make_connector_down(0, 2)
        self.make_connector_down(0, 3)
        self.collector_connector(0, 1, 2, 3)

        # LEVEL 2
        self.make_connector_down(1, 4)
        self.collector_connector(1, 4)

        self.make_connector_down(2, 5)
        self.make_connector_down(2, 6)
        self.collector_connector(2, 5, 6)

        self.make_connector_down(3, 7)
        self.collector_connector(3, 7)

        # LEVEL 3
        self.make_connector_down(4, 8)
        self.make_connector_down(5, 9)
        self.make_connector_down(5, 10)
        self.make_connector_down(6, 11)
        self.make_connector_down(7, 12)

        self.collector_connector(4, 8)
        self.collector_connector(5, 9, 10)
        self.collector_connector(6, 11)
        self.collector_connector(7, 12)

        # LEVEL 4
        self.make_connector_down(8, 13)
        self.make_connector_down(8, 14)
        self.make_connector_down(9, 15)
        self.make_connector_down(10, 16)
        self.make_connector_down(12, 17)

        self.collector_connector(8, 13, 14)
        self.collector_connector(9, 15)
        self.collector_connector(10, 16)
        self.collector_connector(12, 17)

        # LEVEL 5
        self.make_connector_down(13, 18)
        self.make_connector_down(14, 19)
        self.make_connector_down(14, 20)
        self.make_connector_down(15, 21)
        self.make_connector_down(17, 22)

        self.collector_connector(13, 18)
        self.collector_connector(14, 19, 20)
        self.collector_connector(15, 21)
        self.collector_connector(17, 22)

        # LEVEL 6
        self.make_connector_down(19, 23)
        self.make_connector_down(20, 24)
        self.make_connector_down(22, 25)
        self.make_connector_down(22, 26)

        self.collector_connector(19, 23)
        self.collector_connector(20, 24)
        self.collector_connector(22, 25, 26)

        # LEVEL 7
        self.make_connector_down(23, 27)
        self.make_connector_down(25, 28)
        self.make_connector_down(26, 29)

        self.collector_connector(23, 27)
        self.collector_connector(25, 28)
        self.collector_connector(26, 29)

        # LEVEL 8
        self.make_connector_down(28, 30)
        self.collector_connector(28, 30)

        print(self.vertex_store)

    def make_connector_up(self, index1, index2):  # Up node connection make
        first_coord = self.make_canvas.coords(self.total_circle[index1])  # Source node coordinates
        second_coord = self.make_canvas.coords(self.total_circle[index2])  # Destination node coordinates
        line_start_x = (first_coord[0] + first_coord[2]) / 2  # Connector line start_x
        line_end_x = (second_coord[0] + second_coord[2]) / 2  # Connector line end_x
        line_start_y = (first_coord[1] + first_coord[3]) / 2  # Connector line start_y
        line_end_y = (second_coord[1] + second_coord[3]) / 2  # Connector line end_y
        self.make_canvas.create_line(line_start_x + 10, line_start_y - 10, line_end_x - 10, line_end_y + 10, width=3)

    def make_connector_down(self, index1, index2):  # Down node connection make
        first_coord = self.make_canvas.coords(self.total_circle[index1])  # Source node coordinates
        second_coord = self.make_canvas.coords(self.total_circle[index2])  # Destination node coordinates
        line_start_x = (first_coord[0] + first_coord[2]) / 2  # Connector line start_x
        line_end_x = (second_coord[0] + second_coord[2]) / 2  # Connector line end_x
        line_start_y = (first_coord[1] + first_coord[3]) / 2  # Connector line start_y
        line_end_y = (second_coord[1] + second_coord[3]) / 2  # Connector line end_y
        self.make_canvas.create_line(line_start_x + 34, line_start_y + 5, line_end_x - 34, line_end_y - 5, width=3)

    def collector_connector(self, source, connector1=None, connector2=None,
                            connector3=None):  # All about node data collect and store
        temp = []
        temp.append(self.total_circle[source])

        if connector1:
            temp.append(self.total_circle[connector1])
        else:
            temp.append(None)

        if connector2:
            temp.append(self.total_circle[connector2])
        else:
            temp.append(None)

        if connector3:
            #   print('abc', self.total_circle[connector3])
            temp.append(self.total_circle[connector3])
        else:
            temp.append(None)
        # print('temp', temp)
        self.vertex_store.append(temp)

    def mode_start(self):
        global mode
        mode = True
        self.goal_btn.config(relief=RAISED, bg="black", fg="white")
        self.start_btn.config(relief=SUNKEN, bg="white", fg="black")

    def mode_goal(self):
        global mode
        mode = False
        self.start_btn.config(relief=RAISED, bg="black", fg="white")
        self.goal_btn.config(relief=SUNKEN, bg="white", fg="black")

    def binary_search(self, start, end, find_it_as_source):  # Binary search algorithm use here
        while start <= end:
            mid = int((start + end) / 2)
            if self.vertex_store[mid][0] == find_it_as_source:
                return self.vertex_store[mid]
            elif self.vertex_store[mid][0] < find_it_as_source:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    def bfs_traversing(self):
        global startNode, goalNode
        start = startNode
        goal = goalNode
        start = start - 1
        print('start: ', start, ' goal: ', goal)
        try:
            print('bfs vector store val: ', self.vertex_store[start][0])
            self.queue_bfs.append(self.vertex_store[start][0])
            while self.queue_bfs:
                temp = self.binary_search(0, 22, self.queue_bfs[0])
                # print('temp: ', temp)
                if temp != -1:
                    if temp[1]:
                        self.queue_bfs.append(temp[1])
                    if temp[2]:
                        self.queue_bfs.append(temp[2])
                    if temp[3]:
                        self.queue_bfs.append(temp[3])
                take_vertex = self.queue_bfs.pop(0)
                self.status['text'] = f"Current City: {self.total_cities[take_vertex - 1].cget('text')}"
                print(self.total_circle[take_vertex - 1], self.total_cities[take_vertex - 1].cget('text'))
                self.total_cities[take_vertex - 1].config(bg="purple")
                self.make_canvas.itemconfig(take_vertex, fill="purple")
                self.window.update()
                time.sleep(0.3)
                if take_vertex == goal:
                    self.status['text'] = "Goal Reached"
                    break
                # if self.total_cities[take_vertex-1].cget("text") == "Bucharest":
                #     self.status['text'] = "Goal Reached"
                #     break
            if self.status['text'] != "Goal Reached":
                self.status['text'] = "All node Visited"
        except:
            print("Force stop error")

    def dfs_traversing(self):
        global startNode, goalNode
        start = startNode
        goal = goalNode
        start = start - 1
        print('start: ', start, ' goal: ', goal)
        try:
            self.stack_dfs.append(self.vertex_store[start][0])
            while self.stack_dfs:
                take_vertex = self.stack_dfs.pop()
                self.status['text'] = f"Current City: {self.total_cities[take_vertex - 1].cget('text')}"
                print(self.total_cities[take_vertex - 1].cget("text"))
                self.total_cities[take_vertex - 1].config(bg="blue")
                self.make_canvas.itemconfig(take_vertex, fill="blue")
                self.window.update()
                time.sleep(0.3)
                temp = self.binary_search(0, 22, take_vertex)
                if temp != -1:
                    if temp[1]:
                        self.stack_dfs.append(temp[1])
                    if temp[2]:
                        self.stack_dfs.append(temp[2])
                    if temp[3]:
                        self.stack_dfs.append(temp[3])
                if take_vertex == goal:
                    self.status['text'] = "Goal Reached"
                    break
                # if self.total_cities[take_vertex-1].cget("text") == "Bucharest":
                #     self.status['text'] = "Goal Reached"
                #     break
            if self.status['text'] != "Goal Reached":
                self.status['text'] = "All node Visited"
        except:
            print("Force stop error")


if __name__ == '__main__':
    window = Tk()
    window.title("Graph Traversal Visualizer")
    window.geometry("400x900")
    window.maxsize(800, 900)
    window.minsize(800, 900)
    window.config(bg="chocolate")
    window.wm_attributes('-transparentcolor', window['bg'])
    GraphTraversal(window)
    window.mainloop()
