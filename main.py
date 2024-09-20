import json

class Card:
    def __init__(self):
        self.cards = {}
    
    def load_cards(self, file):
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for Card in data:
                    category = Card['category']
                    name = Card['name']
                    if category not in self.cards:
                        self.cards[category] = []
                    self.cards[category].append(name)
        except FileNotFoundError:
            print(f"File {file} not found.")
            raise SystemExit
        except json.JSONDecodeError:
            print("Wrong JSON syntax.")
            raise SystemExit

    def __str__(self):
        output = "Cards and categories:\n"
        for category, cards in self.cards.items():
            output += f"{category}:\n"
            for Card in cards:
                output += f"  - {Card}\n"
        return output

owned_cards = Card()
owned_cards.load_cards('cards.json')
print(owned_cards)