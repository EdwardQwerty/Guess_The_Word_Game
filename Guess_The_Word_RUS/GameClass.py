import random


class GuessTheWordGame:
    def __init__(self, allowed_tries: int = 15):

        if allowed_tries < 5 or allowed_tries > 15:
            raise ValueError('Allowed misses should be more than 5 and less than 15')

        self.__allowed_tries = allowed_tries
        self.__word = ""
        self.__lettered_word = []
        self.__showing_word = []
        self.__tries_passed = 0
        self.__used_letters = set()
        self.__used_words = set()

    # randomly generating word using dictionfry file
    def word_generation(self):
        path_to_file = "Dictionary_RUS.txt"
        words = []
        with open(path_to_file, "r", encoding="utf-8") as Dict:
            for line in Dict:
                words.append(line.strip())
        self.__word = words[random.randint(0, len(words))]
        self.__lettered_word = [i for i in self.__word]
        self.__showing_word = [" _" for i in self.__lettered_word]
        return self.__word

    # method to showing "_" for every letter of generated word
    def show_hidden_word(self):
        sw = ""
        for i in range(len(self.__showing_word)):
            sw = sw + self.__showing_word[i]
        return sw

    # method to check is player's input correct
    def is_player_input_correct(self, player_guess):
        alphabet = {
            'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
            'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
            'ч', 'ш', 'щ', 'ь', 'ы', 'ъ', 'э', 'ю', 'я'
        }
        player_guess_lettered = {i for i in player_guess.lower()}
        is_input_correct = player_guess_lettered.issubset(alphabet)
        return is_input_correct

    # method to check player's input is a letter or a word
    def letter_or_word(self, player_guess):
        l_or_w = ""
        if len(player_guess) > 1:
            l_or_w = "word"
        elif len(player_guess) == 1:
            l_or_w = "letter"
        return l_or_w

    # method to check number of letters of player's guess word
    def word_len_check(self, player_guess):
        if len(player_guess) == len(self.__word):
            is_number_of_letter_correct = True
        else:
            is_number_of_letter_correct = False
        return is_number_of_letter_correct

    # method to checking player's input letter
    def checking_letter(self, player_guess):
        if player_guess in self.__used_letters:
            return "Repeated letter"
        else:
            self.__used_letters.add(player_guess)
            if player_guess not in self.__lettered_word:
                self.__tries_passed += 1
                return "Wrong letter"
            elif player_guess in self.__lettered_word:
                for i in range(len(self.__lettered_word)):
                    if self.__lettered_word[i] == player_guess:
                        self.__showing_word[i] = player_guess
                return "Right letter"

    # method to checking player's input word
    def checking_word(self, player_guess):
        if player_guess.lower() in self.__used_words:
            return "Repeated word"
        else:
            self.__used_words.add(player_guess)
            if player_guess.lower() == self.__word:
                return "Right word"
            else:
                self.__tries_passed += 1
                return "Wrong word"

    # method to checking player's win when they input whole word letter by letter
    def checking_win_by_letter(self):
        if (self.__allowed_tries - self.__tries_passed) >= 0 \
                and (self.__showing_word == self.__lettered_word):
            return True
        else:
            return False

    # method to check that player still have tries
    def checking_remaining_tries(self):
        if (self.__allowed_tries - self.__tries_passed) > 0:
            return True
        else:
            return False

    def show_used_letters(self):
        show_used_letters = ""
        used_lettres_list = list(self.__used_letters)
        used_lettres_list.sort()
        for i in range(len(used_lettres_list)):
            show_used_letters = show_used_letters + used_lettres_list[i] + ", "
        return show_used_letters

    def show_used_words(self):
        show_used_words = ""
        used_words_list = list(self.__used_words)
        used_words_list.sort()
        for i in range(len(used_words_list)):
            show_used_words = show_used_words + used_words_list[i] + ", "
        return show_used_words

    @property
    def word_len(self):
        return len(self.__lettered_word)

    @property
    def tries_remaining(self):
        return self.__allowed_tries - self.__tries_passed

    @property
    def used_letters_property(self):
        return self.__used_letters

    @property
    def generated_word(self):
        return self.__word

    @property
    def showed_word(self):
        return self.__showing_word

