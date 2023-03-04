def minion_game(string):
    # start by initialising the values
    i = 0
    j = 1
    stuart_score = 0
    kevin_score = 0
    vowels = "AEIOU" 
    # alphabet = string.ASCII_uppercase()
    while i < len(string):
        if string[i] in vowels:
            kevin_score += len(string)-i
            i += 1
        else:
            stuart_score += len(string) - i
            i += 1
    if stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    elif stuart_score == kevin_score:
        return "Draw"
    else:
        return f"Kevin {kevin_score}"
    
print(minion_game("BANANA"))