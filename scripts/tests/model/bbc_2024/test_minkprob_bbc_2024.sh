python main.py \
--method min-prob \
--local_port 6000 \
--local_port_2 6000 \
--model_name llama \
--model_name_2 llama \
--top_logprobs 5 \
--max_tokens 1 \
--echo \
--eval_data_name "RealTimeData/bbc_news_alltime" \
--eval_data_config_name "2024-02" \
--eval_set_key train \
--text_keys "description+section+content" \
--n_eval_data_points 100 \
--max_request_time 10 \
--num_proc 64 \
--output_dir ./output_dir/min_prob/llama2/bbc-2024

python main.py \
--method min-prob \
--local_port 6000 \
--local_port_2 6000 \
--model_name mistral-ins \
--model_name_2 mistral-ins \
--top_logprobs 5 \
--max_tokens 1 \
--echo \
--eval_data_name "RealTimeData/bbc_news_alltime" \
--eval_data_config_name "2024-02" \
--eval_set_key train \
--text_keys "description+section+content" \
--n_eval_data_points 100 \
--max_request_time 10 \
--num_proc 64 \
--output_dir ./output_dir/min_prob/mistral-ins/bbc-2024

python main.py \
--method min-prob \
--local_port 6000 \
--local_port_2 6000 \
--model_name qwen \
--model_name_2 qwen \
--top_logprobs 5 \
--max_tokens 1 \
--echo \
--eval_data_name "RealTimeData/bbc_news_alltime" \
--eval_data_config_name "2024-02" \
--eval_set_key train \
--text_keys "description+section+content" \
--n_eval_data_points 100 \
--max_request_time 10 \
--num_proc 64 \
--output_dir ./output_dir/min_prob/qwen/bbc-2024