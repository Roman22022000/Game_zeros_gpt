import os
os.environ.setdefault("PYGLET_HEADLESS", "True")

import arcade

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
CELL_SIZE = 60
GRID_COLOR_BLUE = arcade.color.BLUE
GRID_COLOR_GREEN = arcade.color.GREEN
HIGHLIGHT_COLOR = arcade.color.YELLOW


class GridApp(arcade.Window):
    """Simple grid where cells can be toggled between blue and green.

    Arrow keys move a cursor. Press SPACE to toggle the color of the
    highlighted cell. PAGEUP and PAGEDOWN move between stacked grid layers.
    """

    def __init__(self) -> None:
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Grid")
        self.cols = WINDOW_WIDTH // CELL_SIZE
        self.rows = WINDOW_HEIGHT // CELL_SIZE
        self.cx = 0
        self.cy = 0
        self.layers = [self._create_layer()]
        self.current_layer = 0
        arcade.set_background_color(arcade.color.BLACK)

    def _create_layer(self):
        return [
            [GRID_COLOR_BLUE for _ in range(self.cols)]
            for _ in range(self.rows)
        ]

    def on_draw(self) -> None:
        """Render stacked grids and highlight the cursor."""
        arcade.start_render()
        for idx, layer in enumerate(self.layers):
            offset = idx * 5
            for row in range(self.rows):
                for col in range(self.cols):
                    color = layer[row][col]
                    x = col * CELL_SIZE + CELL_SIZE / 2
                    y = row * CELL_SIZE + CELL_SIZE / 2 + offset
                    arcade.draw_rectangle_filled(
                        x, y, CELL_SIZE, CELL_SIZE, color
                    )
                    arcade.draw_rectangle_outline(
                        x, y, CELL_SIZE, CELL_SIZE, arcade.color.GRAY
                    )

        x = self.cx * CELL_SIZE + CELL_SIZE / 2
        y = self.cy * CELL_SIZE + CELL_SIZE / 2 + self.current_layer * 5
        arcade.draw_rectangle_outline(
            x, y, CELL_SIZE, CELL_SIZE, HIGHLIGHT_COLOR, 3
        )
        arcade.draw_text(
            f"Layer: {self.current_layer}",
            10,
            WINDOW_HEIGHT - 20,
            arcade.color.WHITE,
            12,
        )

    def on_key_press(self, key, modifiers) -> None:
        if key == arcade.key.RIGHT and self.cx < self.cols - 1:
            self.cx += 1
        elif key == arcade.key.LEFT and self.cx > 0:
            self.cx -= 1
        elif key == arcade.key.UP and self.cy < self.rows - 1:
            self.cy += 1
        elif key == arcade.key.DOWN and self.cy > 0:
            self.cy -= 1
        elif key == arcade.key.SPACE:
            self._toggle_cell()
        elif key == arcade.key.PAGEUP:
            self._raise_layer()
        elif key == arcade.key.PAGEDOWN:
            self._lower_layer()

    def _toggle_cell(self) -> None:
        """Toggle color of the cell under the cursor."""
        layer = self.layers[self.current_layer]
        color = layer[self.cy][self.cx]
        layer[self.cy][self.cx] = (
            GRID_COLOR_GREEN if color == GRID_COLOR_BLUE else GRID_COLOR_BLUE
        )

    def _raise_layer(self) -> None:
        """Move up to a higher layer, creating one if needed."""
        self.current_layer += 1
        if self.current_layer >= len(self.layers):
            self.layers.append(self._create_layer())

    def _lower_layer(self) -> None:
        """Move down to a lower layer if possible."""
        if self.current_layer > 0:
            self.current_layer -= 1


def main() -> None:
    GridApp()
    arcade.run()


if __name__ == "__main__":
    main()
