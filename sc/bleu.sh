onmt-main --config data.yml --auto_config infer --features_file src-test.txt.token > predictions.txt
perl ../OpenNMT-py/tools/multi-bleu.perl tgt-test.txt.token < predictions.txt 

