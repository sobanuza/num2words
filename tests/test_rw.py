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
from __future__ import unicode_literals

from unittest import TestCase

from num2words import num2words

TEST_CASES_CARDINAL = (
    (1, 'rimwe'),
    (2, 'kabiri'),
    (3, 'gatatu'),
    (5.5, 'gatanu n\' ibice bitanu'),
    (11, 'cumi na rimwe'),
    (12, 'cumi na kabiri'),
    (16, 'cumi na gatandatu'),
    (17.42, 'cumi na karindwi n\' ibice mirongo ine na bibiri'),
    (19, 'cumi ni cyenda'),
    (20, 'makumyabiri'),
    (21, 'makumyabiri na rimwe'),
    (26, 'makumyabiri na gatandatu'),
    (27.312, 'makumyabiri na karindwi n\' ibice magana atatu na cumi na kabiri'),
    (28, 'makumyabiri n\' umunani'),
    (30, 'mirongo itatu'),
    (31, 'mirongo itatu na rimwe'),
    (40, 'mirongo ine'),
    (44, 'mirongo ine na kane'),
    (50, 'mirongo itanu'),
    (53.486, 'mirongo itanu na gatatu n\' ibice magana ane na mirongo inane na gatandatu'),
    (55, 'mirongo itanu na gatanu'),
    (60, 'mirongo itandatu'),
    (67, 'mirongo itandatu na karindwi'),
    (70, 'mirongo irindwi'),
    (79, 'mirongo irindwi n\' icyenda'),
    (89, 'mirongo inani n\' icyenda'),
    (95, 'mirongo icyenda na gatanu'),
    (100, 'ijana'),
    (101, 'ijana na rimwe'),
    (199, 'ijana na mirongo icyenda n\' icyenda'),
    (203, 'magana abiri na gatatu'),
    (287, 'magana atatu na mirongo inani na karindwi'),
    (300.42, 'magana atatu n\' ibice mirongo ine na kabiri'),
    (356, 'magana atatu na mirongo itanu na gatandatu'),
    (400, 'magana ane'),
    (434, 'magane ane na mirongo itatu na kane'),
    (578, 'magana atanu na mirongo irindwi n\' umunani'),
    (689, 'magana atandatu na mirongo inani n\' icyenda'),
    (729, 'magana arindwi na makumyabiri n\' icyenda'),
    (894, 'magana inani na mirongo icyenda na kane'),
    (999, 'magana icyenda na mirongo icyenda n\' icyenda'),
    (1000, 'igihumbi'),
    (1001, 'igihumbi na rimwe'),
    (1097, 'igihumbi na mirongo icyenda na karindwi'),
    (1104, 'igihumbi n\' ijana na kane'),
    (1243, 'igihumbi na magana abiri na mirongo ine na gatatu'),
    (2385, 'ibihumbi bibiri na magana atatu na mirongo inani na gatanu'),
    (3766, 'ibihumbi bitatu na magana arindwi na mirongo itandatu na gatandatu'),
    (4196, 'ibihumbi bine n\' ijana na mirongo icyenda na gatandatu'),
    (4196.42, 'ibihumbi bine n\' ijana na mirongo icyenda na gatandatu n\' ibice mirongo ine na kabiri'),
    (5846, 'ibihumbi bitanu na magana umunani na mirongo ine na gatandatu'),
    (6459, 'ibihumbi bitandatu na magana ane na mirongo itanu n\' icyenda'),
    (7232, 'ibihumbi birindwi na magana abiri na mirongo itatu na kabiri'),
    (8569, 'ibihumbi umunani na magana atanu na mirongo itandatu n\' icyenda'),
    (9539, 'ibihumbi bitanu na magana atanu na mirongo itatu n\' icyenda'),
    (1000000, 'miriyoni'),
    (1000001, 'miriyoni na rimwe'),
    (4000000, 'miliyone ine'),
    (4000004, 'miriyoni ine na kane'),
    (4300000, 'miriyoni ine n\' ibihumbi magana atatu'),
    (80000000, 'miriyoni mirongo inani'),
    (300000000, 'miriyoni magana atatu'),
    (10000000000000, 'miriyari icumi'),
    (10000000000010, 'miriyari icumi n\' icumi'),
    (100000000000000, 'miriyari ijana'),
    (1000000000000000000, 'tiriyoni'),
    (1000000000000000000000, 'tiriyari'),
    (10000000000000000000000000, 'kwadiriyoni icumi')
)

TEST_CASES_ORDINAL = (
    (1, 'uwa mbere'),
    (8, 'uwa munani'),
    (12, 'uwa cumi na kabiri'),
    (14, 'uwa cumi na kane'),
    (28, 'uwa makumyabiri n\' umunani'),
    (100, 'uw\' ijana'),
    (1000, 'uw\' igihumbi'),
    (1000000, 'uwa miriyone'),
    (1000000000000000, 'uwa biriyari'),
    (1000000000000000000, 'uwa tiriyari')  # over 1e18 is not supported
)

TEST_CASES_ORDINAL_NUM = (
    (1, 'uwa 1'),
    (8, 'uwa 8'),
    (11, 'uwa 11'),
    (12, 'uwa 12'),
    (14, 'uwa 14'),
    (21, 'uwa 21'),
    (28, 'uwa 28'),
    (100, 'uwa 100'),
    (101, 'uwa 101'),
    (1000, 'uwa 1000'),
    (1000000, 'uwa 1000000')
)

TEST_CASES_TO_CURRENCY_EUR = (
    (1.00, 'iyero rimwe n\' ibice zeru'),
    (2.01, 'amayero abiri n\'igice kimwe'),
    (8.10, 'amayero umunani n\' ibice icumi'),
    (12.26, 'amayero cumi n\' abiri n\' ibice makumyabiri na bitandatu'),
    (21.29, 'amayero makumyabiri n\' ibice makumyabiri n\' icyenda'),
    (81.25, 'amayero mirongo inani n\' ibice makumyabiri na bitanu'),
    (100.00, 'amayero ijana n\' ibice zeru'),
)

TEST_CASES_TO_CURRENCY_RWF = (
    (1.00, 'ifaranga rimwe n\' ibice zeru'),
    (2.01, 'amafaranga abiri n\'igice kimwe'),
    (8.10, 'amafaranga umunani n\' ibice icumi'),
    (12.26, 'amafaranga cumi n\' abiri n\' ibice makumyabiri na bitandatu'),
    (21.29, 'amafaranga makumyabiri n\' ibice makumyabiri n\' icyenda'),
    (81.25, 'amafaranga mirongo inani n\' ibice makumyabiri na bitanu'),
    (100.00, 'amafaranga ijana n\' ibice zeru'),
)

TEST_CASES_TO_CURRENCY_USD = (
    (1.00, 'idolari rimwe n\' amasenti zeru'),
    (2.01, 'amadolari abiri n\'amasenti kimwe'),
    (8.10, 'amadolari umunani n\' amasenti icumi'),
    (12.26, 'amadolari cumi n\' abiri n\' amasenti makumyabiri na bitandatu'),
    (21.29, 'amadolari makumyabiri n\' amasenti makumyabiri n\' icyenda'),
    (81.25, 'amadolari mirongo inani n\' amasenti makumyabiri na bitanu'),
    (100.00, 'amadolari ijana n\' amasenti zeru'),
)


class Num2WordsRWTest(TestCase):
    def test_ordinal_special_joins(self):
        # ref https://github.com/savoirfairelinux/num2words/issues/18
        self.assertEqual(
            num2words(5, ordinal=True, lang='rw'), "uwa gatanu"
        )
        self.assertEqual(
            num2words(35, ordinal=True, lang='rw'), "uwa mirongo itatu na gatanu"
        )
        self.assertEqual(
            num2words(9, ordinal=True, lang='rw'), "uwa cyenda"
        )
        self.assertEqual(
            num2words(49, ordinal=True, lang='rw'), "uwa mirongo ine n\' icyenda"
        )

    def test_number(self):
        for test in TEST_CASES_CARDINAL:
            self.assertEqual(num2words(test[0], lang='rw'), test[1])

    def test_ordinal(self):
        for test in TEST_CASES_ORDINAL:
            self.assertEqual(
                num2words(test[0], lang='rw', ordinal=True),
                test[1]
            )

    def test_ordinal_num(self):
        for test in TEST_CASES_ORDINAL_NUM:
            self.assertEqual(
                num2words(test[0], lang='rw', to='ordinal_num'),
                test[1]
            )

    def test_currency_eur(self):
        for test in TEST_CASES_TO_CURRENCY_EUR:
            self.assertEqual(
                num2words(test[0], lang='rw', to='currency', currency='EUR'),
                test[1]
            )

    def test_currency_frf(self):
        for test in TEST_CASES_TO_CURRENCY_RWF:
            self.assertEqual(
                num2words(test[0], lang='rw', to='currency', currency='RWF'),
                test[1]
            )

    def test_currency_usd(self):
        for test in TEST_CASES_TO_CURRENCY_USD:
            self.assertEqual(
                num2words(test[0], lang='rw', to='currency', currency='USD'),
                test[1]
            )
