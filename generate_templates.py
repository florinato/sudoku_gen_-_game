import numpy as np

import sudoku_gen


def convert_to_letters(grid):
    # Replace numbers with letters (A=1, B=2, etc.)
    letter_grid = []
    for row in grid:
        letter_row = [chr(64 + num) if num != 0 else "." for num in row]
        letter_grid.append(letter_row)
    return letter_grid


def generate_and_save_templates(num_templates, filename="sudoku_templates.txt"):
    generated_grids = set()
    with open(filename, "w") as f:
        while len(generated_grids) < num_templates:
            generator = sudoku_gen.NewSudokuGeneratorWithDiagonals()
            generator.generate_sudoku()
            grid = generator.board.tolist()  # Convert numpy array to list
            
            # Convert to a tuple of tuples for hashability
            grid_tuple = tuple(tuple(row) for row in grid)
            
            if grid_tuple not in generated_grids:
                generated_grids.add(grid_tuple)
                letter_grid = convert_to_letters(grid)
                # Convert the 2D list to a string representation for the file
                template_string = "\\n".join(["".join(row) for row in letter_grid])
                f.write(template_string + "\\n\\n")  # Separate templates by two newlines


if __name__ == "__main__":
    generate_and_save_templates(10)
