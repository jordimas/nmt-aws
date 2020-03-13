#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import polib
import re

def split_in_six_files():

    srcs = set()
    percentage_train = 90
    percentage_validation = 5
    cnt = 0
    pairs = 0

    print("Split src and tgt files in 6 files for training, text and validation")

    with open("src-val.txt", "w") as source_val,\
        open("tgt-val.txt", "w") as target_val,\
        open("src-test.txt", "w") as source_test,\
        open("tgt-test.txt", "w") as target_test,\
        open("src-train.txt", "w") as source_train,\
        open("tgt-train.txt", "w") as target_train,\
        open("src.txt", "r") as read_source,\
        open("tgt.txt", "r") as read_target:

        src = read_source.readline()
        trg = read_target.readline()

        while src and trg:
            pairs = pairs + 1

            if cnt < percentage_train:
                source = source_train
                target = target_train
            elif cnt < percentage_train + percentage_validation:
                source = source_val
                target = target_val
            else:
                source = source_test
                target = target_test

            source.write(src)
            target.write(trg)
            cnt = cnt + 1
            if cnt >= 100:
                cnt = 0

            src = read_source.readline()
            trg = read_target.readline()


    print("Pairs: " + str(pairs))

def append_lines_from_file(src_filename, trg_file):
    lines = 0
    with open(src_filename, 'r') as tf:
        line = tf.readline()
        while line:
            lines += 1
            trg_file.write(line)
            line = tf.readline()

    print("Appended {0} to {1}".format(lines, src_filename))
    return lines

def generate_two_files():

    src_lines = 0
    trg_lines = 0

    print("Join multiple files in two src and tgt files")
    with open("src.txt", "w") as source,\
        open("tgt.txt", "w") as target:

        src_lines += append_lines_from_file("totes-memories/src.txt", source)
        src_lines += append_lines_from_file("Wikimatrix/WikiMatrix.en-ca.txt.en", source)
        src_lines += append_lines_from_file("global-voices/globalvoices-en.txt", source)
        src_lines += append_lines_from_file("jaume/europarl.en-ca.en", source)
        src_lines += append_lines_from_file("jaume/OpenSubtitles2018.en-ca.en", source)
        src_lines += append_lines_from_file("jaume/tedtalks.en-ca.en", source)

        trg_lines += append_lines_from_file("totes-memories/tgt.txt", target)
        trg_lines += append_lines_from_file("Wikimatrix/WikiMatrix.en-ca.txt.ca", target)
        trg_lines += append_lines_from_file("global-voices/globalvoices-ca.txt", target)
        trg_lines += append_lines_from_file("jaume/europarl.en-ca.ca", target)
        trg_lines += append_lines_from_file("jaume/OpenSubtitles2018.en-ca.ca", target)
        trg_lines += append_lines_from_file("jaume/tedtalks.en-ca.ca", target)


    print("src lines: " + str(src_lines))
    print("trg lines: " + str(trg_lines))


def main():

    print("Converts from PO to OpenNMT text files sets")
    generate_two_files()
    split_in_six_files()

if __name__ == "__main__":
    main()
