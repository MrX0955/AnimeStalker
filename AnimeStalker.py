import requests
from lxml import html
from colorama import Fore
import time
import os

os.system("cls")
os.system("echo off")
os.system("cls")

def menuu():
    print(Fore.LIGHTGREEN_EX)
    menu = """Developer: [DefaceR]MrX ..!"""
    return menu
print(menuu())
def banner():
    print(Fore.GREEN)
    HasFa = """
        Anime Stats And Last Anime Updates => 1
        Manga Stats And Last Manga Updates => 2
    """
    return HasFa
print(banner())

choice = input("İstatistik Numarası Gir: ")
os.system("cls")

if "1" in choice:
    pass
elif "2" in choice:
    pass
else:
    print(Fore.LIGHTRED_EX)
    print("Hiç yakıştıramadım.")
    time.sleep(1)
    exit()

print(menuu())
MrX = input(f"\n {Fore.RED} Profile Name [Example: HasFa or tgkkk] = ").strip()
os.system("cls")

if choice == "1":
    def animestats():
        page = requests.get(f"https://myanimelist.net/profile/{MrX}")
        tree = html.fromstring(page.content)
        LastOnline = tree.xpath('//*[@id="content"]/div/div[1]/div/ul[1]/li[1]/span[2]/text()')
        JoinedDate = tree.xpath('//*[@id="content"]/div/div[1]/div/ul[1]/li[2]/span[2]/text()')
        Gun = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[1]/div[1]/text()')
        Watching = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[1]/span/text()')
        Completed = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[2]/span/text()')
        OnHold = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[3]/span/text()')
        Dropped = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[4]/span/text()')
        PlanToWatch = tree.xpath('//*[@id="statistics"]/div[1]/div[1]/div[3]/ul[1]/li[5]/span/text()')
        print(Fore.LIGHTMAGENTA_EX)
        print(f"Days: {Gun}\nWatching: {Watching}\nCompleted: {Completed}\nOnHold: {OnHold}\nDropped: {Dropped}\nPlanToWatch: {PlanToWatch}\nLastOnline: {LastOnline}\nJoinedDate: {JoinedDate}")

        one = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[1]/div/a/text()')
        Timeone = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[1]/div/div[1]/span/text()')
        two = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[2]/div/a/text()')
        Timetwo = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[2]/div/div[1]/span/text()')
        three = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[3]/div/a/text()')
        Timethree = tree.xpath('//*[@id="statistics"]/div[1]/div[2]/div[3]/div/div[1]/span/text()')

        print(Fore.LIGHTMAGENTA_EX)
        print(f"First: {one} >> {Timeone}\nSecond: {two} >> {Timetwo}\nThree: {three} >> {Timethree}")

    animestats()

if choice == "2":
    def mangastats():
        page = requests.get(f"https://myanimelist.net/profile/{MrX}")
        tree = html.fromstring(page.content)
        LastOnline = tree.xpath('//*[@id="content"]/div/div[1]/div/ul[1]/li[1]/span[2]/text()')
        JoinedDate = tree.xpath('//*[@id="content"]/div/div[1]/div/ul[1]/li[2]/span[2]/text()')
        day = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[1]/div[1]/text()')
        Reading = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[3]/ul[1]/li[1]/span/text()')
        Completed = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[3]/ul[1]/li[2]/span/text()')
        OnHold = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[3]/ul[1]/li[3]/span/text()')
        Dropped = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[3]/ul[1]/li[4]/span/text()')
        PlanToWatch = tree.xpath('//*[@id="statistics"]/div[2]/div[1]/div[3]/ul[1]/li[5]/span/text()')
        print(Fore.LIGHTMAGENTA_EX)
        print(f"Days: {day}\nWatching: {Reading}\nCompleted: {Completed}\nOnHold: {OnHold}\nDropped: {Dropped}\nPlanToWatch: {PlanToWatch}\nLastOnline: {LastOnline}\nJoinedDate: {JoinedDate}")

        one = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[1]/div/a/text()')
        Timeone = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[1]/div/div[1]/span/text()')
        two = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[2]/div/a/text()')
        Timetwo = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[2]/div/div[1]/span/text()')
        three = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[3]/div/a/text()')
        Timethree = tree.xpath('//*[@id="statistics"]/div[2]/div[2]/div[3]/div/div[1]/span/text()')
        print(Fore.LIGHTMAGENTA_EX)
        print(f"First: {one} >> {Timeone}\nSecond: {two} >> {Timetwo}\nThree: {three} >> {Timethree}")

    mangastats()