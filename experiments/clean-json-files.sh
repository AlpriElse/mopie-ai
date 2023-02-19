ls | grep --include *.json | xargs -I {} rm "{}"

rm -rf downloads