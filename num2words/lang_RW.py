# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, print_function, unicode_literals

from . import lang_EU


class Num2Word_RW(lang_EU.Num2Word_EU):
    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "illion"

    def setup(self):
        super(Num2Word_EN, self).setup()

        self.negword = "munsi ya zeru"
        self.pointword = "n' ibice"
        self.exclude_title = ["na", "ibice", "munsi ya zeru"] #"n'" 

        self.mid_numwords = [(1000, "igihumbi"), (100, "hundred"),
                             (90, "ninety"), (80, "eighty"), (70, "seventy"),
                             (60, "sixty"), (50, "fifty"), (40, "forty"),
                             (30, "thirty")]
        self.low_numwords = ["makumyabiri", "cumi n'icyenda", "cumi n'umunani", "cumi na karindi",
                             "cumi na gatandatu", "cumi na gatanu", "cumi na kane", "cumi na gatatu",
                             "cumi na kabiri", "cumi na rimwe", "icumi", "icyenda", "umunani",
                             "karindwi", "gatandatu", "gatanu", "kane", "gatatu", "kabiri",
                             "rimwe", "zeru"]
        self.ords = {"rimwe": "uwa mbere",
                     "kabiri": "uwa kabiri",
                     "gatatu": "uwa gatatu",
                     "kane": "uwa kane",
                     "gatanu": "uwa gatanu",
                     "gatandatu": "uwa gatandatu",
                     "karindwi": "uwa karindwi",
                     "umunani": "uwa munani",
                     "icyenda": "uwa cyenda",
                     "icumi": "uwa cumi",
                     "cumi na rimwe": "uwa cumi na rimwe",
                     "cumi na kabiri": "uwa cumi na kabiri"}

    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s-%s" % (ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s and %s" % (ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s" % (ltext, rtext), lnum * rnum)
        return ("%s, %s" % (ltext, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value).split(" ")
        lastwords = outwords[-1].split("-")
        lastword = lastwords[-1].lower()
        try:
            lastword = self.ords[lastword]
        except KeyError:
            if lastword[-1] == "y":
                lastword = lastword[:-1] + "ie"
            lastword += "th"
        lastwords[-1] = self.title(lastword)
        outwords[-1] = "-".join(lastwords)
        return " ".join(outwords)

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "%s%s" % (value, self.to_ordinal(value)[-2:])

    def to_year(self, val, suffix=None, longval=True):
        if val < 0:
            val = abs(val)
            suffix = 'BC' if not suffix else suffix
        high, low = (val // 100, val % 100)
        # If year is 00XX, X00X, or beyond 9999, go cardinal.
        if (high == 0
                or (high % 10 == 0 and low < 10)
                or high >= 100):
            valtext = self.to_cardinal(val)
        else:
            hightext = self.to_cardinal(high)
            if low == 0:
                lowtext = "hundred"
            elif low < 10:
                lowtext = "oh-%s" % self.to_cardinal(low)
            else:
                lowtext = self.to_cardinal(low)
            valtext = "%s %s" % (hightext, lowtext)
        return (valtext if not suffix
                else "%s %s" % (valtext, suffix))
                
                
# sources
# https://elias.unix.fas.harvard.edu/unit-grammar/cardinal-and-ordinal-numbers
# https://glosbe.com/en/rw/ten
