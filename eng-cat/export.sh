echo   rm -f exported.zip
currentDate=`date +"%Y-%m-%d-%s"`
read -p 'Describe model: ' uservar
onmt-main --config data.yml --auto_config export --export_dir exported/
echo "Model description: $uservar" >  exported/assets/model_description.txt
cat bleu.txt >>  exported/assets/model_description.txt
ls *.txt -l > exported/assets/inputs_used.txt
cp *.model exported/assets/
cp data.yml exported/assets/
zip -r exported-$currentDate.zip exported/
