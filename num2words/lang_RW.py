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
    CURRENCY_FORMS = {
        'EUR': (('iyero', 'amayero'), ('igice', 'ibice')),
        'USD': (('idolari', 'amadolari'), ('senti', 'amasenti')),
        'RWF': (('ifaranga', 'amafaranga'), ('igice', 'ibice')),
    }
    
    def set_high_numwords(self, high):
        max = 3 + 3 * len(high)
        for word, n in zip(high, range(max, 3, -3)):
            self.cards[10 ** n] = word + "illion"

    def setup(self):
        super(Num2Word_RW, self).setup()

        self.negword = "munsi ya zeru"
        self.pointword = "n' ibice"
        self.exclude_title = ["na", "ibice", "munsi ya zeru"] #"n'" 

        self.mid_numwords = [(1000, "igihumbi"), (100, "ijana"),  (90, "mirongo icyenda"), 
                             (80, "mirongo inani"), (70, "mirongo irindwi"), (60, "mirongo itandatu"), 
                             (50, "mirongo itanu"), (40, "mirongo ine"), (30, "mirongo itatu")]
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
                     "cumi": "uwa cumi",
                     "cumi na rimwe": "uwa cumi na rimwe",
                     "cumi na kabiri": "uwa cumi na kabiri"}

    def merge(self, lpair, rpair):
        # print("lpair: " + str(lpair))
        # print("rpair: " + str(rpair))
        ltext, lnum = lpair
        rtext, rnum = rpair
        joiner = "na"
        if rtext[0] in ('a', 'e', 'i', 'o', 'u'):
            joiner = "n'"
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum:
            return ("%s %s %s" % (ltext, joiner, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s %s" % (ltext, joiner, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s %s" % (ltext, joiner, rtext), lnum * rnum)
        return ("%s %s %s" % (ltext, joiner, rtext), lnum + rnum)

    def to_ordinal(self, value):
        self.verify_ordinal(value)
        word = self.to_cardinal(value)
        if value == 1:
            word = "mbere"
        if word[0] in ('a', 'e', 'i', 'o', 'u'):
            return "uw' " + word
        else:
            return "uwa " + word

    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return "uwa " + str(value)

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
