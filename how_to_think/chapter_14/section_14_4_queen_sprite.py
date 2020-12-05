gravity = 1e-3


class QueenSprite:
    def __init__(self, img, target_position):
        """
        Create and initialize a queen for this
        target position on the board
        """

        self.image = img
        self.target_posn = target_position
        x, y = target_position
        self.position = (x, 0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        x, y = self.position
        new_y_pos = y + self.y_velocity
        (target_x, target_y) = self.target_posn         # Unpack the position
        dist_to_go = target_y - new_y_pos               # How far to our floor?

        if dist_to_go < 0:                              # Are we under floor?
            self.y_velocity = -0.65 * self.y_velocity   # Bounce
            new_y_pos = target_y + dist_to_go           # Move back above floor

        self.position = (x, new_y_pos)                  # Set our new position.

    def draw(self, target_surface):
        target_surface.blit(self.image, self.position)

    def contains_point(self, point):
        """ Return True if my sprite (rectangle) contains point """
        my_x, my_y = self.position
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        x, y = point
        return my_x <= x < (my_x + my_width) and my_y <= y < (my_y + my_height)

    def handle_click(self):
        self.y_velocity += -.3
