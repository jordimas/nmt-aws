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

import pyonmttok

def end_end_sample():

    # Create model
    #learner = pyonmttok.SentencePieceLearner(vocab_size=32000)
    #learner.ingest_file("src-test.txt")
    #tokenizer = learner.learn("en_m.model")

    # Tokenize
    learner = pyonmttok.SentencePieceLearner(vocab_size=32000)
    text = "I'm loving it more than I expected"
    tokenizer = pyonmttok.Tokenizer(mode="none", sp_model_path="en_m.model")    
    tokens, features = tokenizer.tokenize(text)
    print(tokens)
    

    # Destokenize
    text, ranges = tokenizer.detokenize_with_ranges(tokens, merge_ranges=True)    
    print(text)

def src():
    learner = pyonmttok.SentencePieceLearner(vocab_size=100000)
    learner.ingest_file("src-train.txt")
    tokenizer = learner.learn("en_m.model", verbose=True)
    tokens = tokenizer.tokenize_file("src-train.txt", "src-train.txt.token")

def tgt():
    learner = pyonmttok.SentencePieceLearner(vocab_size=100000)
    learner.ingest_file("tgt-train.txt")
    tokenizer = learner.learn("ca_m.model", verbose=True)
    tokens = tokenizer.tokenize_file("tgt-train.txt", "tgt-train.txt.token")


def main():

    print("Creates tokenized output corpus using SentencePiece")
    src()
    tgt()

if __name__ == "__main__":
    main()
