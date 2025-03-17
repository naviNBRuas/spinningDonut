import os
from math import sin, cos

def main():
    a = 0
    b = 0

    # Function to clear console based on the operating system
    def clear_console():
        os.system("cls" if os.name == 'nt' else "clear")

    # Initial clear of the console
    clear_console()

    while True:
        # Initialize arrays to store z-buffer and screen characters
        z_buffer = [0] * 1760
        screen = [' '] * 1760

        # Loop for theta (j)
        j = 0
        while j < 6.28:
            j += 0.07

            # Loop for phi (i)
            i = 0
            while i < 6.28:
                i += 0.02

                # Calculate trigonometric values
                sin_a = sin(a)
                cos_a = cos(a)
                cos_b = cos(b)
                sin_b = sin(b)

                sin_i = sin(i)
                cos_i = cos(i)
                cos_j = cos(j)
                sin_j = sin(j)

                cos_j2 = cos_j + 2
                mess = 1 / (sin_i * cos_j2 * sin_a + sin_j * cos_a + 5)
                t = sin_i * cos_j2 * cos_a - sin_j * sin_a

                # Calculate x and y coordinates
                x = int(40 + 30 * mess * (cos_i * cos_j2 * cos_b - t * sin_b))
                y = int(12 + 15 * mess * (cos_i * cos_j2 * sin_b + t * cos_b))
                o = x + 80 * y
                n = int(8 * ((sin_j * sin_a - sin_i * cos_j * cos_a) *
                        cos_b - sin_i * cos_j * sin_a - sin_j * 
                        cos_a - cos_i * cos_j * sin_b))

                # Check if the point is within the screen boundaries 
                #and closer than previous points
                if 0 < y < 22 and 0 < x < 80 and z_buffer[o] < mess:
                    z_buffer[o] = mess
                    screen[o] = ".,-~:;=!*#$@"[n if n > 0 else 0]

        # Clear console and print the screen
        clear_console()
        for index, char in enumerate(screen):
            print(char, end='')
            if (index + 1) % 80 == 0:
                print()

        # Increment angles for next frame
        a += 0.04
        b += 0.02

if __name__ == "__main__":
    main()
