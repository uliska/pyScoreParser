import re

class NameScoreTable:
    def __init__(self):
        self.names = []
        self.scores = []
        self.years = []

    def append(self, pair):
        self.names.append(pair.name.lower())
        self.scores.append(pair.score)
        self.years.append(pair.year)

    def get_score(self, name, year=False):
        if name in self.names:
            if year:
                indices = [i for i, x in enumerate(self.names) if x == name]
                for i in indices:
                    if self.years[i] == year:
                        index = i
            else:
                index = self.names.index(name)
            score = self.scores[index]
            year = self.years[index]
            return score, year
        else:
            print('Error: No matching name, ', name)
            return None, None

class NameScorePair:
    def __init__(self, name, score, year):
        self.name = name
        self.score = score
        self.year = year


def define_perf_name_to_score():
    # 1st prize = 6
    # 2nd to 3rd prize = 5
    # 4th to 6th prize = 4
    # final = 3
    # semi_final = 2
    # second round = 1
    # audition, first round = 0
    name_score_table = NameScoreTable()
    name_score_table.extend(( # double parenthesis to extend with a tuple
        NameScorePair('Dossin', 0, 2002),
        NameScorePair('Ali', 0, 2008),
        NameScorePair('Day', 0, 2006),
        NameScorePair('Jia', 1, 2004), #check ran jia and jia ran
        NameScorePair('LeeKoeun', 3, 2004),
        NameScorePair('LinTao', 2, 2002),
        NameScorePair('McNamara', 0, 2008),
        NameScorePair('Sinkev', 4, 2004),
        NameScorePair('YeSijing', 0, 2008),
        NameScorePair('Denisova', 3, 2008),
        NameScorePair('MunA', 5, 2015),
        NameScorePair('Zhou', 3, 2011),
        NameScorePair('Sladek', 1, 2011),
        NameScorePair('KimSuyeon', 5, 2011),
        NameScorePair('Tetzloff', 2, 2008),
        NameScorePair('Gasanov', 1, 2009),
        NameScorePair('Ko', 3, 2008),
        NameScorePair('Tan', 0, 2008),
        NameScorePair('Khmara', 1, 2008),
        NameScorePair('Kociuban', 3, 2008),
        NameScorePair('Levitsky', 4, 2008),
        NameScorePair('Nikiforov', 5, 2008),
        NameScorePair('ChenC', 1, 2006),
        NameScorePair('Yang', 0, 2006),
        NameScorePair('Solom', 0, 2004),
        NameScorePair('Lim', 0, 2002),
        NameScorePair('LuEric', 6, 2013),
        NameScorePair('GonzalezJ', 1, 2014),
        NameScorePair('Verbaite', 0, 2008),
        NameScorePair('Avdeeva', 1, 2006),
        # To be continued
    ))
    name_score_table.append(NameScorePair('MorozovS', 1, 2006))
    name_score_table.append(NameScorePair('Park', 1, 2006))
    name_score_table.append(NameScorePair('Savitski', 6, 2006))
    name_score_table.append(NameScorePair('Shelest', 0, 2006))
    name_score_table.append(NameScorePair('Stahievitch', 0, 2006))
    name_score_table.append(NameScorePair('Tysman', 0, 2006))
    name_score_table.append(NameScorePair('Giltburg', 0, 2002))
    name_score_table.append(NameScorePair('Hireche', 0, 2002))
    name_score_table.append(NameScorePair('Mikhailoff', 0, 2002))
    name_score_table.append(NameScorePair('Hireche', 0, 2002))
    name_score_table.append(NameScorePair('Stahievitch', 0, 2002))
    name_score_table.append(NameScorePair('SunMeiting', 6, 2002))
    name_score_table.append(NameScorePair('Adig', 1, 2004))
    name_score_table.append(NameScorePair('Benabd', 1, 2004))
    name_score_table.append(NameScorePair('Blinov', 1, 2004))
    name_score_table.append(NameScorePair('ChenJie', 6, 2004))
    name_score_table.append(NameScorePair('Choe', 0, 2004))
    name_score_table.append(NameScorePair('Danilo', 1, 2004))
    name_score_table.append(NameScorePair('Evstio', 5, 2004))
    name_score_table.append(NameScorePair('Faliks', 1, 2004))
    name_score_table.append(NameScorePair('Feiner', 0, 2004))
    name_score_table.append(NameScorePair('Fong', 1, 2004))
    name_score_table.append(NameScorePair('Gadeliya', 0, 2004))
    name_score_table.append(NameScorePair('Gordel', 0, 2004))
    name_score_table.append(NameScorePair('Hagino', 0, 2004))
    name_score_table.append(NameScorePair('Hong', 1, 2004))
    name_score_table.append(NameScorePair('Hsu', 0, 2004))
    name_score_table.append(NameScorePair('HuangB', 0, 2004))
    name_score_table.append(NameScorePair('HuangJ', 1, 2004))
    name_score_table.append(NameScorePair('Ishida', 0, 2004))
    name_score_table.append(NameScorePair('Ivleva', 1, 2004))
    name_score_table.append(NameScorePair('Karyagina', 1, 2004))
    name_score_table.append(NameScorePair('KimBenjamin', 2, 2004))
    name_score_table.append(NameScorePair('KimJ', 0, 2004))
    name_score_table.append(NameScorePair('KimW', 0, 2004))
    name_score_table.append(NameScorePair('Koleso', 4, 2004))
    name_score_table.append(NameScorePair('Krasnitsky', 2, 2004))
    name_score_table.append(NameScorePair('Kwon', 0, 2004))
    name_score_table.append(NameScorePair('LeeHwakyu', 0, 2004))
    name_score_table.append(NameScorePair('LeeJisun', 0, 2004))
    name_score_table.append(NameScorePair('Liao', 0, 2004))
    name_score_table.append(NameScorePair('Luo', 0, 2004))
    name_score_table.append(NameScorePair('Matsum', 0, 2004))
    name_score_table.append(NameScorePair('McVey', 0, 2004))
    name_score_table.append(NameScorePair('Moret', 0, 2004))
    name_score_table.append(NameScorePair('Nakaji', 0, 2004))
    name_score_table.append(NameScorePair('Ousset', 0, 2004))
    name_score_table.append(NameScorePair('Potamousis', 0, 2004))
    name_score_table.append(NameScorePair('Merjan', 0, 2004))
    name_score_table.append(NameScorePair('Schu', 1, 2004))
    name_score_table.append(NameScorePair('Sebastian', 0, 2004))
    name_score_table.append(NameScorePair('Shybay', 4, 2004))
    name_score_table.append(NameScorePair('Sudbin', 0, 2004))
    name_score_table.append(NameScorePair('SunJay', 0, 2004))
    name_score_table.append(NameScorePair('Teterin', 0, 2004))
    name_score_table.append(NameScorePair('Toivio', 0, 2004))
    name_score_table.append(NameScorePair('Ueno', 0, 2004))
    name_score_table.append(NameScorePair('Ushiki', 1, 2004))
    name_score_table.append(NameScorePair('Yoo', 5, 2004))
    name_score_table.append(NameScorePair('You', 0, 2004))
    name_score_table.append(NameScorePair('ZhouWenli', 0, 2004))
    name_score_table.append(NameScorePair('Arciglione', 2, 2006))
    name_score_table.append(NameScorePair('Avila', 0, 2006))
    name_score_table.append(NameScorePair('Bach', 0, 2006))
    name_score_table.append(NameScorePair('Benabdallah', 1, 2006))
    name_score_table.append(NameScorePair('Bogdanovich', 0, 2006))
    name_score_table.append(NameScorePair('CaiSheng', 0, 2006))
    name_score_table.append(NameScorePair('ChenS', 0, 2006))
    name_score_table.append(NameScorePair('DeTurck',4, 2006))
    name_score_table.append(NameScorePair('Dulu', 1, 2006))
    name_score_table.append(NameScorePair('Faliks', 1, 2006))
    name_score_table.append(NameScorePair('Feiner', 0, 2006))
    name_score_table.append(NameScorePair('Fung', 0, 2006))
    name_score_table.append(NameScorePair('Goldberg', 0, 2006))
    name_score_table.append(NameScorePair('Guzman', 0, 2006))
    name_score_table.append(NameScorePair('Han', 0, 2006))
    name_score_table.append(NameScorePair('Hao', 0, 2006))
    name_score_table.append(NameScorePair('Hirata', 0, 2006))
    name_score_table.append(NameScorePair('HouMiao', 0, 2006))
    name_score_table.append(NameScorePair('Huangci', 0, 2006))
    name_score_table.append(NameScorePair('Hwang', 0, 2006))
    name_score_table.append(NameScorePair('Izzard', 0, 2006))
    name_score_table.append(NameScorePair('JiaXin', 0, 2006))
    name_score_table.append(NameScorePair('Katyukova', 0, 2006))
    name_score_table.append(NameScorePair('Kavalerova', 0, 2006))
    name_score_table.append(NameScorePair('KimSunah', 0, 2006))
    name_score_table.append(NameScorePair('KorchinskayaKogan', 5, 2006))
    name_score_table.append(NameScorePair('Koshoeva', 0, 2006))
    name_score_table.append(NameScorePair('Krasnitsky', 2, 2006))
    name_score_table.append(NameScorePair('Larionova', 1, 2006))
    name_score_table.append(NameScorePair('LeeEunjin', 0, 2006))
    name_score_table.append(NameScorePair('LiuLangning', 0, 2006))
    name_score_table.append(NameScorePair('Mordvinov', 4, 2006))
    name_score_table.append(NameScorePair('MorozovS', 1, 2006))
    name_score_table.append(NameScorePair('MorozovY', 0, 2006))
    name_score_table.append(NameScorePair('Na', 1, 2006))
    name_score_table.append(NameScorePair('Namirovsky',1, 2006))
    name_score_table.append(NameScorePair('Pavlovic', 0, 2006))
    name_score_table.append(NameScorePair('Schmitt', 0, 2006))
    name_score_table.append(NameScorePair('Schneider', 0, 2006))
    name_score_table.append(NameScorePair('Sekino', 0, 2006))
    name_score_table.append(NameScorePair('Seo', 0, 2006))
    name_score_table.append(NameScorePair('Shamray', 1, 2006))
    name_score_table.append(NameScorePair('Shen', 1, 2006))
    name_score_table.append(NameScorePair('Shi', 1, 2006))
    name_score_table.append(NameScorePair('Shybayeva', 1, 2006))
    name_score_table.append(NameScorePair('Smirnov', 0, 2006))
    name_score_table.append(NameScorePair('Doe', 1, 2006))
    name_score_table.append(NameScorePair('Yanagitani', 5, 2006))
    name_score_table.append(NameScorePair('Yang', 0, 2006))
    name_score_table.append(NameScorePair('Yarden', 4, 2006))
    name_score_table.append(NameScorePair('Yu', 0, 2006))
    name_score_table.append(NameScorePair('Zagalskaia', 0, 2006))
    name_score_table.append(NameScorePair('Zhao', 0, 2006))
    name_score_table.append(NameScorePair('Zusko', 0, 2006))
    name_score_table.append(NameScorePair('Abdelmoula', 0, 2008))
    name_score_table.append(NameScorePair('Broberg', 0, 2008))
    name_score_table.append(NameScorePair('Cui', 1, 2008))
    name_score_table.append(NameScorePair('Duepree', 6, 2008))
    name_score_table.append(NameScorePair('Huang', 6, 2008))
    name_score_table.append(NameScorePair('KimEloise', 0, 2008))
    name_score_table.append(NameScorePair('Kleisen', 2, 2008))
    name_score_table.append(NameScorePair('Kochetkova', 0, 2008))
    name_score_table.append(NameScorePair('Ko', 3, 2008))
    name_score_table.append(NameScorePair('Kwok', 0, 2008))
    name_score_table.append(NameScorePair('Ladid', 0, 2008))
    name_score_table.append(NameScorePair('Lai', 0, 2008))
    name_score_table.append(NameScorePair('LinTami', 3, 2008))
    name_score_table.append(NameScorePair('Lisiecki', 5, 2008))
    name_score_table.append(NameScorePair('Li', 0, 2008))
    name_score_table.append(NameScorePair('Lo', 0, 2008))
    name_score_table.append(NameScorePair('Meng', 0, 2008))
    name_score_table.append(NameScorePair('Nedayvoda', 0, 2008))
    name_score_table.append(NameScorePair('Qin', 0, 2008))
    name_score_table.append(NameScorePair('Song', 1, 2008))
    name_score_table.append(NameScorePair('SunRan', 0, 2008))
    name_score_table.append(NameScorePair('Tan', 0, 2008))
    name_score_table.append(NameScorePair('Tario', 2, 2008))
    name_score_table.append(NameScorePair('Keanu', 1, 2008))
    name_score_table.append(NameScorePair('Tran', 0, 2008))
    name_score_table.append(NameScorePair('Tuncali', 0, 2008))
    name_score_table.append(NameScorePair('WangA', 1, 2008))
    name_score_table.append(NameScorePair('WangV', 0, 2008))
    name_score_table.append(NameScorePair('Wong', 0, 2008))
    name_score_table.append(NameScorePair('Marks', 2, 2008))
    name_score_table.append(NameScorePair('Yoon', 0, 2008))
    name_score_table.append(NameScorePair('Tim', 1, 2008))
    name_score_table.append(NameScorePair('ZhangX', 0, 2008))
    name_score_table.append(NameScorePair('Gorucan', 0, 2008))
    name_score_table.append(NameScorePair('Ahn', 0, 2009))
    name_score_table.append(NameScorePair('Albright', 0, 2009))
    name_score_table.append(NameScorePair('Atzinger', 0, 2009))
    name_score_table.append(NameScorePair('CaiY', 0, 2009))
    name_score_table.append(NameScorePair('CaiC', 1, 2009))
    name_score_table.append(NameScorePair('ChenL', 0, 2009))
    name_score_table.append(NameScorePair('Erice', 0, 2009))
    name_score_table.append(NameScorePair('Faliks', 0, 2009))
    name_score_table.append(NameScorePair('Falzone', 0, 2009))
    name_score_table.append(NameScorePair('Floril', 0, 2009))
    name_score_table.append(NameScorePair('Garritson', 1, 2009))
    name_score_table.append(NameScorePair('Gasanov', 1, 2009))
    name_score_table.append(NameScorePair('Georgieva', 0, 2009))
    name_score_table.append(NameScorePair('Gintov', 0, 2009))
    name_score_table.append(NameScorePair('Goh', 0, 2009))
    name_score_table.append(NameScorePair('Gokcin', 0, 2009))
    name_score_table.append(NameScorePair('Golubeva', 0, 2009))
    name_score_table.append(NameScorePair('Gryaznov', 1, 2009))
    name_score_table.append(NameScorePair('HouMiao', 0, 2009))
    name_score_table.append(NameScorePair('Huang', 0, 2009))
    name_score_table.append(NameScorePair('JiaRan', 1, 2009))
    name_score_table.append(NameScorePair('Jussow', 1, 2009))
    name_score_table.append(NameScorePair('Karpeyev', 0, 2009))
    name_score_table.append(NameScorePair('KimEunhae', 4, 2009))
    name_score_table.append(NameScorePair('Kunz', 0, 2009))
    name_score_table.append(NameScorePair('Lajko', 0, 2009))
    name_score_table.append(NameScorePair('Lariviere', 0, 2009))
    name_score_table.append(NameScorePair('LeeHanchien', 1, 2009))
    name_score_table.append(NameScorePair('Masycheva', 0, 2009))
    name_score_table.append(NameScorePair('Meek', 0, 2009))
    name_score_table.append(NameScorePair('Na', 4, 2009))
    name_score_table.append(NameScorePair('ParkH', 0, 2009))
    name_score_table.append(NameScorePair('ParkJ', 0, 2009))
    name_score_table.append(NameScorePair('Rozanski', 2, 2009))
    name_score_table.append(NameScorePair('Sekino', 1, 2009))
    name_score_table.append(NameScorePair('Seredenko', 0, 2009))
    name_score_table.append(NameScorePair('Shelest', 0, 2009))
    name_score_table.append(NameScorePair('Shi', 2, 2009))
    name_score_table.append(NameScorePair('Shilyaev', 0, 2009))
    name_score_table.append(NameScorePair('Soukhovetski', 1, 2009))
    name_score_table.append(NameScorePair('Staupe', 1, 2009))
    name_score_table.append(NameScorePair('Sychev', 0, 2009))
    name_score_table.append(NameScorePair('Tak', 1, 2009))
    name_score_table.append(NameScorePair('Tang', 0, 2009))
    name_score_table.append(NameScorePair('Taverna', 6, 2009))
    name_score_table.append(NameScorePair('Terenkova', 0, 2009))
    name_score_table.append(NameScorePair('Toscano', 0, 2009))
    name_score_table.append(NameScorePair('Travinskyy', 0, 2009))
    name_score_table.append(NameScorePair('Tysman', 5, 2009))
    name_score_table.append(NameScorePair('Ulasiuk', 0, 2009))
    name_score_table.append(NameScorePair('Wilshire', 0, 2009))
    name_score_table.append(NameScorePair('Wong', 0, 2009))
    name_score_table.append(NameScorePair('Xu', 0, 2009))
    name_score_table.append(NameScorePair('Yang', 1, 2009))
    name_score_table.append(NameScorePair('Yeletskiy', 5, 2009))
    name_score_table.append(NameScorePair('Zhao', 0, 2009))
    name_score_table.append(NameScorePair('Zhdanov', 1, 2009))
    name_score_table.append(NameScorePair('Zuber', 4, 2009))
    name_score_table.append(NameScorePair('Zukiewicz', 0, 2009))
    name_score_table.append(NameScorePair('Ahfat', 1, 2011))
    name_score_table.append(NameScorePair('Chon', 3, 2011))
    name_score_table.append(NameScorePair('Colafelice', 3, 2011))
    name_score_table.append(NameScorePair('Giesbrecht', 1, 2011))
    name_score_table.append(NameScorePair('Guo', 1, 2011))
    name_score_table.append(NameScorePair('HouKimberly', 2, 2011))
    name_score_table.append(NameScorePair('Kurz', 1, 2011))
    name_score_table.append(NameScorePair('Lan', 1, 2011))
    name_score_table.append(NameScorePair('LeeClaire', 1, 2011))
    name_score_table.append(NameScorePair('LinPeng', 2, 2011))
    name_score_table.append(NameScorePair('Lou', 1, 2011))
    name_score_table.append(NameScorePair('LuXingyu', 2, 2011))
    name_score_table.append(NameScorePair('Mizumoto', 3, 2011))
    name_score_table.append(NameScorePair('Ozaki', 4, 2011))
    name_score_table.append(NameScorePair('Rizikov', 1, 2011))
    name_score_table.append(NameScorePair('Sham', 6, 2011))
    name_score_table.append(NameScorePair('Shychko', 1, 2011))
    name_score_table.append(NameScorePair('Sladek', 1, 2011))
    name_score_table.append(NameScorePair('Song', 1, 2011))
    name_score_table.append(NameScorePair('Teo', 5, 2011))
    name_score_table.append(NameScorePair('WangZitong', 3, 2011))
    name_score_table.append(NameScorePair('Yi', 1, 2011))
    name_score_table.append(NameScorePair('ZhangYunling', 3, 2011))
    name_score_table.append(NameScorePair('Lan', 1, 2011))
    name_score_table.append(NameScorePair('Hebert', 1, 2013))
    name_score_table.append(NameScorePair('Ruan', 1, 2013))
    name_score_table.append(NameScorePair('Eras', 3, 2013))
    name_score_table.append(NameScorePair('Park', 3, 2013))
    name_score_table.append(NameScorePair('Yang', 5, 2013))
    name_score_table.append(NameScorePair('YeZ', 2, 2013))
    name_score_table.append(NameScorePair('Min', 4, 2013))
    name_score_table.append(NameScorePair('JinD', 2, 2013))
    name_score_table.append(NameScorePair('YeF', 2, 2013))
    name_score_table.append(NameScorePair('Mo', 3, 2013))
    name_score_table.append(NameScorePair('Kurz', 1, 2013))
    name_score_table.append(NameScorePair('Knoll', 5, 2013))
    name_score_table.append(NameScorePair('Tsianos',1, 2013))
    name_score_table.append(NameScorePair('Ozel', 3, 2013))
    name_score_table.append(NameScorePair('LuE', 6, 2013))
    name_score_table.append(NameScorePair('Narumi', 1, 2013))
    name_score_table.append(NameScorePair('WongT', 1, 2013))
    name_score_table.append(NameScorePair('Richardson', 4, 2013))
    name_score_table.append(NameScorePair('GuangC', 4, 2014))
    name_score_table.append(NameScorePair('LiuY', 1, 2014))
    name_score_table.append(NameScorePair('WangY', 1, 2014))
    name_score_table.append(NameScorePair('KyykhynenT', 1, 2014))
    name_score_table.append(NameScorePair('ShevchenkoO', 1, 2014))
    name_score_table.append(NameScorePair('HamS', 2, 2014))
    name_score_table.append(NameScorePair('KimHyejin', 2, 2014))
    name_score_table.append(NameScorePair('ParkJ', 2, 2014))
    name_score_table.append(NameScorePair('JohannsonP', 6, 2014))
    name_score_table.append(NameScorePair('GintovP', 2, 2014))
    name_score_table.append(NameScorePair('GonzalezJ', 1, 2014))
    name_score_table.append(NameScorePair('BrendleA', 1, 2014))
    name_score_table.append(NameScorePair('DupreeF', 5, 2014))
    name_score_table.append(NameScorePair('ChernovA', 5, 2014))
    name_score_table.append(NameScorePair('KharselM', 1, 2014))
    name_score_table.append(NameScorePair('MaximovI', 1, 2014))
    name_score_table.append(NameScorePair('MustakimovT', 2, 2014))
    name_score_table.append(NameScorePair('PrjevalskayaM', 4, 2014))
    name_score_table.append(NameScorePair('HuangS', 1, 2014))
    name_score_table.append(NameScorePair('GarritsonL', 1, 2014))
    name_score_table.append(NameScorePair('LeungM', 1, 2014))
    name_score_table.append(NameScorePair('ParkS', 1, 2014))
    name_score_table.append(NameScorePair('LuoJ', 2, 2015))
    name_score_table.append(NameScorePair('VuV', 1, 2015))
    name_score_table.append(NameScorePair('WangA', 1, 2015))
    name_score_table.append(NameScorePair('MiyashitaM', 1, 2015))
    name_score_table.append(NameScorePair('ChenW', 1, 2015))
    name_score_table.append(NameScorePair('LiYz', 4, 2015))
    name_score_table.append(NameScorePair('SunD', 1, 2015))
    name_score_table.append(NameScorePair('HuNY', 2, 2015))
    name_score_table.append(NameScorePair('ZhaoK', 2, 2015))
    name_score_table.append(NameScorePair('WongWY', 2, 2015))
    name_score_table.append(NameScorePair('JeonH', 2, 2015))
    name_score_table.append(NameScorePair('BorickC', 2, 2015))
    name_score_table.append(NameScorePair('Bult-ItoS', 1, 2015))
    name_score_table.append(NameScorePair('LeeN', 6, 2015))
    name_score_table.append(NameScorePair('LeeE', 1, 2015))
    name_score_table.append(NameScorePair('LiuC', 1, 2015))
    name_score_table.append(NameScorePair('LuA', 1, 2015))
    name_score_table.append(NameScorePair('LuM', 1, 2015))
    name_score_table.append(NameScorePair('Richardson', 4, 2015))
    name_score_table.append(NameScorePair('WuuE', 5, 2015))
    name_score_table.append(NameScorePair('YoungS', 2, 2015))


    return name_score_table

TABLE = define_perf_name_to_score()
ART_NAME= re.compile('^[A-Za-z-]+')
YEAR = re.compile('[0-9]{4}')
LIST_YEARS = [2002, 2004, 2006, 2008, 2009, 2011, 2013, 2014, 2015]

def cal_score(name):
    artist_name = ART_NAME.match(name).group().lower()
    year = YEAR.match(name)

    if year:
        score = TABLE.get_score(artist_name, year)
    else:
        score, year = TABLE.get_score(artist_name)

    print(artist_name, score, year)


    score_year = [0] * 10
    score_year[0] = score
    year_index = LIST_YEARS.index(year)
    score_year[year_index+1] = 1

    return score_year
