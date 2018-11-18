#!/usr/bin/env bash

print_usage()
{
  echo "usage:"
  echo "  build.sh --development|--production (you need to supply either --development or --production)"
  echo "  In production mode, the docker build cache is removed to reduce the image size."
}

for arg in $@;
do
  if [ "$arg" == "--development" ]
  then
    if [ "$mode" == "prod" ]
    then
      echo "Only one of --development and --production can be specified!"
      echo ""
      print_usage
      exit 1
    fi
    mode=devel
  elif [ "$arg" == "--production" ]
  then
    if [ "$mode" == "devel" ]
    then
      echo "Only one of --development and --production can be specified!"
      echo ""
      print_usage
      exit 1
    fi
    mode=prod
  elif [[ "$arg" == "--help" || "$arg" == "-h" ]]
  then
    print_usage
    exit 0
  fi
done

if [ -z "$mode" ];
then
  echo "Invalid or missing argument!"
  echo ""
  print_usage
  exit 1
fi

# Download/update repositories
[ -d hiob_msgs ] && rm -rf hiob_msgs
git clone --depth 1 https://github.com/theCalcaholic/hiob_msgs
[ -d hiob_ros ] && rm -rf hiob_ros
git clone --depth 1 --recurse-submodules https://github.com/theCalcaholic/hiob_ros

if [ "$mode" == "prod" ];
then
  docker build --no-cache --squash --rm ./ -t hiob_ros || echo "An error occured! Did you enable experimental features for docker?"
else
  docker build --rm ./ -t hiob_ros
fi


rm -rf hiob_msgs
rm -rf hiob_ros
