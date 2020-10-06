cd ./setup/
for d in */ ; do
    cd "$d"
    echo "$pwd"
    rm *.log
    bash program/run.sh input output program 1> out.log 2> err.log
    cd -
done
