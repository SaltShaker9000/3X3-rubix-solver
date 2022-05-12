import pygame
import tkinter as tk
from rubik_solver import utils
import rubik_solver.CubieCube

pygame.init()

COLORS = dict(
    white=(255, 255, 255),
    black=(0, 0, 0),
    red=(255, 0, 0),
    dark_grey=(25, 25, 25),
    green=(0, 255, 0),
    blue=(0, 0, 255),
    yellow=(255, 233, 0),
    orange=(255, 127, 0),
    grey=(30, 30, 30),
)

NUM_TO_COLOR = {
    0: COLORS["white"],
    1: COLORS["red"],
    2: COLORS["green"],
    3: COLORS["blue"],
    4: COLORS["yellow"],
    5: COLORS["orange"],
}

R_COLORS = {
    (255, 255, 255): "w",
    (255, 0, 0): "r",
    (0, 255, 0): "g",
    (0, 0, 255): "b",
    (255, 233, 0): "y",
    (255, 127, 0): "o",
}

current_color = COLORS["red"]


class Settings:
    __U_squares = [
        [131, 71, COLORS["dark_grey"], 0],
        [171, 71, COLORS["dark_grey"], 1],
        [211, 71, COLORS["dark_grey"], 2],
        [131, 111, COLORS["dark_grey"], 3],
        (171, 111, COLORS["yellow"], 4),
        [211, 111, COLORS["dark_grey"], 5],
        [131, 151, COLORS["dark_grey"], 6],
        [171, 151, COLORS["dark_grey"], 7],
        [211, 151, COLORS["dark_grey"], 8],
    ]

    __L_squares = [
        [11, 191, COLORS["dark_grey"], 0],
        [51, 191, COLORS["dark_grey"], 1],
        [91, 191, COLORS["dark_grey"], 2],
        [11, 231, COLORS["dark_grey"], 3],
        (51, 231, COLORS["blue"], 4),
        [91, 231, COLORS["dark_grey"], 5],
        [11, 271, COLORS["dark_grey"], 6],
        [51, 271, COLORS["dark_grey"], 7],
        [91, 271, COLORS["dark_grey"], 8],
    ]

    __F_squares = [
        [131, 191, COLORS["dark_grey"], 0],
        [171, 191, COLORS["dark_grey"], 1],
        [211, 191, COLORS["dark_grey"], 2],
        [131, 231, COLORS["dark_grey"], 3],
        (171, 231, COLORS["red"], 4),
        [211, 231, COLORS["dark_grey"], 5],
        [131, 271, COLORS["dark_grey"], 6],
        [171, 271, COLORS["dark_grey"], 7],
        [211, 271, COLORS["dark_grey"], 8],
    ]

    __R_squares = [
        [251, 191, COLORS["dark_grey"], 0],
        [291, 191, COLORS["dark_grey"], 1],
        [331, 191, COLORS["dark_grey"], 2],
        [251, 231, COLORS["dark_grey"], 3],
        (291, 231, COLORS["green"], 4),
        [331, 231, COLORS["dark_grey"], 5],
        [251, 271, COLORS["dark_grey"], 6],
        [291, 271, COLORS["dark_grey"], 7],
        [331, 271, COLORS["dark_grey"], 8],
    ]

    __B_squares = [
        [371, 191, COLORS["dark_grey"], 0],
        [411, 191, COLORS["dark_grey"], 1],
        [451, 191, COLORS["dark_grey"], 2],
        [371, 231, COLORS["dark_grey"], 3],
        (411, 231, COLORS["orange"], 4),
        [451, 231, COLORS["dark_grey"], 5],
        [371, 271, COLORS["dark_grey"], 6],
        [411, 271, COLORS["dark_grey"], 7],
        [451, 271, COLORS["dark_grey"], 8],
    ]

    __D_squares = [
        [131, 311, COLORS["dark_grey"], 0],
        [171, 311, COLORS["dark_grey"], 1],
        [211, 311, COLORS["dark_grey"], 2],
        [131, 351, COLORS["dark_grey"], 3],
        (171, 351, COLORS["white"], 4),
        [211, 351, COLORS["dark_grey"], 5],
        [131, 391, COLORS["dark_grey"], 6],
        [171, 391, COLORS["dark_grey"], 7],
        [211, 391, COLORS["dark_grey"], 8],
    ]
    BAR_SQUARES = [[621, 129 + (40 * i), NUM_TO_COLOR[i], i] for i in range(6)]
    _side = "F"
    tk_gui_rerun = False

    def __init__(self):
        self.WIDTH = 670
        self.HEIGHT = 500

        self.main_font = pygame.font.SysFont("ubuntu", 30)
        self.ans_font = pygame.font.SysFont("ubuntu", 15)
        self.err_font = pygame.font.SysFont("ubuntu", 15)

        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("3x3x3 Rubix Solver")

    def grid(self):
        self.display.fill(COLORS["grey"])

        def plane3x3(x_offset=0, y_offset=0, clr="black"):
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset,
                                                y_offset + 40, 120, 1)
            )  # top
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset,
                                                y_offset + 80, 120, 1)
            )  # mid1
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset,
                                                y_offset + 120, 120, 1)
            )  # mid2
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset,
                                                y_offset + 160, 121, 1)
            )  # bottom
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset +
                                                40, y_offset + 40, 1, 120)
            )  # mid3
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset +
                                                80, y_offset + 40, 1, 120)
            )  # mid4
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset,
                                                y_offset + 41, 1, 120)
            )  # left side
            pygame.draw.rect(
                self.display, COLORS["black"], (x_offset +
                                                120, y_offset + 40, 1, 120)
            )  # right side

        plane3x3(10, 150)  # L
        plane3x3(130, 30)  # U
        plane3x3(130, 150)  # F
        plane3x3(250, 150)  # R
        plane3x3(130, 270)  # D
        plane3x3(370, 150)  # B

        pygame.draw.rect(self.display, COLORS["black"], (620, 128, 1, 241))
        pygame.draw.rect(self.display, COLORS["black"], (660, 128, 1, 241))

        for i in range(7):
            pygame.draw.rect(
                self.display, COLORS["black"], (620, 128 + i * 40, 41, 1))

    @property
    def Sides(self):
        vailed_sides = ["F", "B", "L", "R", "U", "D"]
        my_sides = [
            Settings.__F_squares,
            Settings.__B_squares,
            Settings.__L_squares,
            Settings.__R_squares,
            Settings.__U_squares,
            Settings.__D_squares,
        ]
        for i, j in enumerate(vailed_sides):
            if Settings._side == j:
                return my_sides[i]  # returns the side data

    @Sides.setter
    def Sides(cls, index):
        vailed_sides = ["F", "B", "L", "R", "U", "D"]
        my_sides = [
            Settings.__F_squares,
            Settings.__L_squares,
            Settings.__R_squares,
            Settings.__U_squares,
            Settings.__D_squares,
            Settings.__B_squares,
        ]
        for i, j in enumerate(vailed_sides):
            if Settings._side == j:
                my_sides[i][index][2] = current_color  # sets the square that was clicked to the current color

    def vailed_side(self, side, mode, index=None):
        Settings._side = side
        assert Settings._side in ["F", "B", "L", "R", "U", "D"]
        if mode == "getter":
            return self.Sides

        elif mode == "setter":
            self.Sides = index

    def load_layout(self):
        root = tk.Tk()
        root.title("Layout Loader")
        root.configure(bg="grey")
        root.geometry("300x400")

        checkbutton_vars = [tk.StringVar() for _ in range(12)]

        for var in checkbutton_vars:
            var.set("0")

        entry_var = tk.StringVar()
        text = tk.Entry(root, textvariable=entry_var)
        saves = []

        def change_values(index):
            for var in checkbutton_vars:
                var.set("0")  # sets all vars to false

            else:
                checkbutton_vars[index].set("1")  # sets the one clicked check mark to true

        def go_funk():
            if entry_var.get() and saves.count(entry_var.get()) < 1:

                text.place_forget()
                go_bnt.place_forget()

                with open("layoutSaves.txt", "a") as f:
                    # writes the current values of the grid squares to the layoutSaves file
                    f.write(f"{entry_var.get()}:\n")
                    f.write(f"{Settings.__U_squares}\n")
                    f.write(f"{Settings.__L_squares}\n")
                    f.write(f"{Settings.__F_squares}\n")
                    f.write(f"{Settings.__R_squares}\n")
                    f.write(f"{Settings.__B_squares}\n")
                    f.write(f"{Settings.__D_squares}\n")

                Settings.tk_gui_rerun = True
                root.destroy()

        def save_funk():
            if len(saves) <= 12:
                if saves:
                    for j, i in enumerate(saves):
                        try:
                            # Displaying all saves
                            text.place(x=10, y=14 + (31 * (j + 1)) - (1 * j))

                        except IndexError:
                            break

                else:
                    text.place(x=50, y=14 + (31 * 1))

                go_bnt.place(x=235, y=200)

        def stringTranslate(string_list):  # converts the text from the file to source code
            new_lst = []

            def add(num1, num2, num3, num4, num5, num6):
                new_lst.append(
                    [int(num1), int(num2), (int(num3),
                                            int(num4), int(num5)), int(num6)]
                )

            def mid_add(num1, num2, num3, num4, num5, num6):
                new_lst.append(
                    (int(num1), int(num2), (int(num3), int(num4), int(num5)), int(num6))
                )

            for i in range(8):
                string_var = string_list.split(", [")[i]
                if i == 3:
                    for j, i in enumerate(string_var.split("], (")):
                        var_index = i.split(", ")

                        for num, index in enumerate(var_index):
                            var_index[num] = (
                                ((index.strip("[")).strip("]")).strip("(")
                            ).strip(")")

                        if j == 0:
                            mid_add(
                                var_index[0],
                                var_index[1],
                                var_index[2],
                                var_index[3],
                                var_index[4],
                                var_index[5],
                            )

                        else:
                            add(
                                var_index[0],
                                var_index[1],
                                var_index[2],
                                var_index[3],
                                var_index[4],
                                var_index[5],
                            )

                else:
                    var_index = string_var[: string_var[2:].find(
                        "[")].split(", ")

                    for num, index in enumerate(var_index):
                        var_index[num] = (
                            ((index.strip("[")).strip("]")).strip("(")
                        ).strip(")")

                    add(
                        var_index[0],
                        var_index[1],
                        var_index[2],
                        var_index[3],
                        var_index[4],
                        var_index[5],
                    )

            return new_lst

        def load_funk():
            # loading selected save
            if "1" in [i.get() for i in checkbutton_vars]:
                load_name = saves[[i.get()
                                   for i in checkbutton_vars].index("1")]
                with open("layoutSaves.txt") as f:
                    contents = f.readlines()
                    for j, i in enumerate(contents):
                        if i[:-2] == load_name:
                            Settings.__U_squares = stringTranslate(
                                contents[j + 1])
                            Settings.__L_squares = stringTranslate(
                                contents[j + 2])
                            Settings.__F_squares = stringTranslate(
                                contents[j + 3])
                            Settings.__R_squares = stringTranslate(
                                contents[j + 4])
                            Settings.__B_squares = stringTranslate(
                                contents[j + 5])
                            Settings.__D_squares = stringTranslate(
                                contents[j + 6])
                            root.destroy()
                            break

        def delete_funk():
            # delete selected save
            if "1" in [i.get() for i in checkbutton_vars]:
                load_name = saves[[i.get()
                                   for i in checkbutton_vars].index("1")]
                with open("layoutSaves.txt", "r") as f:
                    contents = f.readlines()

                    for num, line in enumerate(contents):
                        if line[:-2] == load_name:
                            first_half = contents[:num]
                            second_half = contents[num + 7:]
                            with open("layoutSaves.txt", "w") as f:
                                for i in first_half:
                                    f.write(i)

                                for i in second_half:
                                    f.write(i)

                            root.destroy()
                            Settings.tk_gui_rerun = True
                            break

        def exit_funk():
            root.destroy()

        with open("layoutSaves.txt") as f:
            contents = f.readlines()
            for i in range(len(contents)):
                try:
                    saves.append(contents[7 * i][:-2])

                except IndexError:
                    break

        go_bnt = tk.Button(root, text="Go", command=go_funk)
        (tk.Button(root, text="Save", command=save_funk)).place(x=230, y=50)
        (tk.Button(root, text="Load", command=load_funk)).place(x=230, y=100)
        (tk.Button(root, text="Delete", command=delete_funk)).place(x=225, y=150)
        (tk.Button(root, text="Exit", command=exit_funk)).place(x=235, y=355)

        labels = [tk.Label(root, text=i) for i in saves]

        if labels:
            for j, i in enumerate(labels):
                try:
                    (i).place(x=50, y=14 + (31 * j) - (1 * j))

                except IndexError:
                    break

        y_pos, y_offset = 30, 16
        if len(saves) >= 1:
            (
                tk.Checkbutton(
                    root,
                    text="",
                    variable=checkbutton_vars[0],
                    command=lambda: change_values(0),
                )
            ).place(x=10, y=y_pos * 1 - y_offset)
            if len(saves) >= 2:
                (
                    tk.Checkbutton(
                        root,
                        text="",
                        variable=checkbutton_vars[1],
                        command=lambda: change_values(1),
                    )
                ).place(x=10, y=y_pos * 2 - y_offset)
                if len(saves) >= 3:
                    (
                        tk.Checkbutton(
                            root,
                            text="",
                            variable=checkbutton_vars[2],
                            command=lambda: change_values(2),
                        )
                    ).place(x=10, y=y_pos * 3 - y_offset)
                    if len(saves) >= 4:
                        (
                            tk.Checkbutton(
                                root,
                                text="",
                                variable=checkbutton_vars[3],
                                command=lambda: change_values(3),
                            )
                        ).place(x=10, y=y_pos * 4 - y_offset)
                        if len(saves) >= 5:
                            (
                                tk.Checkbutton(
                                    root,
                                    text="",
                                    variable=checkbutton_vars[4],
                                    command=lambda: change_values(4),
                                )
                            ).place(x=10, y=y_pos * 5 - y_offset)
                            if len(saves) >= 6:
                                (
                                    tk.Checkbutton(
                                        root,
                                        text="",
                                        variable=checkbutton_vars[5],
                                        command=lambda: change_values(5),
                                    )
                                ).place(x=10, y=y_pos * 6 - y_offset)
                                if len(saves) >= 7:
                                    (
                                        tk.Checkbutton(
                                            root,
                                            text="",
                                            variable=checkbutton_vars[6],
                                            command=lambda: change_values(6),
                                        )
                                    ).place(x=10, y=y_pos * 7 - y_offset)
                                    (
                                        tk.Checkbutton(
                                            root,
                                            text="",
                                            variable=checkbutton_vars[7],
                                            command=lambda: change_values(7),
                                        )
                                    ).place(x=10, y=y_pos * 8 - y_offset)
                                    if len(saves) >= 8:
                                        (
                                            tk.Checkbutton(
                                                root,
                                                text="",
                                                variable=checkbutton_vars[8],
                                                command=lambda: change_values(
                                                    8),
                                            )
                                        ).place(x=10, y=y_pos * 9 - y_offset)
                                        if len(saves) >= 9:
                                            (
                                                tk.Checkbutton(
                                                    root,
                                                    text="",
                                                    variable=checkbutton_vars[9],
                                                    command=lambda: change_values(
                                                        9),
                                                )
                                            ).place(x=10, y=y_pos * 10 - y_offset)
                                            if len(saves) >= 10:
                                                (
                                                    tk.Checkbutton(
                                                        root,
                                                        text="",
                                                        variable=checkbutton_vars[10],
                                                        command=lambda: change_values(
                                                            10
                                                        ),
                                                    )
                                                ).place(x=10, y=y_pos * 11 - y_offset)
                                                if len(saves) >= 11:
                                                    (
                                                        tk.Checkbutton(
                                                            root,
                                                            text="",
                                                            variable=checkbutton_vars[
                                                                11
                                                            ],
                                                            command=lambda: change_values(
                                                                11
                                                            ),
                                                        )
                                                    ).place(
                                                        x=10, y=y_pos * 12 - y_offset
                                                    )

        root.mainloop()

    def button(self, x1, y1, x2, y2, idx, num, clr=COLORS["blue"]):
        on_bnt4x = False
        on_bnt4y = False

        for x in range(1, x2):
            if pygame.mouse.get_pos()[0] == x1 + x:
                on_bnt4x = True

        for y in range(1, y2):
            if pygame.mouse.get_pos()[1] == y1 + y:
                on_bnt4y = True

        if on_bnt4x is True and on_bnt4y is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if num == i:
                            if i == 0:
                                Settings.vailed_side(
                                    self, "F", "setter", index=idx
                                )  # using setter method

                            elif i == 1:
                                Settings.vailed_side(
                                    self, "B", "setter", index=idx
                                )  # using setter method

                            elif i == 2:
                                Settings.vailed_side(
                                    self, "L", "setter", index=idx
                                )  # using setter method

                            elif i == 3:
                                Settings.vailed_side(
                                    self, "R", "setter", index=idx
                                )  # using setter method

                            elif i == 4:
                                Settings.vailed_side(
                                    self, "U", "setter", index=idx
                                )  # using setter method

                            elif i == 5:
                                Settings.vailed_side(
                                    self, "D", "setter", index=idx
                                )  # using setter method

                pygame.draw.rect(self.display, clr, (x1, y1, x2, y2), 5)

        else:
            pygame.draw.rect(self.display, clr, (x1, y1, x2, y2))

    def bar_button(self, x1, y1, x2, y2, clr, index):
        global current_color
        on_bnt4x = False
        on_bnt4y = False

        for x in range(1, x2):
            if pygame.mouse.get_pos()[0] == x1 + x:
                on_bnt4x = True

        for y in range(1, y2):
            if pygame.mouse.get_pos()[1] == y1 + y:
                on_bnt4y = True

        if on_bnt4x is True and on_bnt4y is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(6):
                        if index == i:
                            current_color = NUM_TO_COLOR[i]

                pygame.draw.rect(self.display, clr, (x1, y1, x2, y2), 5)

        else:
            pygame.draw.rect(self.display, clr, (x1, y1, x2, y2))

    def funk_button(
        self,
        x1,
        y1,
        x2,
        y2,
        txt,
        txt_x_offset=0,
        txt_y_offset=0,
        clr=COLORS["white"],
        change_clr=COLORS["blue"],
        funk=None,
    ):
        on_bnt4x = False
        on_bnt4y = False

        for x in range(1, x2):
            if pygame.mouse.get_pos()[0] == x1 + x:
                on_bnt4x = True

        for y in range(1, y2):
            if pygame.mouse.get_pos()[1] == y1 + y:
                on_bnt4y = True

        if on_bnt4x is True and on_bnt4y is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if funk == "cls":  # clear
                        Settings.__U_squares = [
                            [131, 71, COLORS["dark_grey"], 0],
                            [171, 71, COLORS["dark_grey"], 1],
                            [211, 71, COLORS["dark_grey"], 2],
                            [131, 111, COLORS["dark_grey"], 3],
                            (171, 111, COLORS["yellow"], 4),
                            [211, 111, COLORS["dark_grey"], 5],
                            [131, 151, COLORS["dark_grey"], 6],
                            [171, 151, COLORS["dark_grey"], 7],
                            [211, 151, COLORS["dark_grey"], 8],
                        ]

                        Settings.__L_squares = [
                            [11, 191, COLORS["dark_grey"], 0],
                            [51, 191, COLORS["dark_grey"], 1],
                            [91, 191, COLORS["dark_grey"], 2],
                            [11, 231, COLORS["dark_grey"], 3],
                            (51, 231, COLORS["blue"], 4),
                            [91, 231, COLORS["dark_grey"], 5],
                            [11, 271, COLORS["dark_grey"], 6],
                            [51, 271, COLORS["dark_grey"], 7],
                            [91, 271, COLORS["dark_grey"], 8],
                        ]

                        Settings.__F_squares = [
                            [131, 191, COLORS["dark_grey"], 0],
                            [171, 191, COLORS["dark_grey"], 1],
                            [211, 191, COLORS["dark_grey"], 2],
                            [131, 231, COLORS["dark_grey"], 3],
                            (171, 231, COLORS["red"], 4),
                            [211, 231, COLORS["dark_grey"], 5],
                            [131, 271, COLORS["dark_grey"], 6],
                            [171, 271, COLORS["dark_grey"], 7],
                            [211, 271, COLORS["dark_grey"], 8],
                        ]

                        Settings.__R_squares = [
                            [251, 191, COLORS["dark_grey"], 0],
                            [291, 191, COLORS["dark_grey"], 1],
                            [331, 191, COLORS["dark_grey"], 2],
                            [251, 231, COLORS["dark_grey"], 3],
                            (291, 231, COLORS["green"], 4),
                            [331, 231, COLORS["dark_grey"], 5],
                            [251, 271, COLORS["dark_grey"], 6],
                            [291, 271, COLORS["dark_grey"], 7],
                            [331, 271, COLORS["dark_grey"], 8],
                        ]

                        Settings.__B_squares = [
                            [371, 191, COLORS["dark_grey"], 0],
                            [411, 191, COLORS["dark_grey"], 1],
                            [451, 191, COLORS["dark_grey"], 2],
                            [371, 231, COLORS["dark_grey"], 3],
                            (411, 231, COLORS["orange"], 4),
                            [451, 231, COLORS["dark_grey"], 5],
                            [371, 271, COLORS["dark_grey"], 6],
                            [411, 271, COLORS["dark_grey"], 7],
                            [451, 271, COLORS["dark_grey"], 8],
                        ]

                        Settings.__D_squares = [
                            [131, 311, COLORS["dark_grey"], 0],
                            [171, 311, COLORS["dark_grey"], 1],
                            [211, 311, COLORS["dark_grey"], 2],
                            [131, 351, COLORS["dark_grey"], 3],
                            (171, 351, COLORS["white"], 4),
                            [211, 351, COLORS["dark_grey"], 5],
                            [131, 391, COLORS["dark_grey"], 6],
                            [171, 391, COLORS["dark_grey"], 7],
                            [211, 391, COLORS["dark_grey"], 8],
                        ]

                    elif funk == "slv":  # solve it
                        Rubiks.solve(self)

                    elif funk == "load":
                        self.load_layout()

                pygame.draw.rect(self.display, change_clr, (x1, y1, x2, y2))
                self.display.blit(
                    self.main_font.render(txt, True, COLORS["black"]),
                    [x1 + txt_x_offset, y1 + txt_y_offset],
                )

        else:
            pygame.draw.rect(self.display, clr, (x1, y1, x2, y2))
            self.display.blit(
                self.main_font.render(txt, True, COLORS["black"]),
                [x1 + txt_x_offset, y1 + txt_y_offset],
            )


class Rubiks(Settings):
    display_Parity_err = False
    display_flip_err = False
    display_dub_err = False
    display_dub_c_err = False
    display_INS_Color = [False, None]

    solve_directions = []
    my_scramble = []

    @classmethod
    def display_error_change(cls, **kwargs):
        display_names = [
            "display_Parity_err",
            "display_flip_err",
            "display_dub_err",
            "display_dub_c_err",
            "display_INS_Color",
        ]

        cls.display_Parity_err = False
        cls.display_flip_err = False
        cls.display_dub_err = False
        cls.display_dub_c_err = False
        cls.display_INS_Color[0] = False

        if kwargs:
            for i, j in enumerate(kwargs.keys()):
                if j in display_names:
                    if j == "display_Parity_err":
                        cls.display_Parity_err = True

                    elif j == "display_flip_err":
                        cls.display_flip_err = True

                    elif j == "display_dub_err":
                        cls.display_dub_err = True

                    elif j == "display_dub_c_err":
                        cls.display_dub_c_err = True

                    elif j == "display_INS_Color":
                        cls.display_INS_Color[0] = True

    class Insufficient_color(rubik_solver.CubieCube.DupedEdge):
        color_names = ("Red", "White", "Green", "Blue", "Yellow", "Orange")

        def __init__(self, *args):
            if args:
                for i, j in enumerate(Rubiks.Insufficient_color.color_names):
                    if args[0][i] < 9:
                        self.msg = j
                        break

                else:
                    self.msg = "error101"

                    print(args)

            else:
                self.msg = "error102"

            Rubiks.display_INS_Color[1] = Rubiks.Insufficient_color.__str__(
                self)

        def __str__(self):
            return "<ERROR> Insufficient Color(%s)" % self.msg

    class Flip_error(rubik_solver.CubieCube.FlipError):
        def __init__(self):
            super().__init__()

        def __str__(self):
            return "<ERROR> Flipped Edge(Fix: Double check your values)"

    class Duped_error(rubik_solver.CubieCube.DupedEdge):
        def __init__(self):
            super().__init__()

        def __str__(self):
            return "<ERROR> DupedEdge(Fix: Double check your values)"

    class Duped_C_error(rubik_solver.CubieCube.DupedCorner):
        def __init__(self):
            super().__init__()

        def __str__(self):
            return "<ERROR> DupedCorner(Fix: Double check your values)"

    class Parity_error(rubik_solver.CubieCube.ParityError):
        def __init__(self):
            super().__init__()

        def __str__(self):
            return "<ERROR> Parity Error"

    def solve(self):
        for i in [
            super().vailed_side("U", "getter"),
            super().vailed_side("L", "getter"),
            super().vailed_side("F", "getter"),
            super().vailed_side("R", "getter"),
            super().vailed_side("B", "getter"),
            super().vailed_side("D", "getter"),
        ]:
            for j in i:
                if COLORS["dark_grey"] == j[2]:
                    break

                else:
                    Rubiks.my_scramble.append(R_COLORS[j[2]])

        try:
            if not (
                Rubiks.my_scramble.count("r") == 9
                and Rubiks.my_scramble.count("w") == 9
                and Rubiks.my_scramble.count("g") == 9
                and Rubiks.my_scramble.count("b") == 9
                and Rubiks.my_scramble.count("y") == 9
                and Rubiks.my_scramble.count("o") == 9
            ):
                raise Rubiks.Insufficient_color(
                    [
                        Rubiks.my_scramble.count("r"),
                        Rubiks.my_scramble.count("w"),
                        Rubiks.my_scramble.count("g"),
                        Rubiks.my_scramble.count("b"),
                        Rubiks.my_scramble.count("y"),
                        Rubiks.my_scramble.count("o"),
                    ]
                )

            Rubiks.my_scramble = "".join(Rubiks.my_scramble)

            Rubiks.solve_directions = utils.solve(
                str(Rubiks.my_scramble), "Kociemba")

            Rubiks.display_error_change()

        except rubik_solver.CubieCube.ParityError:
            Rubiks.display_error_change(display_Parity_err=True)

        except Rubiks.Insufficient_color:
            Rubiks.display_error_change(display_INS_Color=True)

        except rubik_solver.CubieCube.FlipError:
            Rubiks.display_error_change(display_flip_err=True)

        except rubik_solver.CubieCube.DupedEdge:
            Rubiks.display_error_change(display_dub_err=True)

        except rubik_solver.CubieCube.DupedCorner:
            Rubiks.display_error_change(display_dub_err=True)

        finally:
            Rubiks.my_scramble = []

    def show_errs(self):
        if Rubiks.display_Parity_err == True:
            self.display.blit(
                self.err_font.render(
                    str(Rubiks.Parity_error.__str__(self)), True, COLORS["red"]
                ),
                [300, 467],
            )

        elif Rubiks.display_flip_err == True:
            self.display.blit(
                self.err_font.render(
                    str(Rubiks.Flip_error.__str__(self)), True, COLORS["red"]
                ),
                [300, 467],
            )

        elif Rubiks.display_INS_Color[0] == True:
            self.display.blit(
                self.err_font.render(
                    str(Rubiks.display_INS_Color[1]), True, COLORS["red"]
                ),
                [300, 467],
            )

        elif Rubiks.display_dub_err == True:
            self.display.blit(
                self.err_font.render(
                    str(Rubiks.Duped_error.__str__(self)), True, COLORS["red"]
                ),
                [300, 467],
            )

        elif Rubiks.display_dub_c_err:
            self.display.blit(
                self.err_font.render(
                    str(Rubiks.Duped_C_error.__str__(
                        self)), True, COLORS["red"]
                ),
                [300, 467],
            )

    def run(self):
        super().grid()  # drawing the grid
        # Grabbing the values in the grid with the associated color
        for j, k in enumerate(
            [
                super().vailed_side("F", "getter"),
                super().vailed_side("L", "getter"),
                super().vailed_side("R", "getter"),
                super().vailed_side("U", "getter"),
                super().vailed_side("D", "getter"),
                super().vailed_side("B", "getter"),
            ]
        ):
            for i in k:
                try:
                    super().button(
                        i[0], i[1], 39, 39, i[3], j, clr=i[2]
                    )  # Displaying the square

                except TypeError:  # This happens if it tries to change the center square that is always the same
                    continue

        for i in Settings.BAR_SQUARES:
            super().bar_button(
                i[0], i[1], 39, 39, i[2], i[3]
            )  # Displays the bar buttons

        # displays the clear button
        super().funk_button(
            510, 40, 130, 50, "Clear", txt_x_offset=25, txt_y_offset=6, funk="cls"
        )
        # displays the Solve button
        super().funk_button(
            510, 400, 130, 50, "Solve", txt_x_offset=25, txt_y_offset=6, funk="slv"
        )
        # displays the Load button
        super().funk_button(
            350, 400, 130, 50, "Load", txt_x_offset=25, txt_y_offset=6, funk="load"
        )

        Rubiks.show_errs(
            self
        )  # Displays the possible error on screen without breaking down the program

        if (
            Rubiks.solve_directions
        ):  # Displays the directions on screen when rubix is correctly solved
            self.display.blit(
                self.ans_font.render(
                    str(Rubiks.solve_directions), True, COLORS["white"]
                ),
                [20, 10],
            )

        if Settings.tk_gui_rerun == True:
            Settings.tk_gui_rerun = False
            super().load_layout()

        pygame.display.update()


while True:  # keeps the program up
    try:
        Rubiks().run()  # calling a new "run" function from the Rubiks class

    except (KeyboardInterrupt, SystemExit):
        break
