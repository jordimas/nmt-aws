VOCSIZE=50000
onmt-build-vocab --sentencepiece --size $VOCSIZE --save_vocab src-vocab.txt src-train.txt
onmt-build-vocab --sentencepiece --size $VOCSIZE --save_vocab tgt-vocab.txt tgt-train.txt
