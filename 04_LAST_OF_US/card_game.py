# Problem 3: Multiplayer Card Game
# Step 1: Basic Game Setup
# Create a basic setup for a multiplayer card game where users can join the game, and a deck of cards is shuffled and distributed among the players.
#
# Implement functions to create a game room, join a game, shuffle the deck, and distribute cards evenly among players.

# Step 2: Basic Gameplay Mechanics
# Extend the game to support basic gameplay mechanics, such as playing a card, drawing a card from the deck, and keeping track of each player’s hand.
#
# Implement functions for players to play a card and draw a card from the deck.
# Maintain the state of each player's hand and update it as cards are played or drawn.

# Step 3: Game Rules and Winning Conditions
# Add game rules and conditions to determine the winner. Define the rules for valid moves and implement a scoring system or winning conditions.
#
# Implement functions to check if a move is valid based on the game rules.
# Keep track of the scores or conditions required for a player to win the game.
# Implement logic to determine and announce the winner.
# Step 4: Concurrency Control for Multi-player Interaction
# Introduce concurrency control to handle simultaneous actions from multiple players, such as playing cards or drawing from the deck, ensuring the game state remains consistent.
#
# Implement locks or other synchronization mechanisms to manage concurrent actions.
# Ensure that the game state is accurately updated even with high concurrency.
# Step 5: Real-time Updates and Synchronization
# Enhance the game with real-time updates so all players see the current state of the game (e.g., played cards, current hands, scores) without delay.
#
# Implement WebSocket or similar real-time communication to broadcast game state changes to all players.
# Ensure that all players receive accurate and timely updates by managing concurrency and synchronization properly.
# Step 6: Chat Feature
# Add a chat feature to allow players to communicate with each other during the game.
#
# Implement a chat system where players can send and receive messages.
# Ensure that messages are displayed in real-time to all players.
# Step 7: Reconnection and Persistence
# Allow players to reconnect to the game if they lose their connection and persist the game state to prevent data loss.
#
# Implement a mechanism for players to reconnect to the game and restore their previous state.
# Use a database or in-memory store to persist the game state and player information.
# Summary of Steps
# Basic Game Setup: Game room creation, joining, shuffling, and card distribution.
# Basic Gameplay Mechanics: Playing and drawing cards, managing player hands.
# Game Rules and Winning Conditions: Valid moves, scoring system, determining the winner.
# Concurrency Control: Managing simultaneous actions, ensuring game state consistency.
# Real-time Updates and Synchronization: Broadcasting game state changes in real-time.
# Chat Feature: Real-time player communication.
# Reconnection and Persistence: Handling reconnections and persisting game state.
# This problem progressively adds new features and complexities, requiring updates to previous implementations and incorporating concurrency control to ensure a consistent and synchronized game experience.

from enum import Enum
from typing import List
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f'{self.value} of {self.suit}'

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class CardDeck:

    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.cards = []
        self.__shuffle()

    def __shuffle(self):
        self.cards = []
        for suit in self.suits:
            for number in self.numbers:
                self.cards.append(Card(suit, number))
        random.shuffle(self.cards)

    def draw(self, n) -> List[Card]:
        if len(self.cards) < n:
            raise Exception("Not enough cards")

        drawn_cards = []
        for i in range(n):
            drawn_cards.append(self.cards.pop())
        return drawn_cards


class UserType(Enum):
    GAMBLER = "GAMBLER"
    SMART = "SMART"
    RANDOM = "RANDOM"


class User:

    def __init__(self, name: str, user_type: UserType):
        self.name = name
        self.cards = None
        self.user_type = user_type

    def __repr__(self):
        return f"<User: {self.name}, cards: {self.cards}, user_type: {self.user_type}>"

    def set_cards(self, cards: List[Card]):
        self.cards = cards

    def get_cards(self) -> List[Card]:
        return self.cards

    def decide_to_replace(self, number: int) -> List[Card]:
        if number > len(self.cards):
            raise ValueError(f"Cannot replace more than {len(self.cards)} cards")

        if self.user_type == UserType.GAMBLER:
            # todo update later
            return random.choices(self.cards, k=number)
        elif self.user_type == UserType.SMART:
            # todo update later
            return random.choices(self.cards, k=number)
        elif self.user_type == UserType.RANDOM:
            return random.choices(self.cards, k=number)
        else:
            raise ValueError(f"Unknown user type: {self.user_type}")


class Game:

    def __init__(self, user_card_count:int):
        self.users = []
        self.current_user_index = -1
        self.carddeck = None
        self.started = False
        self.user_card_count = user_card_count

    def add_users(self, users: List[User]) -> bool:
        for user in users:
            self.add_user(user)
        return True

    def add_user(self, user: User) -> bool:
        if self.started:
            raise Exception('Already started')

        if user.name in [u.name for u in self.users]:
            raise Exception("User already exists")

        self.users.append(user)
        return True

    def reset(self):
        self.users = []
        self.current_user_index = -1
        self.carddeck = None
        self.started = False

    def start(self):
        if len(self.users) < 2:
            raise Exception('Not enough users')

        self.started = True
        self.carddeck = CardDeck()
        for user in self.users:
            drawn_cards = self.carddeck.draw(self.user_card_count)
            user.set_cards(drawn_cards)

        self.current_user_index = 0

    def print(self):
        print("Printing game status:")
        print("There are {} users in this game".format(len(self.users)))
        for user in self.users:
            print(user)

        if self.started:
            print("Current user is: {}".format(self.users[self.current_user_index]))

    def get_current_user(self) -> User:
        return self.users[self.current_user_index]

    def current_user_replace(self, replace_cards: List[Card]) -> User:
        the_user = self.get_current_user()

        current_cards = the_user.get_cards()
        for card in replace_cards:
            if card not in current_cards:
                raise Exception("User does not have card: {}".format(card))

        for card in replace_cards:
            current_cards.remove(card)

        remaining_count = len(current_cards)
        new_cards = self.carddeck.draw(self.user_card_count - remaining_count)
        new_cards.extend(current_cards)
        the_user.set_cards(new_cards)
        self.current_user_index += 1
        if self.current_user_index == len(self.users):
            self.current_user_index = 0

        return the_user

    def find_winner(self) -> User:
        pass

game = Game(2)
u_tahsin = User("Tahsin", user_type=UserType.SMART)
u_faisal = User("Faisal", user_type=UserType.RANDOM)
u_ahad = User("Ahad", user_type=UserType.SMART)
u_nafiz = User("Nafiz", user_type=UserType.GAMBLER)
users = [u_tahsin, u_faisal, u_ahad, u_nafiz]
game.add_users(users)
game.start()
# game.print()

rounds = 11  # 8 + 12 * 4 = 52
for round in range(rounds):
    print(f"Round {round}")
    for _ in range(len(users)):
        current_user = game.get_current_user()
        rc = current_user.decide_to_replace(1)
        game.current_user_replace(rc)
        game.print()

# game.find_winner()
