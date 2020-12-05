class DukeSprite:

    def __init__(self, image, target_position):
        self.image = image
        self.position = target_position
        self.animation_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.animation_frame_count > 0:
            self.animation_frame_count = (self.animation_frame_count + 1) % 300     # slowed it down to look nicer
            self.curr_patch_num = self.animation_frame_count // 30

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0, 50, self.image.get_height())
        target_surface.blit(self.image, self.position, patch_rect)

    def handle_click(self):
        if self.animation_frame_count == 0:
            self.animation_frame_count = 5

    def contains_point(self, point):
        """ Return True if my sprite (rectangle) contains point """
        my_x, my_y = self.position
        my_width = 50
        my_height = self.image.get_height()
        x, y = point
        return my_x <= x < (my_x + my_width) and my_y <= y < (my_y + my_height)
