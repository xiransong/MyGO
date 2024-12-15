project_root="/Users/xiransong/Code/MyTeam_Project"

code_root=$project_root"/MyTeam"
all_data_root=$project_root"/data"

cd $code_root
uv run python -m MyTeam.dataset.mmlu.download --all-data-root $all_data_root
