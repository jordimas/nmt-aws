echo   rm -f exported.zip
modelDescription="exported/assets/model_description.txt"
currentDate=`date +"%Y-%m-%d-%s"`
read -p 'Describe model: ' uservar
onmt-main --config data.yml --auto_config export --export_dir exported/
echo "Model description: $uservar" >  $modelDescription
cat bleu.txt >>  $modelDescription
echo "Date: $currentDate" >> $modelDescription
ls *.txt -l > exported/assets/inputs_used.txt
cp *.model exported/assets/
cp data.yml exported/assets/
zip -r exported-$currentDate.zip exported/
