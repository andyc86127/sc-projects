"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    dx = 0
    dy = 0

    # Animation loop
    while True:
        point1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)  # upper left
        point2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)  # upper right
        point3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)  # lower left
        point4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                               graphics.ball.y + graphics.ball.height)  # lower right
        if graphics.switch:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            graphics.switch = False

        if graphics.ball.y < graphics.window.height and lives > 0 and graphics.earned_score != graphics.total_score:
            if graphics.ball.x + graphics.ball.width > graphics.window.width or graphics.ball.x < 0:  # hit L/R wall
                dx = -dx
            elif graphics.ball.y <= 0:  # hit roof
                dy = -dy
            elif point3 is graphics.paddle or point4 is graphics.paddle:  # hit paddle
                dy = -dy
                graphics.ball.move(dx, -graphics.paddle.height/2)
            elif point1 is None:  # each point of the ball's 4 corners hits brick(s) or not
                if point2 is None:
                    if point3 is None:
                        if point4 is None:
                            pass
                        elif point4 is not graphics.paddle and point4 is not graphics.scoreboard:
                            graphics.window.remove(point4)
                            graphics.earned_score += 1
                            dx = -dx
                    elif point3 is not graphics.paddle and point3 is not graphics.scoreboard:
                        graphics.window.remove(point3)
                        graphics.earned_score += 1
                        dx = -dx
                elif point2 is not graphics.paddle and point2 is not graphics.scoreboard:
                    graphics.window.remove(point2)
                    graphics.earned_score += 1
                    dy = -dy
            elif point1 is not graphics.paddle and point1 is not graphics.scoreboard:
                graphics.window.remove(point1)
                graphics.earned_score += 1
                dy = -dy
            graphics.ball.move(dx, dy)
            graphics.update_scoreboard()
            pause(FRAME_RATE)
        elif graphics.earned_score == graphics.total_score:  # win the game
            graphics.reset_ball()
            break
        else:  # lose one life
            lives -= 1
            graphics.reset_ball()
            dx = 0
            dy = 0
            if lives == 0:  # run out of lives
                break


if __name__ == '__main__':
    main()
