# 🎮 Connect 4 🎮

Welcome to **Connect 4**, a console-based version of the classic two-player connection game! The objective is simple: be the first player to connect four of your pieces in a row, column, or diagonal.

## 📋 Table of Contents

- [📝 Introduction](#introduction)
- [🎲 Gameplay](#gameplay)
- [💻 Installation](#installation)
- [🎮 How to Play](#how-to-play)
- [✨ Features](#features)

## 📝 Introduction

**Connect 4** is a classic two-player board game where players take turns dropping their discs into a vertical grid. The goal is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. The game ends when a player achieves this or when the board is full with no more possible moves.

## 🎲 Gameplay

The game is played on a grid of 6 rows and 7 columns. Each player has a set of discs, and they take turns choosing a column in which to drop their disc. The disc falls to the lowest available space in that column. The game ends when a player manages to connect four of their discs in a line (horizontally, vertically, or diagonally) or when the grid is completely filled without any player achieving the objective, resulting in a draw.

## 💻 Installation

To compile and run **Connect 4**, ensure you have a C++ compiler installed on your system. Follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/nicolas-droppa/Connect-4-Videogame.git
    cd Connect4-Game
    ```

2. Compile the code:
    ```sh
    g++ -o Connect-4-Videogame main.cpp
    ```

3. Run the executable:
    ```sh
    ./Connect-4-Videogame
    ```

## 🎮 How to Play

Use the following keys to control the game:

- **A** or **a** - Drop disc in Column 1
- **B** or **b** - Drop disc in Column 2
- **C** or **c** - Drop disc in Column 3
- **D** or **d** - Drop disc in Column 4
- **E** or **e** - Drop disc in Column 5
- **F** or **f** - Drop disc in Column 6
- **G** or **g** - Drop disc in Column 7

The goal is to be the first to connect four of your discs in a row, column, or diagonal.

### Example Gameplay

![Example Gameplay](https://github.com/user-attachments/assets/example_connect4_gameplay.png)

## ✨ Features

- **🎮 Simple Controls**: Use the **A, B, C, D, E, F, G** keys to place your discs in the desired column.
- **🎨 Customizable Players**: Players can set their names and choose symbols to represent their discs.
- **🖥️ Dynamic Board Display**: The game board updates in real-time after each move, providing an engaging experience.
- **🔀 Winning Detection**: The game automatically detects a win or a draw and displays the result accordingly.

---

Thank you for playing **Connect 4**! 🌟
