# Add "My todo:" to the beginning of the todoText
# Add " - Download games" to the end of the todoText
# Add " - Diablo" to the end of the todoText but with indention

# Expected outpt:

# My todo:
#  - Buy milk
#  - Download games
#      - Diablo

todoText = " - Buy milk\n"

todoText = todoText[0] + "My todo\n" + todoText[1:12] + "-Download games\n" + "\t -Diablo"


print(todoText)