rm $2/*

task1_dir="$1/res/Task1"
task2_dir="$1/res/Task2"

if [ -d "$task1_dir" ]; then
    bash $3/task1.sh $1 $2 $3
fi

if [ -d "$task2_dir" ]; then
    bash $3/task2.sh $1 $2 $3
fi
