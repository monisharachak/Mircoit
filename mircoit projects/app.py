import streamlit as st

# Initialize session state for board and current player
if 'board' not in st.session_state:
    st.session_state.board = [""] * 9
if 'current_player' not in st.session_state:
    st.session_state.current_player = "X"
if 'winner' not in st.session_state:
    st.session_state.winner = None

# Winning combinations (row, column, diagonal)
winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Check for a winner
def check_winner():
    for combo in winning_combinations:
        a, b, c = combo
        if st.session_state.board[a] == st.session_state.board[b] == st.session_state.board[c] != "":
            return st.session_state.board[a]
    return None

# Reset the game
def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None

st.title("🎮 Tic-Tac-Toe Game")
st.markdown("Play a classic game of Tic-Tac-Toe!")

# Display the 3x3 board using columns
for i in range(0, 9, 3):
    cols = st.columns(3)
    for j in range(3):
        index = i + j
        with cols[j]:
            if st.session_state.board[index] == "" and st.session_state.winner is None:
                if st.button(" ", key=index, help="Click to make a move"):
                    st.session_state.board[index] = st.session_state.current_player
                    st.session_state.winner = check_winner()
                    if not st.session_state.winner:
                        # Check for draw
                        if "" not in st.session_state.board:
                            st.session_state.winner = "Draw"
                        else:
                            # Switch player
                            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            else:
                st.markdown(f"## {st.session_state.board[index]}")

# Display the game result
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.success("It's a draw! 🤝")
    else:
        st.success(f"Player {st.session_state.winner} wins! 🎉")

# Reset button
st.button("🔄 Restart Game", on_click=reset_game)
