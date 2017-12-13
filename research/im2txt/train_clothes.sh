bazel-bin/im2txt/train \
  --input_file_pattern="data/clothes/train-?????-of-00256" \
  --inception_checkpoint_file="data/inception_v3.ckpt" \
  --train_dir="model/train" \
  --train_inception=false \
  --number_of_steps=1000000
