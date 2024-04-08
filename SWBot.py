import tkinter as tk
from bots.ClanBattle import ClanBattleBot
from bots.ClanBattleQuick import ClanBattleQuickBot
from bots.XPFarm import XPFarmBot
from bots.Arena import ArenaBot


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SW Bot")
        self.root.configure(bg="#2B2B2B")
        self.root.geometry("300x150")

        self.bot_options = ["XP Farm", "Arena",
                            "Clan Battle", "Clan Battle Quick"]
        self.selected_bot = tk.StringVar(root)
        self.selected_bot.set(self.bot_options[0])

        self.setup_dropdown()
        self.setup_buttons()

        self.root.attributes('-topmost', True)
        self.root.geometry("+0+0")

    def setup_dropdown(self):
        self.dropdown_label = tk.Label(
            self.root, text="Select Bot:", bg="#2B2B2B", fg="#00FF00", font=("Arial", 14))
        self.dropdown_label.pack()

        self.dropdown = tk.OptionMenu(
            self.root, self.selected_bot, *self.bot_options)
        self.dropdown.config(bg="#2B2B2B", fg="#00FF00",
                             font=("Arial", 12))
        self.dropdown.pack()

    def setup_buttons(self):
        self.start_button = tk.Button(
            self.root, text="Start Bot", command=self.start_bot, bg="#2B2B2B", fg="#00FF00", font=("Arial", 12))
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(
            # Increase font size
            self.root, text="Stop Bot", command=self.stop_bot, bg="#2B2B2B", fg="#00FF00", font=("Arial", 12))
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

    def start_bot(self):
        bot_name = self.selected_bot.get()
        if bot_name == "XP Farm":
            self.start_xp_farm_bot()
        elif bot_name == "Arena":
            self.start_offline_arena_bot()
        elif bot_name == "Clan Battle":
            self.start_clan_battle_bot()
        elif bot_name == "Clan Battle Quick":
            self.start_clan_battle_quick_bot()

    def start_xp_farm_bot(self):
        self.clan_battle_bot = XPFarmBot()
        self.clan_battle_bot.start()

    def start_offline_arena_bot(self):
        self.clan_battle_bot = ArenaBot()
        self.clan_battle_bot.start()

    def start_clan_battle_bot(self):
        self.clan_battle_bot = ClanBattleBot()
        self.clan_battle_bot.start()

    def start_clan_battle_quick_bot(self):
        self.clan_battle_bot = ClanBattleQuickBot()
        self.clan_battle_bot.start()

    def stop_bot(self):
        if hasattr(self, 'xp_farm_bot'):
            self.clan_battle_bot.stop()
            return
        if hasattr(self, 'offline_arena'):
            self.start_offline_arena_bot.stop_bot()
            return
        if hasattr(self, 'clan_battle_bot'):
            self.clan_battle_bot.stop()
            return
        if hasattr(self, 'clan_battle_quick_bot'):
            self.start_clan_battle_quick_bot.stop()
            return


def main():
    root = tk.Tk()
    GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
