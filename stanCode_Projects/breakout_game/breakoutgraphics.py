"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.window.add(self.paddle, (self.window.width - paddle_width) / 2,
                        self.window.height - paddle_offset - paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'blue'
        self.paddle.color = 'blue'

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.reset_ball()

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = 0
        self.switch = False

        # Initialize our mouse listeners.
        onmouseclicked(self.game_start)
        onmousemoved(self.move_paddle)

        # Draw bricks.
        by = 0
        for i in range(brick_rows):
            bx = 0
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < brick_cols / 5:
                    self.brick.fill_color = 'red'
                elif brick_cols / 5 <= i < brick_cols / 5 * 2:
                    self.brick.fill_color = 'orange'
                elif brick_cols / 5 * 2 <= i < brick_cols / 5 * 3:
                    self.brick.fill_color = 'yellow'
                elif brick_cols / 5 * 3 <= i < brick_cols / 5 * 4:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, bx, brick_offset+by)
                bx += brick_width + brick_spacing
            by += brick_height + brick_spacing

        # scoreboard
        self.earned_score = 0
        self.total_score = brick_cols * brick_rows
        self.scoreboard = GLabel(f'score: {self.earned_score}/{self.total_score}', x=10, y=30)
        self.scoreboard.font = 'courier-20'
        self.window.add(self.scoreboard)

    def update_scoreboard(self):
        self.window.remove(self.scoreboard)
        self.scoreboard = GLabel(f'score: {self.earned_score}/{self.total_score}', x=10, y=30)
        self.window.add(self.scoreboard)

    def reset_ball(self):
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)
        self.__dx = 0
        self.__dy = 0
        self.switch = False

    def move_paddle(self, event):
        self.paddle.x = event.x - self.paddle.width/2

    def game_start(self, event):
        if self.__dx == 0:
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.__dy = INITIAL_Y_SPEED
            self.switch = True

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

