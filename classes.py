from os import get_terminal_size
from random import randint
from time import sleep, time
# Package built-in python3.8

# Text style.
normal_text = '\033[0m'
bold_text = '\033[1m'


class Screen:
    def __init__(self, nb_snow: int):
        """
        :param nb_snow: maximum number of snowflakes on each line.
        :raise OSError: Raise an error if this script is not run into a terminal.
        """

        # Create an empty list according to the size of the terminal.
        try:
            terminal_size = get_terminal_size()
        except OSError as _:
            raise OSError(f'{bold_text}Try to run this scrpit into a terminal, not into an IDE console.{normal_text}')

        self.nb_snow = nb_snow
        self.screen = [[' ' for _ in range(terminal_size.columns)] for _ in range(terminal_size.lines)]
        self.snow_on_screen = []

    def __getitem__(self, index_item: int) -> list:
        """
        :param index_item: Int.
        :return: Return the index_item line.
        """
        if index_item >= len(self.screen):
            return None

        return self.screen[index_item]

    def __len__(self) -> int:
        """
        :return: Return the number of lines.
        """
        return len(self.screen)

    def __str__(self) -> str:
        """
        :return: Return a str representing the screen and the flakes on the screen.
        """

        # Calculate the render time and show it.
        render_time = time()

        screen_to_text = ''
        for lines in self.screen:
            for char in lines:
                screen_to_text += str(char)
            screen_to_text += '\n'

        # Copyright - romain_flcht
        screen_to_text += f'\n{bold_text}Snowy terminal{normal_text} by {bold_text}romain_flcht{normal_text} - ' \
                          f'Render time : {bold_text}{time() - render_time}s{normal_text} - ' \
                          f'Press {bold_text}Ctrl + Z{normal_text} to stop...'
        return screen_to_text

    def set_snow_layer(self) -> None:
        """
        Create the first layer of snowflake on top of the screen.
        """
        column_already_taken = []

        # Create snowflakes (between 1 and the number of snowflake put in nb_snow, parameter of Screen).
        for nb_snow in range(randint(1, self.nb_snow)):
            random_column = randint(0, len(self[0]) - 1)

            # If random_column is already taken, change to another random number.
            while random_column in column_already_taken:
                random_column = randint(0, len(self[0]) - 1)

            # If random_column is empty, put a snowflake and put it into column_already_taken.
            column_already_taken.append(random_column)
            new_snow = Snowflake(self, 0, random_column, 1)

            self.snow_on_screen.append(new_snow)
            self[0][random_column] = new_snow

    def start(self) -> None:
        """
        Start the animation forever - Press Crtl + Z to stop it...
        """
        while True:
            for snowflake in self.snow_on_screen:
                # Move every snowflake on screen
                snowflake.move()

            # Put another layer and display the frame.
            self.set_snow_layer()
            print(self)

            # 0.2 sec between each frame for a slow falling.
            sleep(0.2)


class Snowflake:
    def __init__(self, screen: Screen, line: int, column: int, speed: int):
        self.screen = screen
        self.line = line
        self.column = column
        self.speed = speed

    def __str__(self) -> str:
        """
        :return: Return a snowflake.
        """
        return f'{bold_text}*{normal_text}'

    def move(self) -> None:
        """
        Moves the flake one line to the bottom.
        """

        # If it is the last line or there are a snowflake underneath, remove the snowflake.
        if self.line == len(self.screen) - 1 or \
                str(self.screen[self.line + 1][self.column]) == f'{bold_text}*{normal_text}':

            self.screen.snow_on_screen.remove(self)
        else:
            # Else move the snowflake by one line to the bottom.
            self.screen[self.line][self.column] = ' '
            self.screen[self.line + self.speed][self.column] = self
            self.line += 1


if __name__ == '__main__':
    print('classes.py file : do nothing, import it into a python file...')
