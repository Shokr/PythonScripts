#!/bin/sh

# Bash script that takes a screenshot every seconds for an hour then make a video form the shots, it is good script if you want to know where did the time go.

seconds=120

if [ ! -d "$HOME/watcher" ]; then
  mkdir "$HOME/watcher"
fi
echo "Taking screenshots, the plan is to go like that for an hour"
for counter in $(seq -f "%05g" 0 $seconds); do
  screencapture -x -C "$HOME/watcher/$counter.png"
  convert $HOME/watcher/$counter.png -scale 40% $HOME/watcher/$counter.jpg
  rm "$HOME/watcher/$counter.png"
  sleep 1
done

echo "Making the video."
ffmpeg -framerate 15 -pattern_type glob -i "$HOME/watcher/*.jpg" -c:v libx264 "$HOME/watcher/out.mp4"

echo "Deleting not imporant files."
for counter in $(seq -f "%05g" 0 $seconds); do
  rm "$HOME/watcher/$counter.jpg"
done
