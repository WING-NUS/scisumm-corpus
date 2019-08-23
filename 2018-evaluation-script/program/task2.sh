python $3/create_setting_task2_rouge.py $1 $2 abstract
$3/rouge/ROUGE-1.5.5.pl -e $3/rouge/data -f A -a -x -s -d -t 1 -m -2 -4 -u -n 2 $2/task2_settings.xml > $2/task2_raw
python $3/task2_eval.py $1 $2 abstract
# rm $2/task2_settings.xml
# rm $2/task2_raw
python $3/create_setting_task2_rouge.py $1 $2 community
$3/rouge/ROUGE-1.5.5.pl -e $3/rouge/data -f A -a -x -s -d -t 1 -m -2 -4 -u -n 2 $2/task2_settings.xml > $2/task2_raw
python $3/task2_eval.py $1 $2 community
# rm $2/task2_settings.xml
# rm $2/task2_raw
python $3/create_setting_task2_rouge.py $1 $2 human
$3/rouge/ROUGE-1.5.5.pl -e $3/rouge/data -f A -a -x -s -d -t 1 -m -2 -4 -u -n 2 $2/task2_settings.xml > $2/task2_raw
python $3/task2_eval.py $1 $2 human
rm $2/task2_settings.xml
rm $2/task2_raw
# python $3/create_setting_task2_rouge.py $1 $2 combined
# $3/rouge/ROUGE-1.5.5.pl -e $3/rouge/data -f A -a -x -s -d -t 1 -m -2 4 -u -n 2 $2/task2_settings.xml > $2/task2_raw
# python $3/task2_eval.py $1 $2 comnined
# rm $2/task2_settings.xml
# rm $2/task2_raw
