"""
This file is for extension which contains:
# -----EXTENSION------------->SCORES
    Every brick crush will get 10 point, the score will keep updating. 

# -----EXTENSION------------->LUCKY BRICKS
    When the bricks are set, if the bricks location (i,j) cause the i * j == lucky number,
    this brick will be the lucky brick, which makes the paddle's width twice as the normal one.
    And after next ten bricks been crushed, the paddle will back to the normal one.   

# -----EXTENSION------------->GRAPHIC
    After player wins a game, the graphics will show up on the screen.
    If losing a game, bricks left will turn into gray, and window will show "LOSE"     
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    # 請不要更改以下的constructor keyword argument
    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__brick_height = brick_height
        self.__brick_width = brick_width
        self.__brick_spacing = brick_spacing
        self.__brick_offset = brick_offset

        #                                   Create a graphical window, with some extra space
        self.__window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=self.__window_width, height=self.window_height, title=title)

        #                                   Create a paddle
        self.__paddle = GRect(paddle_width, paddle_height, x=(self.__window_width - paddle_width) / 2,
                              y=self.window_height - paddle_offset)
        self.__paddle.filled = True
        self.__p_offset = self.window_height - paddle_offset

        self.__ball_radius = ball_radius  # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius, x=self.__window_width/2-ball_radius,
                          y=self.window_height/2-ball_radius)
        self.ball.filled = True

        self.__dx = 0                     # Default initial velocity for the ball
        self.__dy = 0
        self.__window.add(self.ball)

        onmousemoved(self.cat)            # Initialize our mouse listeners
        onmouseclicked(self.mouse)

        self.__paddle_lucky = GRect(paddle_width * 2, paddle_height, x=(self.__window_width - paddle_width) / 2,
                                    y=self.window_height - paddle_offset)
        self.__lucky_brick = None
        self.lucky_number = random.randint(0, brick_rows*brick_cols)    # Lucky number generater
        for j in range(brick_rows):       # Draw bricks
            for i in range(brick_cols):
                if i * j == self.lucky_number:
                    """
                    # -----EXTENSION------------->LUCKY BRICKS   
                    """
                    print("LUCKY NUMBER is ", self.lucky_number)
                    self.__lucky_brick = GRect(brick_width, brick_height, x=i * (brick_width + brick_spacing),
                                               y=j * (brick_height + brick_spacing) + brick_offset)
                    self.set_brick(j, 1)
                    self.__window.add(self.__lucky_brick)
                else:                                       # normal bricks
                    self.__brick = GRect(brick_width, brick_height, x=i * (brick_width + brick_spacing),
                                         y=j * (brick_height + brick_spacing) + brick_offset)
                    self.set_brick(j)                       # set brick
                    self.__window.add(self.__brick)         # add brick
        self.__brick_toll = (brick_rows * brick_cols)       # counter for bricks left
        self.__window.add(self.__paddle)                    # add paddle

        """
        # -----EXTENSION------------->SCORES
        """
        self.__score_count = 0
        self.__score_text = GLabel("SCORE: "+str(self.__score_count), x=20, y=30)
        self.__score_text.font = "Helvetica-20"
        self.__score_text.color = "black"
        self.__window.add(self.__score_text)
        self.__paddle_counter = 1

        """
        # -----EXTENSION------------->GRAPHIC
        """
        self.__background = GRect(self.__window_width, self.window_height, x=0, y=self.window_height)
        self.__background.filled = True
        self.__background.color = "mediumseagreen"
        self.__background.fill_color = "mediumseagreen"

        self.__in_line = GRect(750, 2.5*PADDLE_HEIGHT, x=0, y=0)
        self.__in_line.filled = True
        self.__in_line.color = "white"
        self.__in_line.fill_color = "white"

        self.__in_line2 = GRect(2.5*PADDLE_HEIGHT, self.window_height, x=70, y=self.window_height)
        self.__in_line2.filled = True
        self.__in_line2.color = "white"
        self.__in_line2.fill_color = "white"

        self.__background2 = GRect(self.__window_width, self.window_height, x=0, y=0)
        self.__background2.filled = True
        self.__background2.color = "Green"
        self.__background2.fill_color = "Green"

        self.ball2 = GOval(self.__ball_radius, self.__ball_radius, x=self.__window_width / 2 - self.__ball_radius,
                           y=self.window_height / 2 - self.__ball_radius)
        self.ball2.filled = True
        self.ball2.color = "gray"
        self.ball2.fill_color = "gray"

        self.__blue_backg = GRect(222, 30, x=108, y=self.window_height)
        self.__blue_backg.filled = True
        self.__blue_backg.color = "midnightblue"
        self.__blue_backg.fill_color = "midnightblue"

        self.__white_nackg = GRect(222, 30, x=108, y=380)
        self.__white_nackg.filled = True
        self.__white_nackg.color = "aliceblue"
        self.__white_nackg.fill_color = "aliceblue"

        self.__reviewing = GLabel("OFFICIAL REVIEW", x=130, y=176)
        self.__reviewing.color = "aliceblue"
        self.__reviewing.font = "Verdana-20"

        self.__count1 = GLabel("COURT 1", x=177, y=380)
        self.__count1.color = "aliceblue"
        self.__count1.font = "Verdana-20"

        self.__inbound = GLabel("In", x=205, y=410)
        self.__inbound.color = "midnightblue"
        self.__inbound.font = "Verdana-20"

        self.__win = GLabel("W", x=180, y=self.window_height)
        self.__win.color = "midnightblue"
        self.__win.font = "Verdana-20-bold"
        """"""

    def cat(self, tom):
        """
        set the paddle
        """
        self.__paddle.y = self.__p_offset                   # set offset of paddle
        if 0 < tom.x < self.__window_width-self.__paddle.width:
            self.__paddle.x = tom.x                         # stick paddle with mouse

        self.__paddle_lucky.y = self.__p_offset  # set offset of paddle
        if 0 < tom.x < self.__window_width - self.__paddle_lucky.width:
            self.__paddle_lucky.x = tom.x  # stick paddle with mouse

    def mouse(self, jerry):
        """
        set the velocity of ball when click on the mouse
        """
        check = self.__window.get_object_at(self.__window_width/2, self.window_height/2)    # check starting location
        if check is not None:                               # if the ball is at starting location and remain still
            if self.__dx == 0 and self.__dy == 0:
                self.__dx = random.randint(1, MAX_X_SPEED)  # random a velocity from 1 to maximum on x-axis
                self.__dy = INITIAL_Y_SPEED                 # velocity on y-axis remains constant
                if random.random() > 0.5:                   # random a direction on x-axis
                    self.__dx = -self.__dx

    def object_check(self):
        """
        detect the brick or paddle base on 4 point around the ball.
        If reach paddle bounce back upward.
        If reach bricks, remove all of the bricks the ball reached, and reverse the ball's velocity on y-axis.
        """
        bounce = False
        for i in range(4):
            a = self.ball.x                             # check up left point
            b = self.ball.y
            if i == 1:                                  # check up right point
                a = self.ball.x + 2*self.__ball_radius
            elif i == 2:                                # check down left point
                b = self.ball.y + 2*self.__ball_radius
            elif i == 3:                                # check down right point
                a = self.ball.x + 2*self.__ball_radius
                b = self.ball.y + 2*self.__ball_radius

            obj = self.__window.get_object_at(a, b)     # check these points
            if obj is not None:                         # if reach a stuff
                bounce = True                           # variable to change the velocity
                if obj != self.__paddle and obj != self.__score_text and obj != self.__paddle_lucky:
                    # not a paddle or score text means it's a brick
                    """
                    # -----EXTENSION------------->SCORES & LUCKY BRICKS
                    """
                    self.__window.remove(obj)           # remove the brick
                    self.__brick_toll -= 1              # bricks left on window
                    self.__score_count += 10                  # update the score
                    self.__paddle_counter += 1
                    self.__window.remove(self.__score_text)
                    self.__score_text = GLabel("SCORE: " + str(self.__score_count), x=20, y=30)
                    self.__score_text.font = "Helvetica-20"
                    self.__score_text.color = "black"
                    self.__window.add(self.__score_text)

                    if self.__brick_toll == 0:          # if all clear, set the ball to ending point
                        self.reset_ball(1)
                        break
                    if obj == self.__lucky_brick:
                        self.__window.remove(self.__paddle)
                        self.__window.add(self.__paddle_lucky)
                        self.__paddle_counter = -10
                    elif self.__paddle_counter == 0:
                        self.__window.remove(self.__paddle_lucky)
                        self.__window.add(self.__paddle)

                elif obj == self.__paddle or obj == self.__paddle_lucky:    # reach the paddle
                    if self.__dy < 0:                   # to avoid more than 1 point reach the paddle
                        bounce = False
                    break
                else:                                   # it's score text
                    bounce = False                      # pass through it
        if bounce:                                      # bounce back
            self.bounce_back_dy()

    def wall_bounce(self):
        """
        if reach wall or upper bound
        """
        if self.ball.x + 2*self.__ball_radius >= self.__window_width or self.ball.x <= 0:
            self.bounce_back_dx()
        if self.ball.y <= 0:
            self.bounce_back_dy()

    def bounce_back_dx(self):
        """
        change velocity on x-axis
        """
        self.__dx = -self.__dx

    def bounce_back_dy(self):
        """
        change velocity on y-axis
        """
        self.__dy = -self.__dy

    def set_brick(self, j, x=0):
        """
        set bricks color base on the j-th rows
        """
        if j < 2:
            color = 'red'
        elif j < 4:
            color = 'orange'
        elif j < 6:
            color = "yellow"
        elif j < 8:
            color = "green"
        elif j < 10:
            color = "blue"
        elif j < 12:
            color = "midnightblue"
        else:
            color = "gray"
        if x == 1:
            self.__lucky_brick.filled = True
            self.__lucky_brick.fill_color = color
            self.__lucky_brick.color = color
            return
        self.__brick.filled = True
        self.__brick.fill_color = color
        self.__brick.color = color

    def getter_dx(self):
        """
        dx getter
        """
        return self.__dx

    def getter_dy(self):
        """
        dy getter
        """
        return self.__dy

    def reset_ball(self, x=0):
        """
        1. reset the ball to the starting point.
        2. If x == 0 set the ball to the ending point
        3. If x == 1 user win the game, move ball to ending point and show the "win" graphics
        """

        if x == 1:                                  # win
            self.__window.remove(self.ball)
            self.__window.add(self.__background)
            self.__window.add(self.__blue_backg)
            self.__window.add(self.ball)
            counter = 0
            while self.__background.y > 15:
                self.__background.move(0, -15)
                pause(10)

                if counter > (self.window_height/15)/2:
                    self.__reviewing.move(0, -(self.window_height - 380)/(self.window_height/15/2-1))
                    self.__blue_backg.move(0, -(self.window_height - 350)/(self.window_height/15/2-1))
                counter += 1

            self.__reviewing.y = 380
            self. __blue_backg.y = 350
            self.__background.y = 0
            self.__window.add(self.__reviewing)

            # move the ball to game point
            w = self.__window_width
            h = self.window_height
            r = self.__ball_radius
            dxx = (w / 2 - r - self.ball.x)/50
            dyy = (188 - self.ball.y)/50
            self.__window.add(self.__in_line)
            self.__window.add(self.__in_line2)
            counter = 0
            while self.ball.x != w / 2 - r and self.ball.y <= 188:
                self.__ball_radius -= self.__ball_radius/70
                temp_x = self.ball.x
                temp_y = self.ball.y
                self.__window.remove(self.ball)
                self.ball = GOval(2*self.__ball_radius, 2*self.__ball_radius, x=temp_x, y=temp_y)
                self.ball.filled = True
                self.ball.color = "black"
                self.ball.fill_color = "black"
                self.__window.add(self.ball)

                self.ball.x += dxx
                self.ball.y += dyy

                self.__in_line2.move(0, -(h - 193)/50)

                counter += 1
                if counter <= 40:
                    self.__in_line.move(0, 5)
                else:
                    self.__in_line.move(0, -(5*40-176)/10)
                pause(10)

            self.ball.y = 188
            self.__window.remove(self.ball)
            self.ball.color = "gray"
            self.ball.fill_color = "gray"
            self.__window.add(self.ball)
            pause(1000)
            self.__window.add(self.__white_nackg)
            self.__window.add(self.__count1)

            self.__window.remove(self.__reviewing)
            self.__window.add(self.__white_nackg)
            self.__window.add(self.__inbound)
            pause(1000)
            self.__window.add(self.__win)
            while self.__win.y > 420:
                self.__win.move(0, -5)
                pause(10)
            self.__win.y = 410
        else:
            self.ball.x = self.__window_width / 2 - self.__ball_radius
            self.ball.y = self.window_height / 2 - self.__ball_radius
        self.__dy = 0
        self.__dx = 0

    def lose(self):
        """
        1. turn all te bricks left into gray
        2. show "LOSE"
        """
        for j in range(self.__brick_rows):  # Draw bricks
            for i in range(self.__brick_cols):
                check = self.__window.get_object_at(i * (self.__brick_width + self.__brick_spacing),
                                                    j * (self.__brick_height + self.__brick_spacing) + self.__brick_offset)
                if check is not None:

                    self.__window.remove(check)
                    self.__brick = GRect(self.__brick_width, self.__brick_height, x=i*(self.__brick_width+self.__brick_spacing),
                                         y=j * (self.__brick_height + self.__brick_spacing) + self.__brick_offset)
                    self.set_brick(i*j+20)          # set brick color to gray

                    self.__window.add(self.__brick)   # add brick
        lose = GLabel("LOSE", x=125, y=500)
        lose.color = "Green"
        lose.font = "Verdana-70-bold"
        self.__window.add(lose)
