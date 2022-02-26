# Graph Traversing #
from tkinter import *
import time


class GraphTraversal:
    def __init__(self, root):
        self.window = root
        self.make_canvas = Canvas(self.window, bg="chocolate", relief=RAISED, bd=7, width=800, height=800)
        self.make_canvas.pack()

        # Status label initialization
        self.status = None

        # Some list initialization bt default
        self.vertex_store = []
        self.total_circle = []
        self.queue_bfs = []
        self.stack_dfs = []

        # Some default function call
        self.basic_set_up()
        self.make_vertex()

    def basic_set_up(self):
        heading = Label(self.make_canvas, text="Graph Traversing Visualization", bg="chocolate", fg="yellow",
                        font=("Arial", 20, "bold", "italic"))
        heading.place(x=200, y=10)

        bfs_btn = Button(self.window, text="BFS", font=("Arial", 15, "bold"), bg="black", fg="green", relief=RAISED,
                         bd=8, command=self.bfs_traversing)
        bfs_btn.place(x=20, y=630)

        dfs_btn = Button(self.window, text="DFS", font=("Arial", 15, "bold"), bg="black", fg="green", relief=RAISED,
                         bd=8, command=self.dfs_traversing)
        dfs_btn.place(x=700, y=630)

        self.status = Label(self.make_canvas, text="Not Visited", bg="chocolate", fg="brown",
                            font=("Arial", 20, "bold", "italic"))
        self.status.place(x=50, y=550)

    def make_vertex(self):  # Vertex with connection make
        for i in range(31):
            self.total_circle.append(i)

            # LEVEL 0

        self.total_circle[0] = self.make_canvas.create_oval(80, 330, 110, 360, width=3)  # Arad

        # LEVEL 1

        self.total_circle[1] = self.make_canvas.create_oval(160, 260, 190, 290, width=3)  # Zerind

        self.total_circle[2] = self.make_canvas.create_oval(160, 330, 190, 360, width=3)  # Sibiu

        self.total_circle[3] = self.make_canvas.create_oval(160, 400, 190, 430, width=3)  # Temisora

        # LEVEL 2

        self.total_circle[4] = self.make_canvas.create_oval(240, 210, 270, 240, width=3)  # Zerind -> Oradia

        self.total_circle[5] = self.make_canvas.create_oval(240, 310, 270, 340, width=3)  # Sibiu -> Rimnicu

        self.total_circle[6] = self.make_canvas.create_oval(240, 370, 270, 400, width=3)  # Sibiu -> Fagaras

        self.total_circle[7] = self.make_canvas.create_oval(240, 450, 270, 480, width=3)  # Temisora -> Lugoj

        # LEVEL 3

        self.total_circle[8] = self.make_canvas.create_oval(320, 160, 350, 190, width=3)  # Oradia -> Sibiu

        self.total_circle[9] = self.make_canvas.create_oval(320, 290, 350, 320, width=3)  # Rimnicu -> Craiova

        self.total_circle[10] = self.make_canvas.create_oval(320, 330, 350, 360, width=3)  # Rimnicu -> Pitesti

        self.total_circle[11] = self.make_canvas.create_oval(320, 400, 350, 430, width=3)  # Fagaras -> Bucharest***

        self.total_circle[12] = self.make_canvas.create_oval(320, 500, 350, 530, width=3)  # Lugoj -> Mehadia

        # LEVEL 4

        self.total_circle[13] = self.make_canvas.create_oval(400, 120, 430, 150, width=3)  # Sibiu -> Fagaras

        self.total_circle[14] = self.make_canvas.create_oval(400, 190, 430, 220, width=3)  # sibiu -> Rimnicu

        self.total_circle[15] = self.make_canvas.create_oval(400, 290, 430, 320, width=3)  # Craiova -> Pitesti

        self.total_circle[16] = self.make_canvas.create_oval(400, 330, 430, 360, width=3)  # Pitesti -> Bucharest***

        self.total_circle[17] = self.make_canvas.create_oval(400, 500, 430, 530, width=3)  # Mehadia -> Dobreta

        # LEVEL 5

        self.total_circle[18] = self.make_canvas.create_oval(480, 120, 510, 150, width=3)  # Fagaras -> Bucharest***

        self.total_circle[19] = self.make_canvas.create_oval(480, 170, 510, 200, width=3)  # Rimnicu -> Craiova

        self.total_circle[20] = self.make_canvas.create_oval(480, 210, 510, 240, width=3)  # Rimnicu -> Pitesti

        self.total_circle[21] = self.make_canvas.create_oval(480, 290, 510, 320, width=3)  # Pitesti -> Bucharest***

        self.total_circle[22] = self.make_canvas.create_oval(480, 500, 510, 530, width=3)  # Dobreta -> Craiova

        # LEVEL 6

        self.total_circle[23] = self.make_canvas.create_oval(560, 170, 590, 200, width=3)  # Craiova -> Pitesti

        self.total_circle[24] = self.make_canvas.create_oval(560, 210, 590, 240, width=3)  # Pitesti -> Bucharest***

        self.total_circle[25] = self.make_canvas.create_oval(560, 420, 590, 450, width=3)  # Craiova -> Rimnicu

        self.total_circle[26] = self.make_canvas.create_oval(560, 500, 590, 530, width=3)  # Craiova -> Pitesti

        # LEVEL 7

        self.total_circle[27] = self.make_canvas.create_oval(640, 170, 670, 200, width=3)  # Pitesti -> Bucharest***

        self.total_circle[28] = self.make_canvas.create_oval(640, 420, 670, 450, width=3)  # Rimnicu -> Pitesti

        self.total_circle[29] = self.make_canvas.create_oval(640, 500, 670, 530, width=3)  # Pitesti -> Bucharest***

        # LEVEL 8

        self.total_circle[30] = self.make_canvas.create_oval(720, 420, 750, 450, width=3)  # Pitesti -> Bucharest***

        ############################################################################################
        # LEVEL 1
        self.make_connector_up(0, 1)
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

        # self.make_connector_up(1, 3)
        # self.make_connector_down(1, 4)
        # self.collector_connector(1, 3, 4)

        # self.make_connector_up(2, 5)
        # self.make_connector_down(2, 6)
        # self.collector_connector(2, 5, 6)

        # self.make_connector_up(3, 7)
        # self.make_connector_down(3, 8)
        # self.collector_connector(3, 7, 8)

        # self.make_connector_down(4, 9)
        # self.collector_connector(4, None, 9)

        # self.make_connector_down(5, 10)
        # self.collector_connector(5, None, 10)

        # self.make_connector_down(6, 11)
        # self.collector_connector(6, None, 11)

        # self.make_connector_up(8, 12)
        # self.collector_connector(8, 12, None)

        # self.make_connector_up(9, 13)
        # self.collector_connector(9, 13, None)

        # self.make_connector_down(10, 14)
        # self.collector_connector(10, None, 14)

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
        self.make_canvas.create_line(line_start_x + 12, line_start_y + 5, line_end_x - 12, line_end_y - 5, width=3)

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
            temp.append(self.total_circle[connector3])
        else:
            temp.append(None)

        self.vertex_store.append(temp)

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
        try:
            self.status['text'] = "Red: Visited"
            self.queue_bfs.append(self.vertex_store[0][0])
            while self.queue_bfs:
                temp = self.binary_search(0, 22, self.queue_bfs[0])
                if temp != -1:
                    if temp[1]:
                        self.queue_bfs.append(temp[1])
                    if temp[2]:
                        self.queue_bfs.append(temp[2])
                    if temp[3]:
                        self.queue_bfs.append(temp[3])
                take_vertex = self.queue_bfs.pop(0)
                print(take_vertex)
                self.make_canvas.itemconfig(take_vertex, fill="red")
                self.window.update()
                time.sleep(0.3)
            self.status['text'] = "All node Visited"
        except:
            print("Force stop error")

    def dfs_traversing(self):
        try:
            self.status['text'] = "Blue: Visited"
            self.stack_dfs.append(self.vertex_store[0][0])
            while self.stack_dfs:
                take_vertex = self.stack_dfs.pop()
                print(take_vertex)
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
            self.status['text'] = "All node Visited"
        except:
            print("Force stop error")


if __name__ == '__main__':
    window = Tk()
    window.title("Graph Traversal Visualizer")
    window.geometry("400x900")
    window.maxsize(800, 900)
    window.minsize(800, 900)
    window.config(bg="orange")
    GraphTraversal(window)
    window.mainloop()