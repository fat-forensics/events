#! /usr/bin/env bash

OUT_DIR=../../../_quarto/2022_UNSW-lecture

mkdir -p $OUT_DIR

quarto render intro.qmd
sed "s+../../../assets/images/+../../assets/images/+g" intro.html > $OUT_DIR/intro.html
rm intro.html
rm -fr $OUT_DIR/intro_files
mv intro_files $OUT_DIR

quarto render intro_deux.qmd
sed "s+../../../assets/images/+../../assets/images/+g" intro_deux.html > $OUT_DIR/intro_deux.html
rm intro_deux.html
rm -fr $OUT_DIR/intro_deux_files
mv intro_deux_files $OUT_DIR
