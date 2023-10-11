# Import necessary libraries
import pygame  # Import the Pygame library for game development
import sys  # Import the Sys library for system-specific functions
import pygame.mixer  # Import the Pygame mixer for sound/music handling

# Create a Game class to manage the game
class Game:
    # Constructor to initialize the game
    def __init__(self):
        # Initialize pygame and the mixer
        pygame.init()  # Initialize the Pygame library
        pygame.mixer.init()  # Initialize the Pygame mixer for sound

        # Load background music ('music.mp3' is the file to be replaced with your music file)
        pygame.mixer.music.load('music.mp3')

        # Set the music volume to 50% (0.5)
        pygame.mixer.music.set_volume(0.5)

        # Play the music in an infinite loop (-1 to loop indefinitely)
        pygame.mixer.music.play(-1)

        # Define constants for screen dimensions and colors
        self.WIDTH, self.HEIGHT = 1280, 720  # Set the screen width and height
        self.WHITE = (255, 255, 255)  # Define the color white as (R, G, B)

        # Create the game screen and set its title
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Music Quiz")  # Set the window title

        # Load various images for different game elements
        self.start_page_image = pygame.image.load("start_page.jpg")
        self.setting_page = pygame.image.load("setting_page.png")
        self.button_image = pygame.image.load("start.png")
        self.true_button_image = pygame.image.load("true.png")
        self.false_button_image = pygame.image.load("false.png")
        self.setting_button_image = pygame.image.load("setting.png")
        self.quit_button_image = pygame.image.load("quit.png")
        self.winner_image = pygame.image.load("win.jpg")
        self.incorrect_image = pygame.image.load("incorrect.png")
        self.correct_image = pygame.image.load("correct.png")
        self.return_image = pygame.image.load("return.png")
        self.return_image2 = pygame.image.load("return2.png")
        self.sound_on = pygame.image.load("sound_on.png")
        self.sound_off = pygame.image.load("sound_off.png")

        # Initialize game state variables
        self.score = 0  # Initialize the player's score
        self.answers = [False, True, True, False, True, True, False, True, False]  # Define the correct answers for the quiz
        self.quiz_no = 0  # Initialize the quiz question number
        self.timer_font = pygame.font.Font(None, 36)  # Set the font for the timer display
        self.timer = 20  # Initial value for the timer in seconds
        self.timer_text = None  # Initialize the timer display text
        self.timer_active = False  # Flag to indicate if the timer is active
        self.last_time = pygame.time.get_ticks()  # Get the initial time for the timer
        self.sound_flag = 0  # Flag for controlling sound

        # Load quiz page images and scale them
        self.quiz_page_images = [pygame.transform.smoothscale(pygame.image.load("{}.jpg".format(i)), (self.WIDTH, self.HEIGHT)) for i in range(1, 10)]
        self.start_page_image = pygame.transform.smoothscale(self.start_page_image, (self.WIDTH, self.HEIGHT))
        self.winner_image = pygame.transform.smoothscale(self.winner_image, (self.WIDTH, self.HEIGHT))
        self.incorrect_image = pygame.transform.smoothscale(self.incorrect_image, (self.WIDTH, self.HEIGHT))
        self.correct_image = pygame.transform.smoothscale(self.correct_image, (self.WIDTH, self.HEIGHT))
        self.setting_page = pygame.transform.smoothscale(self.setting_page, (self.WIDTH, self.HEIGHT))
        self.return_image2 = pygame.transform.scale(self.return_image2, (self.return_image.get_width() // 6, self.return_image.get_height() // 6))
        self.return_image = pygame.transform.scale(self.return_image, (self.return_image.get_width() // 6, self.return_image.get_height() // 6))
        self.button_image = pygame.transform.scale(self.button_image, (self.button_image.get_width() // 4, self.button_image.get_height() // 4))
        self.sound_on = pygame.transform.scale(self.sound_on, (self.sound_on.get_width() // 4, self.sound_on.get_height() // 4))
        self.sound_off = pygame.transform.scale(self.sound_off, (self.sound_off.get_width() // 4, self.sound_off.get_height() // 4))
        self.true_button_image = pygame.transform.scale(self.true_button_image, (self.true_button_image.get_width() // 2.2, self.true_button_image.get_height() // 2.2))
        self.false_button_image = pygame.transform.scale(self.false_button_image, (self.false_button_image.get_width() // 2.1, self.false_button_image.get_height() // 2.1))
        self.setting_button_image = pygame.transform.scale(self.setting_button_image, (self.setting_button_image.get_width() // 6, self.setting_button_image.get_height() // 6))
        self.quit_button_image = pygame.transform.scale(self.quit_button_image, (self.quit_button_image.get_width() // 6, self.quit_button_image.get_height() // 6))

        # Create buttons and hitboxes for user interactions
        self.start_btn = self.button_image.get_rect()
        self.start_btn.x = 380
        self.start_btn.y = 450
        self.quit_btn = self.quit_button_image.get_rect()
        self.quit_btn.center = (200, 200)
        self.quit_btn.x = 750
        self.quit_btn.y = 500
        self.true_btn = self.true_button_image.get_rect()
        self.true_btn.x = 27  # X position
        self.true_btn.y = 49  # Y position
        self.false_btn = self.false_button_image.get_rect()
        self.false_btn.x = 378  # X position
        self.false_btn.y = 63  # Y position
        self.setting_btn = self.setting_button_image.get_rect()
        self.setting_btn.center = (self.WIDTH // 14, self.HEIGHT // 14)
        self.setting_btn.x = 130
        self.setting_btn.y = 500
        self.return_btn = self.return_image.get_rect()
        self.return_btn.center = (self.WIDTH // 14, self.HEIGHT // 14)
        self.return_btn.x = 950
        self.return_btn.y = 550
        self.return_btn2 = self.return_image2.get_rect()
        self.return_btn2.center = (self.WIDTH // 14, self.HEIGHT // 14)
        self.return_btn2.x = 950
        self.return_btn2.y = 550
        self.sound_on_btn = self.sound_on.get_rect()
        self.sound_on_btn.center = (self.WIDTH // 14, self.HEIGHT // 14)
        self.sound_on_btn.x = 400
        self.sound_on_btn.y = 300
        self.sound_off_btn = self.sound_off.get_rect()
        self.sound_off_btn.center = (self.WIDTH // 14, self.HEIGHT // 14)
        self.sound_off_btn.x = 400
        self.sound_off_btn.y = 300
        self.start_hitbox = pygame.Rect(500, 400, 200, 200)
        self.true_hitbox = pygame.Rect(330, 200, 200, 200)
        self.false_hitbox = pygame.Rect(730, 200, 200, 200)
        self.current_page = "start"  # Track the current page (start/quiz)
        self.current_quiz_page = 0  # Track the current quiz page index
        self.score_font = pygame.font.Font(None, 50)  # Set the font for the score display
        self.score_text = None
        self.score = 0  # Initialize the player's score

    # Method to start the quiz
    def Quiz(self):
        # Check if the current page is "start" before proceeding
        if self.current_page == "start":
            self.current_page = "quiz"
            self.current_quiz_page = 0
            self.score = 0
            self.start_timer()

    # Method to start the timer for each quiz question
    def start_timer(self):
        # Initialize the timer to 10 seconds
        self.timer = 20
        self.timer_active = True
        self.last_time = pygame.time.get_ticks()

    # Method to update the timer
    def update_timer(self):
        if self.timer_active:
            current_time = pygame.time.get_ticks()
            # Calculate elapsed time in seconds
            elapsed_time = (current_time - self.last_time) / 1000
            self.timer -= elapsed_time

            if self.timer <= 0:
                self.timer_active = False
                self.current_quiz_page += 1
                if self.current_quiz_page == 9:
                    # Check the score and set the current page accordingly
                    if self.score >= 5:
                        self.current_page = "correct"
                    else:
                        self.current_page = "incorrect"
                    self.timer_active = False  # Ensure the timer is stopped
                else:
                    self.start_timer()  # Start a new timer for the next quiz question
            else:
                # Update the timer text
                self.timer_text = self.timer_font.render(f"Time: {int(self.timer)} s", True, (255, 255, 255))
                self.last_time = current_time

    # Method to handle True or False responses
    def True_or_False(self, action):
        if self.current_page == "quiz":  # Make sure you are on the quiz page
            if action:
                if self.answers[self.current_quiz_page]:
                    self.score += 1
            else:
                if not self.answers[self.current_quiz_page]:
                    self.score += 1

            self.current_quiz_page += 1

            if self.current_quiz_page == 9:
                self.timer_active = False  # Ensure the timer is stopped
                if self.score >= 5:
                    self.current_page = "correct"
                else:
                    self.current_page = "incorrect"
            else:
                self.start_timer()  # Start a new timer for the next quiz question

    # Method to control the game's sound
    def Sound_control(self):
        if self.sound_flag == 0:
            self.sound_flag = 1
            pygame.mixer.music.pause()
        else:
            self.sound_flag = 0
            pygame.mixer.music.unpause()

    # Method to run the game
    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_hitbox.collidepoint(event.pos):
                        self.Quiz()
                    elif self.quit_btn.collidepoint(event.pos):
                        running = False
                    elif self.true_hitbox.collidepoint(event.pos):
                        self.True_or_False(True)
                    elif self.false_hitbox.collidepoint(event.pos):
                        self.True_or_False(False)
                    elif self.return_btn.collidepoint(event.pos):
                        self.current_page = "start"
                        self.score = 0
                    elif self.setting_btn.collidepoint(event.pos):
                        self.current_page = "setting"
                    elif self.sound_on_btn.collidepoint(event.pos):
                        self.Sound_control()

            self.update_timer()
            self.screen.fill(self.WHITE)

            if self.current_page == "start":
                self.screen.blit(self.start_page_image, (0, 0))
                self.screen.blit(self.button_image, self.start_btn)
                self.screen.blit(self.quit_button_image, self.quit_btn)
                self.screen.blit(self.setting_button_image, self.setting_btn)
            elif self.current_page == "quiz":
                self.screen.blit(self.quiz_page_images[self.current_quiz_page], (0, 0))
                self.screen.blit(self.true_button_image, self.true_btn)
                self.screen.blit(self.false_button_image, self.false_btn)
                self.screen.blit(self.return_image, self.return_btn)
                self.screen.blit(self.timer_text, (self.WIDTH - 150, 10))

                score_text = self.score_font.render(f"Score: {self.score}/9", True, (255, 255, 255))
                self.screen.blit(score_text, (10, 10))
            elif self.current_page == "correct":
                self.screen.blit(self.correct_image, (0, 0))
                pygame.display.flip()
                pygame.time.delay(2000)  # Delay for 2 seconds
                self.current_page = "start"  # Go back to the start page
                self.score = 0
            elif self.current_page == "incorrect":
                self.screen.blit(self.incorrect_image, (0, 0))
                pygame.display.flip()
                pygame.time.delay(2000)  # Delay for 2 seconds
                self.current_page = "start"  # Go back to the start page
                self.score = 0
            elif self.current_page == "setting":
                self.screen.blit(self.setting_page, (0, 0))
                self.screen.blit(self.return_image2, self.return_btn2)
                if self.sound_flag == 0:
                    self.screen.blit(self.sound_on, self.sound_on_btn)
                else:
                    self.screen.blit(self.sound_off, self.sound_off_btn)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()
# Main program entry point
if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.run()  # Start the game
