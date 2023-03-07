"""
M2Offline Database Manager
Author: Myth
----------------------
Ich dachte mir es wird SQLite genutzt, da es sehr einfach zu bedienen ist und
auch sehr schnell ist. Ich habe eine kleine Klasse erstellt, die die Tabellen
erstellt. Die Tabellen werden in der Klasse Schema definiert. Die Tabellen
werden in der Datei database.db gespeichert. Die Klasse Schema kann beliebig
erweitert werden. Die Tabellen werden beim ersten Starten der Anwendung
erstellt. Wenn die Datei database.db geloescht wird, werden die Tabellen
wieder erstellt.
"""

import sqlite3, time

class CharacterRace:
    WARRIOR_MALE        = 0
    WARRIOR_FEMALE      = 10
    SURA_MALE           = 1
    SURA_FEAMLE         = 11
    ASSASSIN_MALE       = 2
    ASSASSIN_FEMALE     = 12
    SHAMAN_MALE         = 3
    SHAMAN_FEMALE       = 13

class Schema:
    class Characters(dict):
        """
        Table: characters
        used to store different characters
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["name"]            = "TEXT"
            self["experience"]      = "INTEGER DEFAULT 0"
            self["create_date"]     = "DATETIME DEFAULT CURRENT_TIMESTAMP"
            self["play_time"]       = "INTEGER DEFAULT 0"
            self["race"]            = "INTEGER DEFAULT 0"
            self["job"]             = "INTEGER DEFAULT 0"
    class Items(dict):
        """
        Table: items
        used to store different items
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["character_id"]    = "INTEGER"
            self["name"]            = "TEXT"
            self["type"]            = "INTEGER"
            self["level"]           = "INTEGER"
            self["rarity"]          = "INTEGER"
            self["description"]     = "TEXT"
            self["icon"]            = "TEXT"
    class ItemProto(dict):
        """
        Table: item_proto
        used to store item prototypes
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["locale"]          = "TEXT"    # unused
            self["name"]            = "TEXT"
            self["type"]            = "INTEGER"
            self["sub_type"]        = "INTEGER"
    class MobProto(dict):
        """
        Table: mob_proto
        used to store mob prototypes
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["locale"]          = "TEXT"    # unused
            self["name"]            = "TEXT"
            self["type"]            = "INTEGER"
            self["sub_type"]        = "INTEGER"
    class AtlasInfo(dict):
        """
        Table: atlas_info
        used to store map information
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["name"]            = "TEXT"
            self["global_x"]        = "INTEGER"                 # global x position on atlas map (world map)
            self["global_y"]        = "INTEGER"                 # global y position on atlas map (world map)
            self["base_x"]          = "INTEGER DEFAULT 0"       # start x position (local map position, its global position - global_x and global_y)
            self["base_y"]          = "INTEGER DEFAULT 0"       # start y position
            self["width"]           = "INTEGER DEFAULT 1"       # 2d width of map
            self["height"]          = "INTEGER DEFAULT 1"       # 2d height of map
            self["minimap"]         = "TEXT"                    # minimap image path
    class QuestStates(dict):
        """
        Table: quests
        used to store quests
        """
        def __init__(self):
            self["id"]              = "INTEGER PRIMARY KEY"
            self["key"]             = "TEXT"
            self["value"]           = "TEXT"

    def __init__(self):
        self.tables = {}
        self.tables["characters"]   = self.Characters()
        self.tables["items"]        = self.Items()
        self.tables["item_proto"]   = self.ItemProto()
        self.tables["mob_proto"]    = self.MobProto()
        self.tables["atlas_info"]   = self.AtlasInfo()
        self.tables["quest_states"] = self.QuestStates()

def create_tables():
    conn = sqlite3.connect('m2offline.db')
    c = conn.cursor()
    for table in Schema().tables:
        print("Creating table: %s" % table)
        columns = []
        for column in Schema().tables[table]:
            columns.append("%s %s" % (column, Schema().tables[table][column]))
            print("Adding column: %s" % column)
        c.execute("CREATE TABLE %s (%s)" % (table, ", ".join(columns)))
    conn.commit()
    conn.close()
def create_character(name, race, job):
    conn = sqlite3.connect('m2offline.db')
    c = conn.cursor()
    c.execute("INSERT INTO characters (name, race, job) VALUES ('%s', %d, %d)" % (name, race, job))
    conn.commit()
    conn.close()
def query(sql):
    conn = sqlite3.connect('m2offline.db')
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    conn.close()
    return rows

def create_atlasinfo_entries(atlasinfo_path):
    with open(atlasinfo_path, "r") as f:
        data = f.read()
        data = data.split("\n")
        print("Found %d entries" % len(data))
        for line in data:
            print("Processing line: %s" % line)
            line = line.split("\t")
            if len(line) == 5:
                conn = sqlite3.connect('m2offline.db')
                c = conn.cursor()
                c.execute("INSERT INTO atlas_info (name, global_x, global_y, width, height) VALUES ('%s', %d, %d, %d, %d)" % (line[0], int(line[1]), int(line[2]), int(line[3]), int(line[4])))
                conn.commit()
                conn.close()

if __name__ == "__main__":
    create_tables()
    create_character("Myth", CharacterRace.WARRIOR_MALE, 1)
    create_atlasinfo_entries("atlasinfo.txt")
    _ = query("SELECT * FROM characters")
    print(_)
