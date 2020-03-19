onmt-main --config data.yml --auto_config export --export_dir exported/
cp *vocab* exported/
zip -r exported.zip exported/
