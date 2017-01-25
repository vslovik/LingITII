#!/usr/bin/env bash

#ffmpeg="/home/valeriya/project/ffmpeg-3.2.2-64bit-static/ffmpeg"
input="/home/valeriya/project/LingITII/sound2/DGmtA01F"
i=1
s=0
max=925
step=10
overlap=5
while [ $s -lt $max ] && [ $s -gt -1 ]
do
    e=$(($s+$step))
    echo "Start: $s end: $e"
    space="_"
    output=$input$space$i
    ffmpeg -ss $s -t $step -i $input.wav $output.wav
    s=$(($e-$overlap))
    i=$(($i+1))
    echo $i
done
